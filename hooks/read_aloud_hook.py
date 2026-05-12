# hooks/read_aloud_hook.py
import re

def on_page_content(html, page, config, files):
    """Inserta el contenedor del reproductor de audio si page.meta.read es True."""
    if page.meta.get("read", False):
        player_div = '<div id="read-aloud-root"></div>'
        match = re.search(r'</h1>', html)
        if match:
            pos = match.end()
            html = html[:pos] + '\n' + player_div + html[pos:]
        else:
            html = player_div + '\n' + html
    return html
