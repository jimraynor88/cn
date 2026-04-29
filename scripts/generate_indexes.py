#!/usr/bin/env python3
"""Genera índices visuales (tarjetas) para cada subcarpeta de AstroMitos."""

import os
import re
from pathlib import Path

# Configuración
BASE = Path("docs/AstroMitos")
IGNORE = {"index.md", "catalog-astromitos.md"}  # no generar índice sobre el índice principal

def slug_to_title(slug: str) -> str:
    """Convierte 'eros-psique' en 'Eros y Psique'."""
    # Reemplazar guiones por espacios y capitalizar
    words = slug.replace('.html', '').split('-')
    return ' '.join(w.capitalize() for w in words)

def extract_icon_from_md(filepath: Path) -> str:
    """Intenta leer el frontmatter para sacar un icono (ej. 'ico: 💘')."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Buscar 'icon: ' en las primeras 20 líneas
        match = re.search(r'ico:\s*([^\n]+)', content[:2000])
        if match:
            return match.group(1).strip()
    except:
        pass
    return "📄"  # icono por defecto

def generate_index_for_folder(folder_path: Path):
    """Crea o sobreescribe index.md dentro de folder_path con tarjetas."""
    # Buscar todos los archivos .md (excepto index.md y los IGNORE)
    files = [f for f in folder_path.glob("*.md")
             if f.name not in IGNORE and f.name != "index.html"]
    if not files:
        return

    # Orden alfabético por nombre de archivo
    files.sort(key=lambda f: f.name)

    # Generar contenido
    category_title = folder_path.name.replace('-', ' ').title()
    frontmatter = f"""---
title: {category_title}
---
"""
    # Cabecera visual
    content = frontmatter + f"""

# 🌌 {category_title}

<div class="astromitos-grid">
"""
    for f in files:
        title = slug_to_title(f.name)
        icon = extract_icon_from_md(f)
        # Enlace relativo al archivo (estamos en la misma carpeta)
        link = f.name
        content += f"""
    <div class="astro-card">
        <a href="{link}" style="text-decoration: none; color: inherit;">
            <div class="card-icon">{icon}</div>
            <h3>{title}</h3>
            <p>Explora el mito y su significado astrológico</p>
        </a>
    </div>
"""
    content += """
</div>

<style>
/* Estas clases ya existen en tu extra.css global, pero las repetimos por si acaso */
.astromitos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}
.astro-card {
    background: var(--md-code-bg-color, #1e293b);
    border-radius: 28px;
    padding: 1.2rem;
    border: 1px solid var(--md-accent-fg-color, #F472B6);
    transition: transform 0.2s, box-shadow 0.2s;
    text-align: center;
}
.astro-card:hover {
    transform: translateY(-5px);
    border-color: var(--md-primary-fg-color, #60A5FA);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.card-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}
.astro-card h3 {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    font-size: 1.3rem;
}
.astro-card p {
    font-size: 0.9rem;
    opacity: 0.8;
}
</style>
"""  # Nota: estas clases ya están en tu extra.css, pero las incluimos para que el generador sea autocontenido.

    # Escribir el archivo
    index_path = folder_path / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Generado {index_path}")

# Recorrer todas las subcarpetas de primer nivel dentro de AstroMitos
if not BASE.exists():
    print(f"❌ La carpeta {BASE} no existe. Asegúrate de haber creado las subcarpetas.")
    exit(1)

for folder in BASE.iterdir():
    if folder.is_dir():
        generate_index_for_folder(folder)
