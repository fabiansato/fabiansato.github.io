document.documentElement.classList.add('js');
'use strict';
const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
if (menuButton && nav) {
  const close = () => { menuButton.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); menuButton.firstChild.textContent = menuButton.dataset.open + ' '; };
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.firstChild.textContent = (open ? menuButton.dataset.close : menuButton.dataset.open) + ' ';
    nav.classList.toggle('is-open', open);
  });
  nav.addEventListener('click', event => { if (event.target.closest('a')) close(); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && nav.classList.contains('is-open')) { close(); menuButton.focus(); } });
  window.matchMedia('(min-width: 761px)').addEventListener('change', close);
}
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
document.querySelectorAll('[data-filter-root]').forEach(root => {
  const buttons = [...root.querySelectorAll('[data-filter]')];
  const input = root.querySelector('[data-search-input]');
  const items = [...root.querySelectorAll('[data-filter-item]')];
  const status = root.querySelector('[data-filter-status]');
  let selected = root.dataset.initialFilter || 'all';
  buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === selected)));
  const apply = () => {
    const query = normalize(input.value.trim()); let count = 0;
    items.forEach(item => {
      const show = (selected === 'all' || selected === item.dataset.group) && normalize(item.dataset.search).includes(query);
      item.hidden = !show; if (show) count++;
    });
    status.textContent = `${count} ${count === 1 ? status.dataset.singular : status.dataset.label}`;
    root.querySelector('[data-no-results]').hidden = count !== 0;
  };
  buttons.forEach(button => button.addEventListener('click', () => {
    selected = button.dataset.filter;
    buttons.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    apply();
  }));
  input.addEventListener('input', apply);
  root.querySelector('[data-filter-controls]').hidden = false;
  apply();
});
document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
  const status = document.querySelector('.copy-status');
  try { await navigator.clipboard.writeText(window.location.href); button.textContent = button.dataset.success; status.textContent = button.dataset.success; }
  catch { status.classList.remove('sr-only'); status.textContent = button.dataset.error; }
}));
