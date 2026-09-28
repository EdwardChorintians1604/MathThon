// Legacy slider support.
// Keberadaan slider ini bersifat opsional; nama fungsi dibuat lokal agar tidak
// menimpa navigasi dashboard grafik pada halaman beranda.
(() => {
  function initialiseLegacySlider() {
    const legacySlides = document.querySelectorAll('.slide');
    const legacyDots = document.querySelectorAll('.dot');
    const legacyPrevButton = document.getElementById('prevBtn');
    const legacyNextButton = document.getElementById('nextBtn');

    if (!legacySlides.length || !legacyDots.length || !legacyPrevButton || !legacyNextButton) {
      return;
    }

    let legacySlideIndex = 0;

    const showLegacySlide = (index) => {
      legacySlideIndex = (index + legacySlides.length) % legacySlides.length;
      legacySlides.forEach((slide, slideIndex) => {
        slide.classList.toggle('active', slideIndex === legacySlideIndex);
      });
      legacyDots.forEach((dot, dotIndex) => {
        dot.classList.toggle('active', dotIndex === legacySlideIndex);
      });
      window.dispatchEvent(new CustomEvent('slideChanged', {
        detail: { slideIndex: legacySlideIndex }
      }));
    };

    legacyPrevButton.addEventListener('click', () => showLegacySlide(legacySlideIndex - 1));
    legacyNextButton.addEventListener('click', () => showLegacySlide(legacySlideIndex + 1));
    legacyDots.forEach((dot, index) => {
      dot.addEventListener('click', () => showLegacySlide(index));
    });

    showLegacySlide(0);
    window.setInterval(() => showLegacySlide(legacySlideIndex + 1), 5000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialiseLegacySlider, { once: true });
  } else {
    initialiseLegacySlider();
  }
})();
