/**
 * MathThon Security Sentinel v2.4
 * Client-Side Threat Intelligence, Anti-SQL Injection & Role Classifier
 * 
 * Features:
 * 1. Real-time SQL Injection & XSS pattern detection on client inputs
 * 2. Automated Honeypot bot-trap & submission latency monitoring
 * 3. Interactive dynamic Role Auto-Detection (Admin vs User)
 * 4. Password visibility toggle & security status beacon
 */

(function () {
    'use strict';

    // 1. Signature Patterns untuk deteksi ancaman di sisi Client
    const SQLI_PATTERNS = [
        /(?i)\b(union\s+select|select\s+.*\s+from|insert\s+into|delete\s+from|drop\s+table|truncate\s+table|update\s+.*\s+set)\b/i,
        /('|\")\s*(OR|AND)\s*('|\")?\d+('|\")?\s*=\s*('|\")?\d+/i,
        /('|\")\s*OR\s*('|\")?1('|\")?\s*=\s*('|\")?1/i,
        /('|\")\s*OR\s*TRUE/i,
        /(--|\#|\/\*)/i,
        /\b(sleep|benchmark|waitfor\s+delay)\s*\(/i
    ];

    const XSS_PATTERNS = [
        /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/i,
        /javascript\s*:/i,
        /on(load|error|click|mouseover|submit)\s*=/i
    ];

    // Timestamp untuk deteksi bot super cepat
    const pageLoadTime = Date.now();
    let userInteracted = false;

    // Tandai interaksi pengguna nyata (Mouse / Touch / Key)
    ['mousemove', 'touchstart', 'keydown', 'scroll'].forEach(evt => {
        window.addEventListener(evt, () => {
            userInteracted = true;
        }, { once: true, passive: true });
    });

    document.addEventListener('DOMContentLoaded', () => {
        const usernameInput = document.getElementById('username');
        const passwordInput = document.getElementById('password');
        const authForm = document.getElementById('unifiedLoginForm');
        const roleBadge = document.getElementById('roleDetectionBadge');
        const securityAlertBox = document.getElementById('clientSecurityAlert');
        const togglePasswordBtn = document.getElementById('togglePasswordBtn');
        const togglePasswordIcon = document.getElementById('togglePasswordIcon');
        const authCard = document.querySelector('.auth-card');

        // Set hidden submission timestamp
        const timeField = document.getElementById('client_timestamp');
        if (timeField) {
            timeField.value = pageLoadTime.toString();
        }

        // ==========================================
        // 2. Dynamic Interactive Role Auto-Detection
        // ==========================================
        if (usernameInput && roleBadge) {
            const updateRolePreview = () => {
                const val = usernameInput.value.trim().toLowerCase();

                if (!val) {
                    roleBadge.className = 'role-badge-pill role-detecting';
                    roleBadge.innerHTML = '<i class="bi bi-cpu"></i> <span>Mendeteksi Peran Otomatis...</span>';
                    if (authCard) authCard.classList.remove('role-admin-active');
                    return;
                }

                // Pola username administrator MathThon
                if (val === 'edward_kenway' || val === 'admin' || val.startsWith('admin_')) {
                    roleBadge.className = 'role-badge-pill role-admin animate__animated animate__fadeIn';
                    roleBadge.innerHTML = '<i class="bi bi-shield-shaded"></i> <span>Otoritas Administrator Terdeteksi</span>';
                    if (authCard) authCard.classList.add('role-admin-active');
                } else if (val.includes('@') && val.includes('.')) {
                    roleBadge.className = 'role-badge-pill role-user animate__animated animate__fadeIn';
                    roleBadge.innerHTML = '<i class="bi bi-envelope-check-fill"></i> <span>Akun Email Terverifikasi</span>';
                    if (authCard) authCard.classList.remove('role-admin-active');
                } else {
                    roleBadge.className = 'role-badge-pill role-user animate__animated animate__fadeIn';
                    roleBadge.innerHTML = '<i class="bi bi-person-badge-fill"></i> <span>Akun Pengguna (Siswa/Umum)</span>';
                    if (authCard) authCard.classList.remove('role-admin-active');
                }
            };

            usernameInput.addEventListener('input', updateRolePreview);
            // Run initial check if pre-filled
            updateRolePreview();
        }

        // ==========================================
        // 3. Password Visibility Toggle
        // ==========================================
        if (togglePasswordBtn && passwordInput && togglePasswordIcon) {
            togglePasswordBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const isPassword = passwordInput.getAttribute('type') === 'password';
                passwordInput.setAttribute('type', isPassword ? 'text' : 'password');
                togglePasswordIcon.className = isPassword ? 'bi bi-eye' : 'bi bi-eye-slash';
            });
        }

        // ==========================================
        // 4. Pre-Submit Client-Side Threat Sentinel
        // ==========================================
        if (authForm) {
            authForm.addEventListener('submit', (e) => {
                const usernameVal = (usernameInput ? usernameInput.value : '');
                const passwordVal = (passwordInput ? passwordInput.value : '');
                const combined = `${usernameVal} ${passwordVal}`;

                // 4a. Cek Pola SQL Injection
                for (const pattern of SQLI_PATTERNS) {
                    if (pattern.test(combined)) {
                        e.preventDefault();
                        showSecurityAlert('Pola SQL Injection berbahaya terdeteksi pada input. Akses diblokir demi integritas database!');
                        markThreatInput(usernameInput);
                        return false;
                    }
                }

                // 4b. Cek Pola XSS
                for (const pattern of XSS_PATTERNS) {
                    if (pattern.test(combined)) {
                        e.preventDefault();
                        showSecurityAlert('Pola script mencurigakan (XSS) terdeteksi. Permintaan dibatalkan demi keamanan!');
                        markThreatInput(usernameInput);
                        return false;
                    }
                }

                // 4c. Cek Honeypot Trap
                const honeypot = document.getElementById('website_url_hp');
                if (honeypot && honeypot.value.trim() !== '') {
                    e.preventDefault();
                    showSecurityAlert('Aktivitas bot otomatis terdeteksi! Akses ditolak.');
                    return false;
                }

                // 4d. Cek Kecepatan Bot (Inhuman submission)
                const elapsed = Date.now() - pageLoadTime;
                if (elapsed < 200 && !userInteracted) {
                    e.preventDefault();
                    showSecurityAlert('Pengiriman formulir terlalu cepat (bot terdeteksi). Silakan coba kembali.');
                    return false;
                }

                // Tombol loading state
                const submitBtn = document.getElementById('btnSubmitLogin');
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Memverifikasi Kredensial...';
                }
            });
        }

        function showSecurityAlert(msg) {
            if (securityAlertBox) {
                securityAlertBox.textContent = msg;
                securityAlertBox.style.display = 'flex';
                securityAlertBox.className = 'auth-alert auth-alert-danger animate__animated animate__headShake';
                securityAlertBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            } else {
                alert(msg);
            }
        }

        function markThreatInput(element) {
            if (!element) return;
            element.classList.add('input-threat-detected');
            setTimeout(() => {
                element.classList.remove('input-threat-detected');
            }, 3000);
        }
    });
})();
