#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from bs4 import BeautifulSoup

def main():
    site_dir = sys.argv[1] if len(sys.argv) > 1 else "site"
    site_path = Path(site_dir)

    # Ruta de la sección AstroMitos
    astro_path = site_path / "AstroMitos"
    if not astro_path.exists():
        print("No se encontró la carpeta AstroMitos")
        return

    # Recorrer cada categoría (subcarpeta de AstroMitos)
    for category_dir in astro_path.iterdir():
        if not category_dir.is_dir():
            continue
        # Obtener todas las subcarpetas dentro de la categoría (cada una es una ficha)
        fichas = [f for f in category_dir.iterdir() if f.is_dir() and (f / "index.html").exists()]
        if len(fichas) < 2:
            continue  # No hay suficientes fichas para enlazar

        # Ordenar alfabéticamente por nombre de carpeta
        fichas.sort(key=lambda f: f.name)

        for idx, ficha_dir in enumerate(fichas):
            index_file = ficha_dir / "index.html"
            prev_dir = fichas[idx-1] if idx > 0 else None
            next_dir = fichas[idx+1] if idx < len(fichas)-1 else None

            # Leer el HTML
            with open(index_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Buscar el contenedor del contenido principal
            content = (
                soup.find('div', class_='md-content') or
                soup.find('main') or
                soup.find('article') or
                soup.body
            )
            if not content:
                continue

            # Construir enlaces relativos
            nav_html = '<div class="prev-next-nav" style="display: flex; justify-content: space-between; margin-top: 2rem;">'
            if prev_dir:
                # Enlace relativo desde la carpeta actual a la carpeta anterior (subir un nivel)
                rel_prev = f"../{prev_dir.name}/"
                nav_html += f'<a href="{rel_prev}" class="prev">&larr; Anterior</a>'
            else:
                nav_html += '<span></span>'
            if next_dir:
                rel_next = f"../{next_dir.name}/"
                nav_html += f'<a href="{rel_next}" class="next">Siguiente &rarr;</a>'
            nav_html += '</div>'

            # Insertar al final del contenido
            content.append(BeautifulSoup(nav_html, 'html.parser'))

            # Guardar
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Actualizado: {index_file}")

if __name__ == '__main__':
    main()
