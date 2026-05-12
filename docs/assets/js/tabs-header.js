// docs/assets/js/tabs-header.js

(function() {
  // Ocultar pestañas originales de inmediato
  const style = document.createElement('style');
  style.textContent = `.md-tabs[data-md-component="tabs"]:not(.tabs-moved) { display: none !important; }`;
  document.head.appendChild(style);

  function removeExistingClones() {
    document.querySelectorAll('.md-tabs.tabs-moved').forEach(el => el.remove());
  }

  function moveTabsToHeader() {
    const headerInner = document.querySelector('.md-header__inner');
    if (!headerInner) return;

    const originalTabs = document.querySelector('.md-tabs[data-md-component="tabs"]');
    if (!originalTabs) return;

    // Si ya está dentro del header, no hacemos nada
    if (originalTabs.parentElement === headerInner) return;

    removeExistingClones();

    const clonedTabs = originalTabs.cloneNode(true);
    clonedTabs.classList.add('tabs-moved');
    clonedTabs.setAttribute('data-cloned', 'true');
    originalTabs.style.display = 'none';

    const source = headerInner.querySelector('.md-header__source');
    if (source) {
      headerInner.insertBefore(clonedTabs, source);
    } else {
      headerInner.appendChild(clonedTabs);
    }

    // Evento personalizado por si lo necesitas
    document.dispatchEvent(new CustomEvent('tabs-moved', { detail: { clone: clonedTabs } }));
  }

  // Carga inicial
  document.addEventListener('DOMContentLoaded', moveTabsToHeader);

  // Refuerzo tras navegación instantánea
  document.addEventListener('page$', function() {
    setTimeout(moveTabsToHeader, 100);
  });

  // MutationObserver: detecta si las tabs originales vuelven a aparecer y las mueve
  const observer = new MutationObserver(function(mutations) {
    for (let mutation of mutations) {
      if (mutation.addedNodes.length) {
        for (let node of mutation.addedNodes) {
          if (node.nodeType === 1 && node.matches && node.matches('.md-tabs[data-md-component="tabs"]')) {
            setTimeout(moveTabsToHeader, 50);
            return;
          }
        }
      }
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });
})();
