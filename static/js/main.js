// main.js — students will add JavaScript here as features are built

// Video modal
(function () {
    const overlay = document.getElementById('videoModal');
    if (!overlay) return;

    const frame   = document.getElementById('videoFrame');
    const closeBtn = document.getElementById('modalClose');
    const dataSrc  = frame.getAttribute('data-src');

    function openModal() {
        frame.setAttribute('src', dataSrc);
        overlay.classList.add('is-open');
    }

    function closeModal() {
        overlay.classList.remove('is-open');
        // Stop video by clearing src, then restoring data-src for next open
        frame.setAttribute('src', '');
    }

    document.querySelectorAll('[data-video-trigger]').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            openModal();
        });
    });

    closeBtn.addEventListener('click', closeModal);

    overlay.addEventListener('click', function (e) {
        if (e.target === overlay) closeModal();
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeModal();
    });
}());
