#!/usr/bin/env python3
"""
Script para generar índices automáticos (index2.md) en todas las carpetas
de documentación de MkDocs, excepto las excluidas.

Uso:
    python generate_indexes.py [--docs-dir docs] [--exclude servicios,otracarpeta]

Genera archivos index2.md en cada carpeta, sin sobrescribir los originales.
"""

import os
import argparse
import frontmatter
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# -----------------------------------------------------------------------------
# Configuración inicial
# -----------------------------------------------------------------------------
DEFAULT_EXCLUDED_DIRS = [
    "servicios", "js", "assets", "docs", "perfiles", "contacto", "cursos",     # carpeta excluida fija
    # Añade aquí otras carpetas que no quieras indexar automáticamente
]

# -----------------------------------------------------------------------------
# Funciones auxiliares
# -----------------------------------------------------------------------------

def get_title_from_path(path: Path) -> str:
    """Convierte un nombre de carpeta/archivo en un título amigable."""
    # Elimina extensión si es archivo
    name = path.stem if path.is_file() else path.name
    # Reemplaza guiones y underscores por espacios
    name = name.replace("-", " ").replace("_", " ")
    # Capitaliza palabras, excepto artículos cortos (opcional)
    return name.title()

def get_frontmatter_data(md_file: Path) -> dict:
    """Extrae los metadatos del frontmatter de un archivo .md."""
    try:
        post = frontmatter.load(md_file)
        return dict(post.metadata)
    except Exception as e:
        print(f"⚠️ Error leyendo {md_file}: {e}")
        return {}

def get_file_title(md_file: Path) -> str:
    """Obtiene el título del archivo: frontmatter 'title' o nombre legible."""
    meta = get_frontmatter_data(md_file)
    if "title" in meta and meta["title"]:
        return meta["title"]
    return get_title_from_path(md_file)

def get_file_description(md_file: Path) -> str:
    """Obtiene la descripción del frontmatter o cadena vacía."""
    meta = get_frontmatter_data(md_file)
    return meta.get("description", "")

def get_file_categories(md_file: Path) -> List[str]:
    """Obtiene categorías del frontmatter (lista o cadena separada por comas)."""
    meta = get_frontmatter_data(md_file)
    cats = meta.get("categories", [])
    if isinstance(cats, str):
        cats = [c.strip() for c in cats.split(",")]
    return cats

# -----------------------------------------------------------------------------
# Generación del contenido del índice
# -----------------------------------------------------------------------------

