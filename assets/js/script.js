document.addEventListener('DOMContentLoaded', () => {
    // ==========================================================================
    // Theme Toggle
    // ==========================================================================
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    
    // Check for saved user preference, if any, on load of the website
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

    if (currentTheme) {
        document.body.classList.add(currentTheme);
        if (currentTheme === 'dark-theme') {
            themeIcon.classList.replace('ph-moon', 'ph-sun');
        }
    }

    themeToggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        let theme = 'light-theme';
        
        if (document.body.classList.contains('dark-theme')) {
            theme = 'dark-theme';
            themeIcon.classList.replace('ph-moon', 'ph-sun');
        } else {
            themeIcon.classList.replace('ph-sun', 'ph-moon');
        }
        
        localStorage.setItem('theme', theme);
    });

    // ==========================================================================
    // Mobile Menu
    // ==========================================================================
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const mobileLinks = mobileMenu.querySelectorAll('a');

    mobileBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        const icon = mobileBtn.querySelector('i');
        if (mobileMenu.classList.contains('hidden')) {
            icon.classList.replace('ph-x', 'ph-list');
        } else {
            icon.classList.replace('ph-list', 'ph-x');
        }
    });

    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
            mobileBtn.querySelector('i').classList.replace('ph-x', 'ph-list');
        });
    });

    // ==========================================================================
    // Entrance Experience
    // ==========================================================================
    const entranceOverlay = document.getElementById('entrance-overlay');
    const mainContent = document.getElementById('main-content');
    const doorContainer = document.getElementById('door');
    const skipBtn = document.getElementById('skip-btn');
    
    // Using a free Google sound effect for the door
    const doorSound = new Audio('https://actions.google.com/sounds/v1/doors/wood_door_open.ogg');
    
    // Check if user has visited before to auto-skip
    const hasVisited = sessionStorage.getItem('visited');
    
    if (hasVisited) {
        // Skip animation if already visited in this session
        entranceOverlay.style.display = 'none';
        mainContent.classList.remove('hidden');
        initScrollAnimations();
    } else {
        const enterSite = () => {
            doorSound.play().catch(e => console.log('Audio playback prevented by browser'));
            doorContainer.classList.add('opening');
            
            setTimeout(() => {
                entranceOverlay.style.opacity = '0';
                mainContent.classList.remove('hidden');
                
                setTimeout(() => {
                    entranceOverlay.style.display = 'none';
                    sessionStorage.setItem('visited', 'true');
                    initScrollAnimations(); // Initialize scroll animations after site is visible
                }, 1000);
            }, 800);
        };

        doorContainer.addEventListener('click', enterSite);
        if (skipBtn) {
            skipBtn.addEventListener('click', () => {
                entranceOverlay.style.opacity = '0';
                mainContent.classList.remove('hidden');
                setTimeout(() => {
                    entranceOverlay.style.display = 'none';
                    sessionStorage.setItem('visited', 'true');
                    initScrollAnimations();
                }, 500);
            });
        }
    }

    // ==========================================================================
    // Scroll Animations (Intersection Observer)
    // ==========================================================================
    function initScrollAnimations() {
        const fadeElements = document.querySelectorAll('.fade-in');
        
        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -100px 0px',
            threshold: 0
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target); // Stop observing once visible
                }
            });
        }, observerOptions);

        fadeElements.forEach(el => observer.observe(el));
    }

    // ==========================================================================
    // Navbar Scroll Effect
    // ==========================================================================
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
});

// ==========================================================================
// Lightbox Logic (Global Functions)
// ==========================================================================
function openLightbox(element) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const imgSrc = element.querySelector('img').src;
    
    lightboxImg.src = imgSrc;
    lightbox.classList.remove('hidden');
    document.body.style.overflow = 'hidden'; // Prevent scrolling
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.classList.add('hidden');
    document.body.style.overflow = 'auto'; // Restore scrolling
}

// Close lightbox on clicking outside image
document.getElementById('lightbox').addEventListener('click', function(e) {
    if (e.target === this) {
        closeLightbox();
    }
});

// ==========================================================================
// PDF Viewer (Iframe)
// ==========================================================================
const pdfModal = document.getElementById('pdf-modal');

if (pdfModal) {
    window.openPdfViewer = (url) => {
        const iframe = document.getElementById('pdf-iframe');
        const loader = document.getElementById('pdf-loading');
        
        // Reset iframe source first to prevent showing old PDF
        iframe.src = "";
        
        if(loader) loader.style.display = 'flex'; // Show loader

        // Give the loader a tiny fraction of a second to render before blocking thread
        setTimeout(() => {
            iframe.src = url + "#toolbar=0&navpanes=0&scrollbar=0";
        }, 50);

        pdfModal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    };

    window.hidePdfLoading = () => {
        // Wait 2 seconds to allow native PDF plugin to initialize and paint its content
        // covering the ugly black/grey screen it shows by default.
        setTimeout(() => {
            const loader = document.getElementById('pdf-loading');
            if(loader) loader.style.display = 'none'; // Hide loader
        }, 2000);
    };

    window.closePdfModal = () => {
        pdfModal.classList.add('hidden');
        document.body.style.overflow = 'auto';
        document.getElementById('pdf-iframe').src = "";
    };

    pdfModal.addEventListener('click', (e) => {
        if (e.target === pdfModal) closePdfModal();
    });
}
