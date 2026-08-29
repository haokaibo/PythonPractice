// Frontend logic for the Python Practice browser.
// - Debounced live prefix search.
// - Tabs: favorites vs. all files.
// - Category dropdown + tag chip multi-filter (AND semantics).
// - Result list grouped by category (collapsible).
// - Keyboard nav: / focus, Esc clear, Up/Down move, Enter open, Ctrl+Click also opens.
// - Lazy-loads Prism.js + line-numbers the first time a file is opened.

(() => {
  const $q        = document.getElementById('q');
  const $list     = document.getElementById('list');
  const $code     = document.getElementById('code');
  const $count    = document.getElementById('count');
  const $tabs     = document.querySelectorAll('.tab');
  const $category = document.getElementById('category');
  const $tagBar   = document.getElementById('tag-bar');
  const $clearBtn = document.getElementById('clear-tags');

  let currentTab = 'all';
  let activeTags = new Set();   // selected tag chips (AND)
  let visibleItems = [];        // flat list of currently rendered items
  let cursor = -1;              // keyboard cursor in visibleItems
  let favSet = new Set();       // paths currently favorited (mirror of server)

  // ---------- helpers ----------

  const debounce = (fn, ms) => {
    let t;
    return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
  };

  const escapeHtml = (s) => s.replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  /**
   * Highlight every character of `q` (in order) inside `text`.
   * Returns escaped HTML with <mark> spans around each matched char.
   * Used for fuzzy-match results where the matched chars are scattered.
   */
  const highlightFuzzy = (text, q) => {
    if (!q) return escapeHtml(text);
    const lower = text.toLowerCase();
    const ql = q.toLowerCase();
    let i = 0;                  // cursor in `text`
    let k = 0;                  // cursor in `q`
    let out = '';
    while (i < text.length && k < ql.length) {
      if (lower[i] === ql[k]) {
        out += '<mark>' + escapeHtml(text[i]) + '</mark>';
        k += 1;
      } else {
        out += escapeHtml(text[i]);
      }
      i += 1;
    }
    out += escapeHtml(text.slice(i));
    return out;
  };

  const fetchJSON = async (url) => {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`${r.status} ${r.statusText}`);
    return r.json();
  };

  const buildQS = () => {
    const params = new URLSearchParams();
    const q = $q.value.trim();
    if (q) params.set('q', q);
    if ($category.value) params.set('category', $category.value);
    if (activeTags.size) params.set('tags', [...activeTags].join(','));
    return params.toString();
  };

  // ---------- data fetch ----------

  async function refresh() {
    const endpoint = currentTab === 'favorites' ? '/api/favorites' : '/api/all';
    const qs = buildQS();
    const items = await fetchJSON(`${endpoint}${qs ? '?' + qs : ''}`);
    // Mirror server truth for the favorite set.
    favSet = new Set(items.filter(it => it.favorited).map(it => it.path));
    visibleItems = items;
    cursor = -1;
    render(items, $q.value.trim());
  }

  async function toggleFavorite(path, title) {
    const wasFav = favSet.has(path);
    // Optimistic update for snappy UI; rollback on server error.
    if (wasFav) favSet.delete(path); else favSet.add(path);
    updateStars();

    try {
      const r = await fetch('/api/favorites/toggle', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path, title, tags: [], note: '' }),
      });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const data = await r.json();
      if (data.favorited) favSet.add(path); else favSet.delete(path);
      updateStars();
      // Refresh the filter catalog so the favorites count stays in sync.
      loadFilterCatalog();
      // On the favorites tab, an add/remove changes the visible list.
      if (currentTab === 'favorites') refresh();
    } catch (e) {
      // Rollback on error.
      if (wasFav) favSet.add(path); else favSet.delete(path);
      updateStars();
      alert(`Failed to update favorite: ${e.message}`);
    }
  }

  function updateStars() {
    document.querySelectorAll('.list li[data-path]').forEach(li => {
      const btn = li.querySelector('.star');
      if (!btn) return;
      const isFav = favSet.has(li.dataset.path);
      btn.classList.toggle('fav', isFav);
      btn.textContent = isFav ? '★' : '☆';
      btn.title = isFav ? 'Remove from favorites' : 'Add to favorites';
    });
  }

  async function loadFilterCatalog() {
    // categories
    const cats = await fetchJSON(`/api/categories?scope=${currentTab}`);
    const prev = $category.value;
    $category.innerHTML = '<option value="">All</option>'
      + Object.entries(cats).map(([name, n]) =>
          `<option value="${escapeHtml(name)}">${escapeHtml(name)} (${n})</option>`
        ).join('');
    if ([...$category.options].some(o => o.value === prev)) $category.value = prev;

    // tags
    const tagMap = await fetchJSON('/api/tags');
    const tags = tagMap[currentTab] || {};
    const entries = Object.entries(tags);
    if (!entries.length) {
      $tagBar.innerHTML =
        `<span class="chip" style="cursor:default;opacity:.6">no tags</span>`;
      return;
    }
    $tagBar.innerHTML = entries.map(([t, n]) =>
      `<button type="button" class="chip ${activeTags.has(t) ? 'active' : ''}" data-tag="${escapeHtml(t)}">
         #${escapeHtml(t)}<span class="count">${n}</span>
       </button>`
    ).join('');
    $tagBar.querySelectorAll('.chip[data-tag]').forEach(btn => {
      btn.addEventListener('click', () => {
        const t = btn.dataset.tag;
        if (activeTags.has(t)) activeTags.delete(t); else activeTags.add(t);
        refresh();
      });
    });
  }

  // ---------- render ----------

  function render(items, q) {
    $list.innerHTML = '';
    if (!items.length) {
      const li = document.createElement('li');
      li.className = 'empty';
      li.textContent = 'No matches';
      $list.appendChild(li);
      $count.textContent =
        `0 matches in ${currentTab === 'favorites' ? '★ Favorites' : 'All files'}`;
      return;
    }

    // group by category, preserving the order categories first appear
    const groups = new Map();
    for (const it of items) {
      const c = it.category || 'other';
      if (!groups.has(c)) groups.set(c, []);
      groups.get(c).push(it);
    }

    let runningIdx = 0;
    for (const [cat, list] of groups) {
      const det = document.createElement('details');
      det.open = true;
      const sum = document.createElement('summary');
      sum.className = 'group';
      sum.innerHTML =
        `<span class="arrow">▾</span> ${escapeHtml(cat)}` +
        `<span class="group-count">${list.length}</span>`;
      det.appendChild(sum);
      list.forEach(it => {
        const idx = runningIdx++;
        const li = document.createElement('li');
        li.dataset.path = it.path;
        li.dataset.idx  = String(idx);

        const titleEl = document.createElement('div');
        titleEl.className = 'title';
        titleEl.innerHTML = highlightFuzzy(it.title || it.path, q);
        li.appendChild(titleEl);

        const pathEl = document.createElement('div');
        pathEl.className = 'path';
        pathEl.textContent = it.path;
        li.appendChild(pathEl);

        const star = document.createElement('button');
        star.type = 'button';
        star.className = 'star';
        star.textContent = it.favorited ? '★' : '☆';
        star.title = it.favorited ? 'Remove from favorites' : 'Add to favorites';
        star.setAttribute('aria-label', 'toggle favorite');
        star.addEventListener('click', (e) => {
          e.stopPropagation();
          toggleFavorite(it.path, it.title);
        });
        li.appendChild(star);

        li.addEventListener('click', () => {
          cursor = idx;
          updateCursor();
          openFile(it.path, idx);
        });
        det.appendChild(li);
      });
      $list.appendChild(det);
    }

    $count.textContent =
      `${items.length} match${items.length === 1 ? '' : 'es'}` +
      ` in ${currentTab === 'favorites' ? '★ Favorites' : 'All files'}` +
      (activeTags.size ? ` · ${activeTags.size} tag${activeTags.size === 1 ? '' : 's'}` : '') +
      ($category.value ? ` · ${$category.value}` : '');
  }

  function updateCursor() {
    document.querySelectorAll('.list li').forEach(li => {
      li.classList.toggle('active', Number(li.dataset.idx) === cursor);
    });
    const el = document.querySelector(`.list li[data-idx="${cursor}"]`);
    if (el) el.scrollIntoView({ block: 'nearest' });
  }

  // ---------- viewer ----------

  async function openFile(path, idx) {
    let text;
    try {
      const r = await fetch(`/api/file?path=${encodeURIComponent(path)}`);
      if (!r.ok) throw new Error(`HTTP ${r.status} ${r.statusText}`);
      text = await r.text();
    } catch (e) {
      $code.textContent = `# Failed to load: ${e.message}`;
      $code.className = '';
      return;
    }

    await window.__loadPrism();

    // Set the new content first, then ask Prism to highlight.
    $code.textContent = text;
    $code.className = 'language-python';

    // Highlight the inner <code>. If line-numbers throws (it does on some
    // browser/font combinations when white-space is computed before layout
    // settles), we still want to see the raw text rather than nothing.
    let highlighted = false;
    try {
      window.Prism.highlightElement($code);
      highlighted = true;
    } catch (e) {
      console.warn('Prism.highlightElement failed:', e);
    }

    // The line-numbers plugin reads getComputedStyle(pre).whiteSpace without
    // null-checking, and the value can be null during the same frame the
    // textContent was just set. We MUST avoid calling ln.resize() ourselves.
    // Instead, the plugin already runs its own complete hook on highlight,
    // so it will build the gutter. We just mirror line-height onto the
    // gutter rows after a frame settles, and re-run if the plugin missed it.
    const ln = window.Prism.plugins.lineNumbers;
    requestAnimationFrame(() => {
      try {
        const pre = $code.parentElement;
        if (!pre) return;
        const rows = pre.querySelector('.line-numbers-rows');
        const cs = getComputedStyle($code);
        let codeLineHeight = cs.lineHeight;
        if (!codeLineHeight || codeLineHeight === 'normal') {
          codeLineHeight = getComputedStyle(pre)
                            .getPropertyValue('--row-h').trim() || '14px';
        }
        if (rows) {
          rows.style.lineHeight = codeLineHeight;
          rows.querySelectorAll('span').forEach(s => {
            s.style.lineHeight = codeLineHeight;
          });
          // The plugin positions each row with top = (i * lineHeight).
          // Force the computed value to match ours.
          const n = code.textContent.split('\n').length;
          for (let i = 0; i < rows.children.length; i++) {
            rows.children[i].style.lineHeight = codeLineHeight;
          }
        } else {
          // Plugin never built the gutter (e.g. highlight threw). Build it
          // ourselves so the user at least sees numbers.
          const n = code.textContent.split('\n').length;
          const gutter = document.createElement('span');
          gutter.setAttribute('aria-hidden', 'true');
          gutter.className = 'line-numbers-rows';
          for (let i = 0; i < n; i++) {
            const span = document.createElement('span');
            span.textContent = i + 1;
            gutter.appendChild(span);
          }
          pre.appendChild(gutter);
        }
      } catch (e) {
        console.warn('line-numbers gutter sync failed:', e);
      }
    });
  }

  // ---------- keyboard nav ----------

  document.addEventListener('keydown', (e) => {
    // '/' focuses search (unless already typing in an input)
    if (e.key === '/' && document.activeElement !== $q) {
      e.preventDefault();
      $q.focus();
      $q.select();
      return;
    }
    if (document.activeElement === $q) {
      if (e.key === 'Escape') { $q.value = ''; refresh(); }
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (visibleItems.length) { cursor = 0; updateCursor(); }
      }
      return;
    }
    if (!visibleItems.length) return;
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      cursor = Math.min(visibleItems.length - 1, cursor + 1);
      updateCursor();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      cursor = Math.max(0, cursor - 1);
      updateCursor();
    } else if (e.key === 'Enter' && cursor >= 0) {
      e.preventDefault();
      const it = visibleItems[cursor];
      openFile(it.path, cursor);
    } else if (e.key === 'Escape') {
      cursor = -1; updateCursor();
    }
  });

  // ---------- events ----------

  $q.addEventListener('input', debounce(refresh, 120));
  $category.addEventListener('change', refresh);
  $clearBtn.addEventListener('click', () => {
    if (!activeTags.size) return;
    activeTags.clear();
    refresh();
  });

  $tabs.forEach(btn => btn.addEventListener('click', () => {
    $tabs.forEach(b => b.classList.toggle('active', b === btn));
    currentTab = btn.dataset.tab;
    activeTags.clear();
    cursor = -1;
    // Reload the chip bar since tags differ per tab, then refresh list.
    loadFilterCatalog().then(refresh);
  }));

  // initial load
  loadFilterCatalog().then(refresh);
})();