def generate_index_content(folder: Path, docs_dir: Path, is_root: bool = False) -> str:
    """
    Genera el contenido Markdown para el índice de una carpeta.
    
    Args:
        folder: Ruta absoluta a la carpeta
        docs_dir: Ruta absoluta a docs/
        is_root: Si es la carpeta raíz (docs/)
    """
    # Título principal: nombre de la carpeta o del sitio para la raíz
    if is_root:
        title = "Inicio"
    else:
        # Obtener título desde posible index.md existente, o del nombre de carpeta
        existing_index = folder / "index.md"
        if existing_index.exists():
            meta = get_frontmatter_data(existing_index)
            if "title" in meta and meta["title"]:
                title = meta["title"]
            else:
                title = get_title_from_path(folder)
        else:
            title = get_title_from_path(folder)
    
    # Construir ruta relativa para enlaces
    rel_folder = folder.relative_to(docs_dir)
    
    # Contenido del índice
    lines = []
    lines.append("---")
    lines.append(f"title: {title}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    
    # Descripción automática
    num_subdirs = len([d for d in folder.iterdir() if d.is_dir() and not d.name.startswith('.')])
    num_files = len([f for f in folder.iterdir() if f.is_file() and f.suffix == '.md' and f.name not in ['index.md', 'index2.md']])
    
    if num_subdirs > 0 or num_files > 0:
        desc_parts = []
        if num_subdirs > 0:
            desc_parts.append(f"{num_subdirs} sección(es)")
        if num_files > 0:
            desc_parts.append(f"{num_files} artículo(s)")
        desc = f"Esta sección contiene {' y '.join(desc_parts)}."
        lines.append(f"{desc}")
        lines.append("")
    
    # Listar subcarpetas como secciones
    subdirs = sorted([d for d in folder.iterdir() if d.is_dir() and not d.name.startswith('.')],
                     key=lambda d: d.name.lower())
    if subdirs:
        lines.append("## 📁 Secciones")
        lines.append("")
        for subdir in subdirs:
            # Enlazar al index.md (o index2.md si no existe)
            index_candidate = subdir / "index.md"
            if not index_candidate.exists():
                index_candidate = subdir / "index2.md"
            if index_candidate.exists():
                link = f"[{get_title_from_path(subdir)}]({subdir.name}/index.md)"
            else:
                link = f"{get_title_from_path(subdir)} (sin índice)"
            # Obtener descripción del index si existe
            desc = ""
            if index_candidate.exists():
                meta = get_frontmatter_data(index_candidate)
                desc = meta.get("description", "")
            if desc:
                lines.append(f"- {link}  ")
                lines.append(f"  _{desc}_")
            else:
                lines.append(f"- {link}")
        lines.append("")
    
    # Listar archivos .md (excluyendo índices)
    md_files = sorted([f for f in folder.iterdir() if f.is_file() and f.suffix == '.md' 
                      and f.name not in ['index.md', 'index2.md']],
                      key=lambda f: f.name.lower())
    if md_files:
        lines.append("## 📄 Artículos")
        lines.append("")
        for md_file in md_files:
            title = get_file_title(md_file)
            desc = get_file_description(md_file)
            # Enlace relativo dentro de la misma carpeta
            link = f"[{title}]({md_file.name})"
            if desc:
                lines.append(f"- {link}  ")
                lines.append(f"  _{desc}_")
            else:
                lines.append(f"- {link}")
        lines.append("")
    
    # Si no hay contenido, mensaje amistoso
    if not subdirs and not md_files:
        lines.append("> 📭 Esta sección está vacía actualmente.")
        lines.append("")
    
    # Pie de página con fecha de generación
    lines.append("---")
    lines.append(f"*Índice generado automáticamente el {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    
    return "\n".join(lines)

# -----------------------------------------------------------------------------
# Lógica principal de recorrido
# -----------------------------------------------------------------------------

def process_directory(dir_path: Path, docs_dir: Path, exclude_dirs: List[str]):
    """Recorre recursivamente y genera index2.md en cada carpeta no excluida."""
    # Determinar si es la raíz
    is_root = (dir_path == docs_dir)
    
    # Comprobar si esta carpeta está excluida (por nombre)
    if dir_path.name in exclude_dirs:
        print(f"🚫 Excluyendo carpeta: {dir_path.relative_to(docs_dir)}")
        return
    
    # Generar contenido del índice
    content = generate_index_content(dir_path, docs_dir, is_root)
    
    # Escribir en index2.md
    output_file = dir_path / "index2.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generado: {output_file.relative_to(docs_dir.parent)}")
    
    # Procesar subcarpetas recursivamente
    for subdir in sorted([d for d in dir_path.iterdir() if d.is_dir() and not d.name.startswith('.')],
                         key=lambda d: d.name):
        process_directory(subdir, docs_dir, exclude_dirs)

def main():
    parser = argparse.ArgumentParser(description="Generar índices automáticos para MkDocs")
    parser.add_argument("--docs-dir", default="docs", help="Directorio de documentación (por defecto: docs)")
    parser.add_argument("--exclude", default="", help="Carpetas adicionales a excluir (separadas por coma)")
    args = parser.parse_args()
    
    docs_dir = Path(args.docs_dir).resolve()
    if not docs_dir.exists() or not docs_dir.is_dir():
        print(f"❌ El directorio {docs_dir} no existe.")
        return
    
    # Construir lista de exclusión
    exclude_dirs = DEFAULT_EXCLUDED_DIRS.copy()
    if args.exclude:
        extra = [d.strip() for d in args.exclude.split(",") if d.strip()]
        exclude_dirs.extend(extra)
    # Eliminar duplicados
    exclude_dirs = list(set(exclude_dirs))
    
    print(f"📂 Procesando documentación en: {docs_dir}")
    print(f"🚫 Carpetas excluidas: {exclude_dirs}")
    print("-" * 60)
    
    # Procesar desde la raíz
    process_directory(docs_dir, docs_dir, exclude_dirs)
    
    print("-" * 60)
    print("✨ Generación de índices completada. Revisa los archivos index2.md generados.")

if __name__ == "__main__":
    main()
