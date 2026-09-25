# 🎨 FRONTEND: KaTeX Renderer Integration Guide

## 📋 Overview
File `katex-renderer-optimized.js` sudah tersedia di `Front_End/static/js/`. 

Ini adalah **optimization layer** untuk rendering LaTeX math equations:
- ✅ Lazy rendering (hanya render math yang visible)
- ✅ Batch processing untuk multiple equations
- ✅ Better error handling
- ✅ Performance monitoring

---

## 🚀 INTEGRATION STEPS

### Step 1: Load KaTeX Library (If Not Already)

**Di `Front_End/templates/` file template HTML utama (header.html, main.html, atau chat page):**

```html
<!-- Add sebelum closing </head> tag -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/contrib/auto-render.min.js"></script>
```

---

### Step 2: Load Optimized Renderer

**Di template yang sama, SETELAH KaTeX scripts:**

```html
<!-- Optimized KaTeX Renderer -->
<script src="{{ url_for('static', filename='js/katex-renderer-optimized.js') }}"></script>

<script>
  // Initialize renderer saat DOM siap
  document.addEventListener('DOMContentLoaded', () => {
    const renderer = new KaTeXRendererOptimized();
    
    // Watch element untuk math rendering
    const chatContainer = document.getElementById('chat-messages'); // Adjust ID sesuai template
    if (chatContainer) {
      // Render semua math elements yang sudah ada
      renderer.renderContainer(chatContainer);
      
      // Observe container untuk math baru (dari AI response)
      renderer.observeContainer(chatContainer);
    }
  });
</script>
```

---

### Step 3: Make Sure Math Elements Have Correct Class

**Di AI response rendering code (JavaScript/Python template):**

Pastikan math equations memiliki class `.math` atau `math-block`:

```html
<!-- Inline Math -->
<span class="math">$x^2 + y^2 = z^2$</span>

<!-- Display Math -->
<div class="math math-block">$$\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$</div>
```

**Atau dengan LaTeX delimiters:**

```html
<!-- KaTeX auto-render akan recognize ini -->
<p>Persamaan: $x^2 + 1 = 0$</p>
<div>$$\int_0^\infty e^{-x} dx = 1$$</div>
```

---

### Step 4: Configure Auto-Render (If Using Auto-Render)

**Alternative approach dengan auto-render lebih simple:**

```html
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "$", right: "$", display: false},
        {left: "\\[", right: "\\]", display: true},
        {left: "\\(", right: "\\)", display: false}
      ],
      throwOnError: false,
      errorColor: '#cc0000'
    });
  });
</script>
```

---

## 🎯 Integration Checklist

### For Chat Page (Where AI Responses Appear)

- [ ] KaTeX library loaded (CDN or local)
- [ ] `katex-renderer-optimized.js` loaded
- [ ] Container ID is correct in JavaScript (`#chat-messages`, `#ai-response`, etc.)
- [ ] Math elements have correct delimiters (`$...$` or `$$...$$`)
- [ ] Test: Send AI query with math, verify LaTeX renders properly
- [ ] Test: Scroll down, verify lazy loading works
- [ ] Test: Multiple equations in one response render correctly

### For Profile/Materi Pages

If these pages also show mathematical content:

- [ ] Load KaTeX library
- [ ] Load renderer
- [ ] Configure observer for correct container
- [ ] Test rendering

---

## 🔍 Debugging

### Issue #1: Math not rendering

**Check:**
```javascript
// In browser console (F12 → Console)
console.log(window.katex); // Should exist
console.log(window.KaTeXRendererOptimized); // Should exist
console.log(document.querySelectorAll('.math')); // Should find elements
```

**Solution:**
1. Verify CDN links are correct (not blocked)
2. Check network tab in DevTools for 404 errors
3. Verify container ID matches actual HTML ID

---

### Issue #2: Slow rendering

**Check:**
- Browser DevTools → Performance tab
- Look for long tasks in rendering

