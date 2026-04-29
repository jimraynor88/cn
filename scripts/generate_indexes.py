#!/usr/bin/env python3
"""Genera índices visuales (tarjetas) para cada subcarpeta de AstroMitos.
   Ahora genera index.html (no index.md) con enlaces a carpetas (formato limpio)
   y corrige la extracción de emojis sin comillas.
"""

import os
import re
from pathlib import Path

# Configuración
BASE = Path("docs/AstroMitos")
IGNORE = {"index.md", "catalog-astromitos.md", "index.html"}

def slug_to_title(slug: str) -> str:
    """Convierte 'eros-psique.md' en 'Eros Psique'."""
    name = slug.replace('.md', '').replace('.html', '')
    words = name.split('-')
    return ' '.join(w.capitalize() for w in words)

def extract_emoji_from_md(filepath: Path) -> str:
    """Lee el campo 'ico:' del frontmatter y devuelve el emoji limpio (sin comillas)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Buscar 'ico:' seguido de cualquier carácter hasta fin de línea (primeras 20 líneas)
        match = re.search(r'^ico:\s*(.+)$', content[:2000], re.MULTILINE)
        if match:
            raw = match.group(1).strip()
            # Eliminar comillas dobles o simples alrededor
            if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
                raw = raw[1:-1]
            return raw
    except Exception:
        pass
    return "📄"  # icono por defecto

def generate_index_for_folder(folder_path: Path):
    """Crea o sobreescribe index.html dentro de folder_path con tarjetas."""
    # Buscar todos los archivos .md (excluyendo index.* y los ignorados)
    files = [f for f in folder_path.glob("*.md")
             if f.name not in IGNORE]
    if not files:
        return

    files.sort(key=lambda f: f.name)

    category_title = folder_path.name.replace('-', ' ').title()
    # Añadimos meta charset para que los emojis se muestren bien
    content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{category_title} · AstroMitos</title>
</head>
<body>
<div class="md-typeset">

# 🌌 {category_title}

<div class="astromitos-grid">
"""
    for f in files:
        title = slug_to_title(f.name)
        emoji = extract_emoji_from_md(f)
        # Enlace a la carpeta (sin extensión .md) - asumiendo que cada .md genera su propia carpeta
        link = f.stem + "/"   # por ejemplo, "adonis/"
        content += f"""
    <div class="astro-card">
        <a href="{link}" style="text-decoration: none; color: inherit;">
            <div class="card-icon">{emoji}</div>
            <h3>{title}</h3>
            <p>Explora el mito y su significado astrológico</p>
        </a>
    </div>
"""
    content += """
</div>

</div>
</body>
</html>
"""
    # Añadir el CSS global (opcional, pero si no se carga extra.css lo ponemos)
    content += """
<style>
/* Estilos de respaldo (normalmente los proporciona extra.css) */
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
"""

    index_path = folder_path / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Generado {index_path}")

if not BASE.exists():
    print(f"❌ La carpeta {BASE} no existe. Crea las subcarpetas primero.")
    exit(1)

for folder in BASE.iterdir():
    if folder.is_dir():
        generate_index_for_folder(folder)
