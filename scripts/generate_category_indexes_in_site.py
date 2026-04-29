import os
from pathlib import Path

SITE_BASE = Path("site/AstroMitos")

for folder in SITE_BASE.iterdir():
    if not folder.is_dir():
        continue
    # Buscar todas las subcarpetas que contienen fichas (cada ficha es una carpeta)
    fichas = [item for item in folder.iterdir() if item.is_dir()]
    if not fichas:
        continue
    # Generar contenido HTML similar al que ya tenías
    category_title = folder.name.replace('-', ' ').title()
    html_content = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{category_title} · AstroMitos</title></head>
<body>
<div class="md-typeset">
<h1>🌌 {category_title}</h1>
<div class="astromitos-grid">
"""
    for ficha_folder in sorted(fichas):
        # Leer el frontmatter del .md original para obtener el emoji (necesitas acceder a la fuente, no al sitio)
        # Opción rápida: usar un mapa previamente generado, o un nombre por defecto.
        name = ficha_folder.name.replace('-', ' ').title()
        html_content += f"""
    <div class="astro-card">
        <a href="{ficha_folder.name}/">
            <div class="card-icon">📄</div>
            <h3>{name}</h3>
            <p>Explora el mito</p>
        </a>
    </div>
"""
    html_content += """
</div>
</div>
</body>
</html>
"""
    with open(folder / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Generado {folder}/index.html")