**Solution:**
- Renderer sudah optimized dengan lazy loading
- If still slow: reduce batch size in `katex-renderer-optimized.js`
  
```javascript
// Line ~70 in katex-renderer-optimized.js
batchSize: 5  // Change from default if needed
```

---

### Issue #3: "?" symbols still appearing

**This is a BACKEND issue, not frontend:**

Check backend fixes:
```bash
# Verify model is deepseek-r1:8b
ollama ls

# Check Flask logs show correct model and temperature
# Should see: "MODEL_NAME: deepseek-r1:8b"
```

Frontend can't fix if backend sends wrong format.

---

## 📊 Complete HTML Example

**Minimal complete example:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>MathThon Chat</title>
    
    <!-- KaTeX Library -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/contrib/auto-render.min.js"></script>
</head>
<body>
    <!-- Chat Container -->
    <div id="chat-messages" class="chat-container">
        <!-- AI responses akan masuk sini -->
        <div class="message ai">
            <div class="content">
                Persamaan kuadrat: $x^2 - 3x + 2 = 0$
                $$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
            </div>
        </div>
    </div>

    <!-- Optimized Renderer -->
    <script src="static/js/katex-renderer-optimized.js"></script>
    
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const renderer = new KaTeXRendererOptimized();
            const chatContainer = document.getElementById('chat-messages');
            
            if (chatContainer) {
                renderer.renderContainer(chatContainer);
                renderer.observeContainer(chatContainer);
            }
        });
    </script>
</body>
</html>
```

---

## ⚡ Performance Tips

### 1. Use Intersection Observer (Default)
```javascript
// Already implemented - lazy loads math only when visible
// Most efficient for long conversations
```

### 2. Debounce on Scroll
```javascript
// For heavy pages, debounce rendering
const debounce = (fn, delay) => {
  let timeout;
  return () => {
    clearTimeout(timeout);
    timeout = setTimeout(fn, delay);
  };
};
```

### 3. Fallback to Simple Rendering (If Needed)
```javascript
// For old browsers without IntersectionObserver
window.renderMathInElement(document.body, {
  delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "$", right: "$", display: false}
  ],
  throwOnError: false
});
```

---

## ✅ Validation Checklist

After integration:

**Test 1: Inline Math**
```
Query to AI: "Hitung 2 + 2"
Expected: $2 + 2 = 4$ (renders as formatted equation)
```

**Test 2: Display Math**
```
Query to AI: "Rumus kuadrat"
Expected: 
$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
(renders centered with larger font)
```

**Test 3: Multiple Equations**
```
Query: "Jelaskan integral"
Expected: Multiple $...$ and $$...$$ all render
```

**Test 4: Lazy Loading**
```
- Send long response with many equations
- Scroll down
- Verify only visible equations render
- Performance should not degrade
```

**Test 5: Unicode vs LaTeX**
```
Query: "Akar dari 9"
Backend sends: $$\sqrt{9} = 3$$  ✅ GOOD
Backend sends: $$√9 = 3$$         ❌ BAD (will show as "?")
```

---

## 🎓 Summary

| Component | Status | What It Does |
|-----------|--------|--------------|
| KaTeX CDN | ✅ Required | Renders LaTeX to visual equations |
| katex-renderer-optimized.js | ✅ Optional but recommended | Optimizes rendering (lazy load, batch) |
| Backend (deepseek-r1:8b) | ✅ Required | Sends proper `\latex` format |
| System Prompt | ✅ Required | Enforces LaTeX-only output |

**All components must work together for perfect rendering!**

---

## 🚀 Next Steps

1. **Integrate KaTeX:** Add CDN link to template
2. **Add Renderer:** Include `katex-renderer-optimized.js`
3. **Test:** Send math queries to AI, verify rendering
4. **Monitor:** Check browser console for errors
5. **Optimize:** Use DevTools to profile performance

---

**Status: ✅ Frontend Renderer Ready to Deploy**

*Last updated: 2024*  
*MathThon LaTeX Rendering v1.0*
