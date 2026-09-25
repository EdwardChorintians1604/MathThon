// ─── State ───────────────────────────────────────────────
    let score = 0;
    let answeredCount = 0;

    // totalQuestions sekarang diambil dari variabel global yang didefinisikan di HTML

    // FIX 7: Null check sebelum ambil CSRF token
    const csrfMeta = document.querySelector('meta[name="csrf-token"]');
    const csrfToken = csrfMeta ? csrfMeta.getAttribute('content') : '';

    // ─── Sanitasi HTML (FIX 5: cegah XSS) ───────────────────
    function escapeHTML(str) {
        const div = document.createElement('div');
        div.appendChild(document.createTextNode(str));
        return div.innerHTML;
    }

    // ─── Submit Jawaban ───────────────────────────────────────
    function submitAnswer(index, questionId) {
        const input    = document.getElementById(`input-${index}`);
        const feedback = document.getElementById(`feedback-${index}`);
        const btn      = document.getElementById(`btn-${index}`);
        const nextBtn  = document.getElementById(`next-${index}`);

        // Null check elemen
        if (!input || !feedback || !btn || !nextBtn) {
            console.error(`Elemen tidak ditemukan untuk index ${index}`);
            return;
        }

        const answer = input.value.trim();

        if (!answer) {
            alert("Harap masukkan jawaban terlebih dahulu.");
            return;
        }

        // FIX 8: Simpan teks button asli agar bisa di-restore jika error
        const originalBtnText = btn.innerHTML;

        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Memeriksa...';

        fetch('/api/latihan/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                question_id: questionId,
                answer: answer
            })
        })
        .then(response => {
            // Cek apakah response OK sebelum parse JSON
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            input.disabled = true;
            btn.style.display = 'none';
            nextBtn.style.display = 'block';
            feedback.style.display = 'flex';

            answeredCount++;

            if (data.is_correct) {
                score++;
                feedback.className = 'feedback-area correct-feedback celebration';
                // FIX 5: Tidak ada user input di sini, aman pakai innerHTML
                feedback.innerHTML = '<i class="bi bi-check-circle-fill me-2"></i> Jawaban Benar! Kerja bagus.';
            } else {
                feedback.className = 'feedback-area wrong-feedback';
                // FIX 5: escapeHTML pada data dari server
                feedback.innerHTML = `<i class="bi bi-x-circle-fill me-2"></i> Kurang tepat. Jawaban yang benar adalah: <strong>${escapeHTML(String(data.correct_answer ?? '-'))}</strong>`;
            }

            // FIX 6: Hanya update progress di satu tempat (di sini)
            updateProgress(answeredCount);
        })
        .catch(error => {
            console.error('Error:', error);
            // FIX 8: Restore button ke kondisi semula jika gagal
            btn.disabled = false;
            btn.innerHTML = originalBtnText;
            alert("Terjadi kesalahan sistem. Silakan coba lagi.");
        });
    }

    // ─── Update Progress Bar ──────────────────────────────────
    // FIX 6: Satu fungsi, satu sumber kebenaran
    function updateProgress(count) {
        const progressBar = document.getElementById('session-progress');
        const counter     = document.getElementById('question-counter');

        if (progressBar) {
            const percent = totalQuestions > 0 ? Math.min(Math.round((count / totalQuestions) * 100), 100) : 0;
            progressBar.style.width = `${percent}%`;
            progressBar.setAttribute('aria-valuenow', percent);
        }

        if (counter) {
            counter.innerText = `Pertanyaan ${count}/${totalQuestions}`;
        }
    }

    // ─── Pindah ke Soal Berikutnya ────────────────────────────
    function nextQuestion(currentIndex) {
        const currentCard = document.getElementById(`q-${currentIndex}`);
        const nextCard    = document.getElementById(`q-${parseInt(currentIndex) + 1}`);

        if (currentCard) currentCard.style.display = 'none';

        if (nextCard) {
            // FIX 6: Counter diupdate dari answeredCount, bukan dari index
            // (hanya tampilkan nomor soal berikutnya yang sedang dikerjakan)
            const counterEl = document.getElementById('question-counter');
            if (counterEl) {
                counterEl.innerText = `Pertanyaan ${parseInt(currentIndex) + 2} / ${totalQuestions}`;
            }
            
            nextCard.style.display = 'block';
            nextCard.classList.add('animate__animated', 'animate__fadeInRight');
        } else {
            finishSession();
        }
    }

    // ─── Selesai ──────────────────────────────────────────────
    // FIX 4: Tampilkan skor + total soal + persentase
    function finishSession() {
        const wrapper    = document.getElementById('session-wrapper');
        const finishCard = document.getElementById('finish-card');
        const finalScore = document.getElementById('final-score');
        const finalTotal = document.getElementById('final-total');        // tambahkan elemen ini di HTML
        const finalPct   = document.getElementById('final-percentage');   // opsional

        if (wrapper)    wrapper.style.display    = 'none';
        if (finishCard) finishCard.style.display = 'block';
        if (finalScore) finalScore.innerText     = score;
        if (finalTotal) finalTotal.innerText     = totalQuestions;
        if (finalPct) {
            const pct = totalQuestions > 0
                ? Math.round((score / totalQuestions) * 100)
                : 0;
            finalPct.innerText = `${pct}%`;
        }
    }

    // ─── KaTeX Render ─────────────────────────────────────────
    // FIX: Gunakan window.onload agar KaTeX CDN sudah pasti selesai dimuat
    window.addEventListener('load', function () {
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(document.body, {
                delimiters: [
                    { left: '$$', right: '$$', display: true  },
                    { left: '$',  right: '$',  display: false },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '\\[', right: '\\]', display: true  }
                ],
                throwOnError: false
            });
        } else {
            console.warn('KaTeX renderMathInElement tidak ditemukan. Pastikan library sudah di-load.');
        }
    });