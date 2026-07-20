document.querySelectorAll('.dropdown-toggle').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        btn.closest('.dropdown').classList.toggle('open');
    });
});

document.addEventListener('click', () => {
    document.querySelectorAll('.dropdown.open').forEach(d => d.classList.remove('open'));
});

window.openModal = (id) => document.getElementById(id)?.classList.add('open');
window.closeModal = (id) => document.getElementById(id)?.classList.remove('open');

document.querySelectorAll('.form-range').forEach(range => {
    const output = range.parentElement.querySelector('.range-value');
    if (output) {
        output.textContent = range.value;
        range.addEventListener('input', () => output.textContent = range.value);
    }
});

const Toast = {
    container: null,

    init() {
        if (this.container) return;
        this.container = document.createElement('div');
        this.container.className = 'toast-container';
        document.body.appendChild(this.container);
    },

    show(message, type = 'success', duration = 4000) {
        this.init();

        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;

        const icons = {
            success: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
            warning: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
            error: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>'
        };

        toast.innerHTML = `
            <span class="toast-icon">${icons[type] || icons.success}</span>
            <span class="toast-message">${message}</span>
            <button class="toast-close" onclick="Toast.dismiss(this.parentElement)">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
        `;

        this.container.appendChild(toast);
        requestAnimationFrame(() => toast.classList.add('show'));

        if (duration > 0) {
            setTimeout(() => this.dismiss(toast), duration);
        }

        return toast;
    },

    dismiss(toast) {
        if (!toast || toast.classList.contains('hiding')) return;
        toast.classList.add('hiding');
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    },

    success(message, duration) {
        return this.show(message, 'success', duration);
    },

    warning(message, duration) {
        return this.show(message, 'warning', duration);
    },

    error(message, duration) {
        return this.show(message, 'error', duration);
    }
};

window.Toast = Toast;

// Mobile sidebar toggle
const sidebarToggle = document.querySelector('.sidebar-toggle');
const sidebarBackdrop = document.querySelector('.sidebar-backdrop');

if (sidebarToggle) {
    sidebarToggle.addEventListener('click', () => {
        document.body.classList.toggle('sidebar-open');
    });
}

if (sidebarBackdrop) {
    sidebarBackdrop.addEventListener('click', () => {
        document.body.classList.remove('sidebar-open');
    });
}

const sidebarNav = document.querySelector('.sidebar-nav');

document.querySelectorAll('.sidebar-link').forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
            document.body.classList.remove('sidebar-open');
        }
        if (sidebarNav) {
            sessionStorage.setItem('sidebarScroll', sidebarNav.scrollTop);
        }
    });
});

if (sidebarNav) {
    const savedScroll = sessionStorage.getItem('sidebarScroll');
    if (savedScroll) sidebarNav.scrollTop = parseInt(savedScroll, 10);
}

function toggleSidebarSection(btn) {
    const section = btn.closest('.sidebar-section');
    section.classList.toggle('collapsed');
    const sectionName = section.dataset.section;
    const collapsed = JSON.parse(localStorage.getItem('sidebarCollapsed') || '{}');
    collapsed[sectionName] = section.classList.contains('collapsed');
    localStorage.setItem('sidebarCollapsed', JSON.stringify(collapsed));
}

window.toggleSidebarSection = toggleSidebarSection;

document.addEventListener('DOMContentLoaded', () => {
    const collapsed = JSON.parse(localStorage.getItem('sidebarCollapsed') || '{}');
    document.querySelectorAll('.sidebar-section').forEach(section => {
        const sectionName = section.dataset.section;
        if (sectionName in collapsed) {
            section.classList.toggle('collapsed', collapsed[sectionName]);
        }
    });
});
