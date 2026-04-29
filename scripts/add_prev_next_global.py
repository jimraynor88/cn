#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from pathlib import Path

def main():
    if len(sys.argv) > 1:
        site_dir = sys.argv[1]
    else:
        site_dir = "site"

    sitemap_path = os.path.join(site_dir, "sitemap.xml")
    if not os.path.isfile(sitemap_path):
        print("Error: sitemap.xml not found. Build might not have generated it.")
        sys.exit(1)

    # Parsear sitemap
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [elem.text for elem in root.findall('.//ns:loc', ns)]

    # Convertir cada URL a ruta de archivo HTML en disco
    page_paths = []
    for url in urls:
        # Quitar dominio
        path = url.replace("https://CartaNatal.de", "").replace("http://localhost:8000", "").lstrip("/")
        if not path:
            continue
        # Construir ruta al archivo HTML
        if path.endswith("/"):
            # Es una carpeta, el archivo es index.html dentro
            file_path = os.path.join(site_dir, path, "index.html")
        else:
            # Es un archivo HTML
            file_path = os.path.join(site_dir, path)
            if not file_path.endswith(".html"):
                file_path += ".html"
        if os.path.isfile(file_path):
            page_paths.append(file_path)
        else:
            print(f"Warning: {file_path} not found for URL {url}")

    # Generar enlaces para cada página
    for idx, full_path in enumerate(page_paths):
        prev_path = page_paths[idx-1] if idx > 0 else None
        next_path = page_paths[idx+1] if idx < len(page_paths)-1 else None

        # Leer el HTML
        with open(full_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Buscar el contenedor principal del contenido
        content = (
            soup.find('div', class_='md-content') or
            soup.find('main', class_='md-main') or
            soup.find('div', role='main') or
            soup.find('article') or
            soup.body
        )
        if not content:
            print(f"No se encontró contenedor principal en {full_path}")
            continue

        # Construir enlaces con rutas relativas
        base_dir = os.path.dirname(full_path)
        nav_html = '<div class="prev-next-nav" style="display: flex; justify-content: space-between; margin-top: 2rem;">'
        if prev_path:
            rel_prev = os.path.relpath(prev_path, base_dir)
            nav_html += f'<a href="{rel_prev}" class="prev">&larr; Anterior</a>'
        else:
            nav_html += '<span></span>'
        if next_path:
            rel_next = os.path.relpath(next_path, base_dir)
            nav_html += f'<a href="{rel_next}" class="next">Siguiente &rarr;</a>'
        nav_html += '</div>'

        # Insertar al final del contenido
        content.append(BeautifulSoup(nav_html, 'html.parser'))

        # Guardar
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        print(f"Actualizado: {full_path}")

if __name__ == '__main__':
    main()
