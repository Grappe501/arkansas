/**
 * Citizens Facts — Depth toggle v1.1.0
 * Four levels: L1 (1 min) → L4 (research file)
 */

function initDepthPanels() {
  document.querySelectorAll('[data-depth-panel]').forEach((panel) => {
    const buttons = panel.querySelectorAll('[data-depth-btn]');
    const layers = panel.querySelectorAll('[data-depth-layer]');

    buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        const target = btn.dataset.depthBtn;

        buttons.forEach((b) => {
          b.classList.toggle('depth-toggle__btn--active', b === btn);
          b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
        });

        layers.forEach((layer) => {
          const show = layer.dataset.depthLayer === target;
          layer.hidden = !show;
          layer.classList.toggle('depth-layer--active', show);
        });
      });
    });
  });
}

function renderDepthToggle(activeLevel) {
  const levels = [
    { id: 'L1', label: '1 min' },
    { id: 'L2', label: '5 min' },
    { id: 'L3', label: '20 min' },
    { id: 'L4', label: 'Research' }
  ];

  return `
    <div class="depth-toggle" role="tablist" aria-label="Choose reading depth">
      ${levels
        .map(
          (l) => `
        <button type="button" class="depth-toggle__btn${l.id === activeLevel ? ' depth-toggle__btn--active' : ''}"
          data-depth-btn="${l.id}" role="tab" aria-selected="${l.id === activeLevel}">
          ${l.label}
        </button>`
        )
        .join('')}
    </div>`;
}

document.addEventListener('DOMContentLoaded', initDepthPanels);
