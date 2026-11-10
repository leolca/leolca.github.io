// Main JavaScript for Leonardo Araujo's Homepage

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initDropdown();
  initPubFilters();
  initCopyButtons();
});

// Theme Management
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const storedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  const currentTheme = storedTheme || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', currentTheme);
  updateThemeIcon(currentTheme);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const activeTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = activeTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('theme-icon');
  if (!icon) return;
  if (theme === 'dark') {
    // Show Sun icon
    icon.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`;
  } else {
    // Show Moon icon
    icon.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
  }
}

// Mobile Menu Toggle
function initMobileMenu() {
  const menuBtn = document.getElementById('menu-toggle');
  const navLinks = document.getElementById('nav-links');
  if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
  }
}

// Publication Search and Category Filters
function initPubFilters() {
  const searchInput = document.getElementById('pub-search');
  const filterChips = document.querySelectorAll('.filter-chip');
  const pubItems = document.querySelectorAll('.pub-item');
  const emptyState = document.getElementById('pub-empty');

  if (!pubItems.length) return;

  let activeCategory = 'all';
  let searchQuery = '';

  function applyFilters() {
    let visibleCount = 0;
    pubItems.forEach(item => {
      const itemCat = item.getAttribute('data-category') || 'article';
      const itemText = item.textContent.toLowerCase();
      
      const matchesCat = (activeCategory === 'all') || (itemCat === activeCategory);
      const matchesSearch = !searchQuery || itemText.includes(searchQuery);

      if (matchesCat && matchesSearch) {
        item.style.display = '';
        visibleCount++;
      } else {
        item.style.display = 'none';
      }
    });

    if (emptyState) {
      emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeCategory = chip.getAttribute('data-filter');
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilters();
    });
  }
}

// Dropdown Interaction (supports touch, click and hover)
function initDropdown() {
  const dropdownItems = document.querySelectorAll('.nav-item-dropdown');
  
  dropdownItems.forEach(item => {
    const trigger = item.querySelector('.nav-link');
    
    // Toggle on click for touch screens or mobile
    if (trigger) {
      trigger.addEventListener('click', (e) => {
        // If window is mobile or user clicks chevron
        if (window.innerWidth <= 920 || e.target.closest('.dropdown-chevron')) {
          e.preventDefault();
          item.classList.toggle('open');
        }
      });
    }

    // Keep open while mouse is hovering item or menu
    item.addEventListener('mouseenter', () => {
      item.classList.add('open');
    });

    item.addEventListener('mouseleave', () => {
      item.classList.remove('open');
    });
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item-dropdown')) {
      dropdownItems.forEach(item => item.classList.remove('open'));
    }
  });
}

// Copy to Clipboard
function initCopyButtons() {
  document.querySelectorAll('[data-copy]').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const text = btn.getAttribute('data-copy');
      try {
        await navigator.clipboard.writeText(text);
        const originalText = btn.innerHTML;
        btn.innerHTML = '✓ Copied!';
        setTimeout(() => {
          btn.innerHTML = originalText;
        }, 2000);
      } catch (err) {
        console.error('Failed to copy', err);
      }
    });
  });
}


