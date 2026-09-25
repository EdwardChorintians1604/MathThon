/**
 * KATEX RENDERER OPTIMIZED
 * ========================
 * Optimasi rendering LaTeX untuk MathThon AI dengan:
 * - Lazy rendering (hanya render yang terlihat)
 * - Batch processing untuk multiple equations
 * - Error handling yang lebih baik
 * - Performance monitoring
 */

class KaTeXRendererOptimized {
  constructor() {
    this.renderQueue = [];
    this.isRendering = false;
    this.observedElements = new WeakSet();
    this.initIntersectionObserver();
  }

  /**
   * Initialize Intersection Observer untuk lazy rendering
   * Hanya render math equations saat user scrolling dekat dengan elemen
   */
  initIntersectionObserver() {
    if (!('IntersectionObserver' in window)) {
      console.warn('IntersectionObserver tidak tersedia, menggunakan fallback');
      this.renderImmediately = true;
      return;
    }

    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && entry.target.textContent.trim()) {
            this.renderElement(entry.target);
            this.observer.unobserve(entry.target);
          }
        });
      },
      {
        root: document.getElementById('chat-scroll'),
        rootMargin: '100px', // Pre-load 100px sebelum masuk viewport
        threshold: 0,
      }
    );
  }

  /**
   * Render LaTeX dalam elemen dengan error handling
   */
  renderElement(el) {
    if (!el || this.observedElements.has(el)) return;

    try {
      if (typeof renderMathInElement !== 'undefined') {
        renderMathInElement(el, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true },
          ],
          throwOnError: false,
          strict: false, // Ignore minor parsing errors
          output: 'html', // Render to HTML (lebih cepat dari MathML)
        });
        this.observedElements.add(el);
      }
    } catch (err) {
      console.warn('KaTeX render error:', err, el);
      // Fallback ke Unicode jika KaTeX gagal
      this.fallbackToUnicode(el);
    }
  }

  /**
   * Batch render multiple elements untuk performa lebih baik
   */
  renderBatch(elements) {
    if (this.isRendering) {
      elements.forEach((el) => this.renderQueue.push(el));
      return;
    }

    this.isRendering = true;

    // Process with requestAnimationFrame untuk smooth rendering
    requestAnimationFrame(() => {
      elements.forEach((el) => {
        if (!this.observedElements.has(el)) {
          this.renderElement(el);
        }
      });

      this.isRendering = false;

      // Process queue jika ada
      if (this.renderQueue.length > 0) {
        const queued = this.renderQueue.splice(0, 5);
        this.renderBatch(queued);
      }
    });
  }

  /**
   * Render with Intersection Observer (untuk messages baru)
   */
  observeElement(el) {
    if (this.observer && !this.observedElements.has(el)) {
      this.observer.observe(el);
    } else if (this.renderImmediately) {
      this.renderElement(el);
    }
  }

  /**
   * Re-render semua equations (saat DOM berubah drastis)
   */
  renderAll(container) {
    if (!container) container = document.getElementById('chat-scroll');
    const elements = container.querySelectorAll('.msg-ai-content');
    this.renderBatch(Array.from(elements));
  }

  /**
   * Fallback ke Unicode untuk LaTeX yang gagal
   * (Jika KaTeX gagal, tampilkan notasi Unicode yang lebih readable)
   */
  fallbackToUnicode(el) {
    const text = el.textContent;

    // Conversions LaTeX → Unicode
    const replacements = [
      [/\$\$(.*?)\$\$/g, '$1'], // Remove outer $$
      [/\\infty/g, '∞'],
      [/\\pi/g, 'π'],
      [/\\alpha/g, 'α'],
      [/\\beta/g, 'β'],
      [/\\theta/g, 'θ'],
      [/\\sum/g, '∑'],
      [/\\int/g, '∫'],
      [/\\times/g, '×'],
      [/\\div/g, '÷'],
      [/\\sqrt\{([^}]+)\}/g, '√($1)'],
      [/\^(\d+)/g, '$1'], // Simple superscript fallback
    ];

    let converted = text;
    replacements.forEach(([pattern, replacement]) => {
      converted = converted.replace(pattern, replacement);
    });

    el.textContent = converted;
  }

  /**
   * Monitor rendering performance
   */
  startPerfMonitor() {
    if (!window.performance || !window.performance.mark) return;

    performance.mark('math-render-start');
    return () => {
      performance.mark('math-render-end');
      performance.measure('math-render', 'math-render-start', 'math-render-end');
      const measure = performance.getEntriesByName('math-render')[0];
      if (measure && measure.duration > 100) {
        console.warn(`⚠️ KaTeX rendering lambat: ${measure.duration.toFixed(2)}ms`);
      }
    };
  }
}

// ─────────────────────────────────────────────────────
// GLOBAL INSTANCE & INTEGRATION
// ─────────────────────────────────────────────────────

const mathRenderer = new KaTeXRendererOptimized();

/**
 * Override function renderMath dari template asli
 * Gunakan optimized renderer
 */
function renderMath(el) {
  if (!el) {
    mathRenderer.renderAll();
  } else {
    mathRenderer.observeElement(el);
  }
}

/**
 * Hook ke function appendMsg untuk auto-render saat pesan baru
 * Pastikan dipanggil setelah appendMsg
 */
const originalAppendMsg = window.appendMsg;
window.appendMsg = function (role, text) {
  // Call original function
  originalAppendMsg.call(this, role, text);

  // Then render new message dengan observer
  if (role === 'ai') {
    const chatbox = document.getElementById('chatbox');
    const lastMessage = chatbox?.lastElementChild?.querySelector('.msg-ai-content');
    if (lastMessage) {
      mathRenderer.observeElement(lastMessage);
    }
  }
};

/**
 * Export untuk debugging/monitoring
 */
window.MathRendererDebug = {
  renderAll: () => mathRenderer.renderAll(),
  renderElement: (el) => mathRenderer.renderElement(el),
  getStats: () => ({
    observedCount: mathRenderer.observedElements.size,
    queueLength: mathRenderer.renderQueue.length,
    isRendering: mathRenderer.isRendering,
  }),
  forceResetObserver: () => {
    mathRenderer.observedElements = new WeakSet();
    console.log('Observer reset complete');
  },
};

console.log('✅ KaTeX Renderer Optimized loaded');
