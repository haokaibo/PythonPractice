// Static-build frontend for the Python Practice browser.
// Counterpart to web/static/app.js — same UI/keyboard behavior, but reads
// pre-generated JSON (api/all.json, api/favorites.json, api/tags.json) and
// raw files under ./src/... instead of calling a live FastAPI backend.
//
// IMPORTANT: this file is not used by `uvicorn web.app:app --reload`.
// It only ships in the static build produced by scripts/build_static.py,
// which copies it in as static/app.js. Keep UI logic here in sync with
// web/static/app.js by hand if you change one.
//
// Favorites: a static host can't write back to favorites.json, so ☆/★
// toggling here only updates the browser's localStorage. It's a per-browser
// overlay on top of the favorites.json snapshot baked in at build time —
// nothing is shared or persisted back to the repo.

(() => {
  const $q        = document.getElementById('q');
  const $list     = document.getElementById('list');
  const $code     = document.getElementById('code');
  const $count    = document.getElementById('count');
  const $tabs     = document.querySelectorAll('.tab');
  const $category = document.getElementById('category');
  const $tagBar   = document.getElementById('tag-bar');
  const $clearBtn = document.getElementById('clear-tags');
  const $brand    = document.querySelector('.brand');

  if ($brand) $brand.textContent = 'Python Practice (static demo)';

  let currentTab = 'all';
  let activeTags = new Set();
  let visibleItems = [];
  let cursor = -1;

  // Raw data loaded once from the pre-built JSON files.
  let ALL_ITEMS = [];        // every .py file under src/
  let BASE_FAVORITES = [];   // favorites.json snapshot at build time
  let TAGS = { all: {}, favorites: {} };

  const OVERRIDES_KEY = 'pp_fav_overrides_v1';
  let overrides = loadOverrides();  // { [path]: { action: 'add'|'remove', item? } }

  // ---------- helpers (unchanged from app.js) ----------

  const debounce = (fn, ms) => {
    let t;
    return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
  };

  const escapeHtml = (s) => s.replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  const highlightFuzzy = (text, q) => {
    if (!q) return escapeHtml(text);
    const lower = text.toLowerCase();
    const ql = q.toLowerCase();
    let i = 0, k = 0, out = '';
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

  // ---------- localStorage overrides ----------

  function loadOverrides() {
    try { return JSON.parse(localStorage.getItem(OVERRIDES_KEY) || '{}'); }
    catch { return {}; }
  }
  function saveOverrides() {
    try { localStorage.setItem(OVERRIDES_KEY, JSON.stringify(overrides)); }
    catch { /* storage disabled/full — overlay just won't persist */ }
  }

  // Effective favorite set = build-time favorites, with local overrides
  // applied (add/remove). Also returns the merged item list for the
  // Favorites tab (build-time metadata preserved where available).
  function effectiveFavorites() {
    const removed = new Set(
      Object.entries(overrides).filter(([, v]) => v.action === 'remove').map(([k]) => k));
    const addedItems = Object.entries(overrides)
      .filter(([, v]) => v.action === 'add')
      .map(([, v]) => v.item);

    const merged = BASE_FAVORITES.filter(it => !removed.has(it.path)).concat(addedItems);
    // de-dupe just in case an item is both base and re-added
    const seen = new Set();
    return merged.filter(it => (seen.has(it.path) ? false : (seen.add(it.path), true)));
  }

  function isFavorited(path) {
    const ov = overrides[path];
    const base = BASE_FAVORITES.some(it => it.path === path);
    if (!ov) return base;
    return ov.action === 'add';
  }

  function toggleFavorite(path, title) {
    const nowFav = !isFavorited(path);
    if (nowFav) {
      overrides[path] = {
        action: 'add',
        item: { path, title: title || path.split('/').pop(), tags: [], note: '', category: categoryFor(path) },
      };
    } else {
      overrides[path] = { action: 'remove' };
    }
    saveOverrides();
    updateStars();
    if (currentTab === 'favorites') refresh();
    loadFilterCatalog(); // counts in the category dropdown can shift
  }

  function categoryFor(relPath) {
    const parts = relPath.split('/');
    return parts.length >= 2 && parts[0] === 'src' ? parts[1] : '';
  }

  function updateStars() {
    document.querySelectorAll('.list li[data-path]').forEach(li => {
      const btn = li.querySelector('.star');
      if (!btn) return;
      const fav = isFavorited(li.dataset.path);
      btn.classList.toggle('fav', fav);
      btn.textContent = fav ? '★' : '☆';
      btn.title = fav ? 'Remove from favorites (this browser only)' : 'Add to favorites (this browser only)';
    });
  }

  // ---------- client-side port of web/app.py's _filter / _fuzzy_score ----------

  function fuzzyScore(needle, haystack) {
    if (!needle) return 0;
    needle = needle.toLowerCase();
    const hay = haystack.toLowerCase();
    let i = 0, first = -1, last = -1;
    for (const ch of needle) {
      const j = hay.indexOf(ch, i);
      if (j < 0) return Infinity;
      if (first < 0) first = j;
      last = j;
      i = j + 1;
    }
    return last - first;
  }

  function filterItems(items, { q = '', tags = new Set(), category = '' } = {}) {
    const needle = q.trim().toLowerCase();
    const withFav = items.map(it => ({ ...it, favorited: isFavorited(it.path) }));
    let out = [];
    for (const it of withFav) {
      if (category && it.category !== category) continue;
      if (tags.size) {
        const have = new Set(it.tags || []);
        let ok = true;
        for (const t of tags) if (!have.has(t)) { ok = false; break; }
        if (!ok) continue;
      }
      if (needle) {
        const basename = (it.path || '').split('/').pop();
        const score = fuzzyScore(needle, basename);
        if (!isFinite(score)) continue;
        it._score = score;
      }
      out.push(it);
    }
    if (needle) out.sort((a, b) => a._score - b._score);
    return out;
  }

  function categoryCounts(items) {
    const c = new Map();
    for (const it of items) {
      const cat = it.category || '';
      if (!cat) continue;
      c.set(cat, (c.get(cat) || 0) + 1);
    }
    return Object.fromEntries(
      [...c.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])));
  }

  function tagCounts(items) {
    const c = new Map();
    for (const it of items) {
      for (const t of it.tags || []) c.set(t, (c.get(t) || 0) + 1);
    }
    return Object.fromEntries(
      [...c.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])));
  }

  const buildFilters = () => ({
    q: $q.value.trim(),
    tags: activeTags,
    category: $category.value,
  });

  // ---------- data load + refresh (replaces the old server round-trips) ----------

  async function loadData() {
    [ALL_ITEMS, BASE_FAVORITES, TAGS] = await Promise.all([
      fetchJSON('./api/all.json'),
      fetchJSON('./api/favorites.json'),
      fetchJSON('./api/tags.json'),
    ]);
  }

  function currentBaseList() {
    return currentTab === 'favorites' ? effectiveFavorites() : ALL_ITEMS;
  }

  function refresh() {
    const items = filterItems(currentBaseList(), buildFilters());
    visibleItems = items;
    cursor = -1;
    render(items, $q.value.trim());
  }

  function loadFilterCatalog() {
    const base = currentBaseList();
    const cats = categoryCounts(base);
    const prev = $category.value;
    $category.innerHTML = '<option value="">All</option>'
      + Object.entries(cats).map(([name, n]) =>
          `<option value="${escapeHtml(name)}">${escapeHtml(name)} (${n})</option>`
        ).join('');
    if ([...$category.options].some(o => o.value === prev)) $category.value = prev;

    // Tags: use the build-time snapshot for the base scope (matches the
    // original server behavior — tag counts don't shift with a search
    // query), but recompute for the favorites tab since local add/remove
    // can change which items (and tags) are in it.
    const tags = currentTab === 'favorites' ? tagCounts(base) : (TAGS.all || {});
    const entries = Object.entries(tags);
    if (!entries.length) {
      $tagBar.innerHTML = `<span class="chip" style="cursor:default;opacity:.6">no tags</span>`;
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

  // ---------- render (unchanged from app.js) ----------

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
        const fav = isFavorited(it.path);
        star.textContent = fav ? '★' : '☆';
        star.title = fav ? 'Remove from favorites (this browser only)' : 'Add to favorites (this browser only)';
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
  // Files are fetched at their own relative path (the build script copies
  // the whole src/ tree into the output), instead of ./api/file?path=...

  async function openFile(path, idx) {
    let text;
    try {
      const r = await fetch(`./${path}`);
      if (!r.ok) throw new Error(`HTTP ${r.status} ${r.statusText}`);
      text = await r.text();
    } catch (e) {
      $code.textContent = `# Failed to load: ${e.message}`;
      $code.className = '';
      return;
    }

    await window.__loadPrism();

    $code.textContent = text;
    $code.className = 'language-python';

    let highlighted = false;
    try {
      window.Prism.highlightElement($code);
      highlighted = true;
    } catch (e) {
      console.warn('Prism.highlightElement failed:', e);
    }

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
          for (let i = 0; i < rows.children.length; i++) {
            rows.children[i].style.lineHeight = codeLineHeight;
          }
        } else {
          const n = $code.textContent.split('\n').length;
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

  // ---------- keyboard nav (unchanged) ----------

  document.addEventListener('keydown', (e) => {
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
    loadFilterCatalog();
    refresh();
  }));

  // initial load
  loadData().then(() => {
    loadFilterCatalog();
    refresh();
  }).catch(e => {
    $count.textContent = `Failed to load data: ${e.message}`;
  });
})();
