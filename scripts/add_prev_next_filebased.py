import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path

def main():
    site_dir = sys.argv[1] if len(sys.argv) > 1 else "site"
    site_path = Path(site_dir)

    # Recorremos todas las carpetas que contengan archivos HTML
    for root, dirs, files in os.walk(site_path):
        # Solo nos interesan archivos .html que no sean index.html (páginas de contenido)
        html_files = [f for f in files if f.endswith('.html') and f != 'index.html']
        if not html_files:
            continue

        # Orden alfabético
        html_files.sort()

        for idx, filename in enumerate(html_files):
            filepath = Path(root) / filename
            prev_file = html_files[idx-1] if idx > 0 else None
            next_file = html_files[idx+1] if idx < len(html_files)-1 else None

            # Leer el HTML
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Buscar el contenedor del contenido principal (más robusto)
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
            if prev_file:
                nav_html += f'<a href="{prev_file}" class="prev">&larr; Anterior</a>'
            else:
                nav_html += '<span></span>'
            if next_file:
                nav_html += f'<a href="{next_file}" class="next">Siguiente &rarr;</a>'
            nav_html += '</div>'

            # Insertar al final del contenido
            content.append(BeautifulSoup(nav_html, 'html.parser'))

            # Guardar
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            print(f"Actualizado: {filepath}")

if __name__ == '__main__':
    main()
