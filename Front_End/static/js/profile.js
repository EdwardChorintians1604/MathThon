// Profile Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize
    const profileData = document.body.dataset.profile;
    const photoUrl = document.body.dataset.photoUrl || '/static/image/default-avatar.png';

    // Parse profile data
    let userData = {};
    try {
        if (profileData && profileData !== '{}') {
            userData = JSON.parse(profileData);
        }
    } catch (e) {
        console.error('Error parsing profile data:', e);
    }

    // ============ MODAL HANDLERS ============
    const editModal = document.getElementById('editModal');
    const passwordModal = document.getElementById('passwordModal');

    function closeAllModals() {
        editModal.classList.remove('active');
        passwordModal.classList.remove('active');
    }

    // Edit Profile Modal
    const editProfileBtn = document.getElementById('editProfileBtn');
    const closeEditModal = document.getElementById('closeEditModal');
    const cancelEditBtn = document.getElementById('cancelEditBtn');

    if (editProfileBtn) {
        editProfileBtn.addEventListener('click', function() {
            document.getElementById('editName').value = userData.name || '';
            document.getElementById('editUsername').value = userData.username || '';
            document.getElementById('editEmail').value = userData.email || '';
            document.getElementById('editBornPlace').value = userData.born_place || '';
            document.getElementById('editBornDate').value = userData.born_date || '';
            editModal.classList.add('active');
        });
    }

    if (closeEditModal) {
        closeEditModal.addEventListener('click', closeAllModals);
    }

    if (cancelEditBtn) {
        cancelEditBtn.addEventListener('click', closeAllModals);
    }

    // Change Password Modal
    const changePasswordBtn = document.getElementById('changePasswordBtn');
    const closePasswordModal = document.getElementById('closePasswordModal');
    const cancelPasswordBtn = document.getElementById('cancelPasswordBtn');

    if (changePasswordBtn) {
        changePasswordBtn.addEventListener('click', function() {
            closeAllModals();
            passwordModal.classList.add('active');
        });
    }

    if (closePasswordModal) {
        closePasswordModal.addEventListener('click', closeAllModals);
    }

    if (cancelPasswordBtn) {
        cancelPasswordBtn.addEventListener('click', closeAllModals);
    }

    // Close modal on overlay click
    [editModal, passwordModal].forEach(modal => {
        if (modal) {
            modal.addEventListener('click', function(e) {
                if (e.target === this) {
                    closeAllModals();
                }
            });
        }
    });

    // ============ FORM SUBMISSIONS ============
    const editProfileForm = document.getElementById('editProfileForm');
    if (editProfileForm) {
        editProfileForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData();
            formData.append('name', document.getElementById('editName').value);
            formData.append('email', document.getElementById('editEmail').value);
            formData.append('born_place', document.getElementById('editBornPlace').value);
            formData.append('date', document.getElementById('editBornDate').value);

            const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';

            fetch('/user/update_profile', {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    return response.text().then(text => {
                        throw new Error(`HTTP ${response.status}: ${text}`);
                    });
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    showToast('Profil berhasil diperbarui!', 'success');
                    userData.name = document.getElementById('editName').value;
                    userData.email = document.getElementById('editEmail').value;
                    userData.born_place = document.getElementById('editBornPlace').value;
                    userData.born_date = document.getElementById('editBornDate').value;
                    updateDisplay();
                    closeAllModals();
                } else {
                    showToast(data.message || data.error || 'Gagal memperbarui profil', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('Terjadi kesalahan saat memperbarui profil', 'error');
            });
        });
    }

    const changePasswordForm = document.getElementById('changePasswordForm');
    if (changePasswordForm) {
        changePasswordForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const oldPassword = document.getElementById('oldPassword').value;
            const newPassword = document.getElementById('newPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (newPassword !== confirmPassword) {
                showToast('Password baru dan konfirmasi tidak cocok', 'error');
                return;
            }

            if (newPassword.length < 6) {
                showToast('Password minimal 6 karakter', 'error');
                return;
            }

            const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';

            fetch('/user/change_password', {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    old_password: oldPassword,
                    new_password: newPassword
                })
            })
            .then(response => {
                if (!response.ok) {
                    return response.text().then(text => {
                        throw new Error(`HTTP ${response.status}: ${text}`);
                    });
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    showToast('Password berhasil diubah!', 'success');
                    changePasswordForm.reset();
                    closeAllModals();
                } else {
                    showToast(data.message || 'Gagal mengubah password', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('Terjadi kesalahan saat mengubah password', 'error');
            });
        });
    }

    // ============ AVATAR UPLOAD ============
    const fileInput = document.getElementById('fileInput');
    const avatarUpload = document.getElementById('avatarUpload');

    if (avatarUpload && fileInput) {
        avatarUpload.addEventListener('click', function(e) {
            if (e.target !== fileInput) {
                fileInput.click();
            }
        });

        fileInput.addEventListener('change', function(e) {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    const avatarImg = document.getElementById('avatarImg');
                    if (avatarImg) {
                        avatarImg.src = event.target.result;
                    }
                    uploadProfilePhoto(fileInput.files[0]);
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    }

    function uploadProfilePhoto(file) {
        const formData = new FormData();
        formData.append('file', file);

        const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';

        fetch('/user/upload_profile_photo', {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.text().then(text => {
                    throw new Error(`HTTP ${response.status}: ${text}`);
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                showToast('Foto profil berhasil diperbarui!', 'success');
                userData.photo_url = data.photo_url;
                setTimeout(() => {
                    location.reload();
                }, 1500);
            } else {
                showToast(data.message || 'Gagal mengunggah foto profil', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showToast('Terjadi kesalahan saat mengunggah foto', 'error');
        });
    }

    // ============ SETTINGS ============
    const langSelect = document.getElementById('langSelect');
    if (langSelect) {
        langSelect.addEventListener('change', function() {
            localStorage.setItem('selectedLanguage', this.value);
            showToast('Bahasa berhasil diubah ke ' + this.value.toUpperCase(), 'info');
        });
    }

    const fontRange = document.getElementById('fontRange');
    const fontVal = document.getElementById('fontVal');
    if (fontRange && fontVal) {
        fontRange.addEventListener('input', function() {
            const size = this.value + 'px';
            fontVal.textContent = size;
            document.documentElement.style.fontSize = size;
            localStorage.setItem('fontSize', this.value);
        });

        // Load saved font size
        const savedFontSize = localStorage.getItem('fontSize') || '16';
        fontRange.value = savedFontSize;
        document.documentElement.style.fontSize = savedFontSize + 'px';
        fontVal.textContent = savedFontSize + 'px';
    }

    // Theme Toggle
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.checked = localStorage.getItem('theme') !== 'light';
        themeToggle.addEventListener('change', function() {
            localStorage.setItem('theme', this.checked ? 'dark' : 'light');
            showToast('Tema berhasil diubah', 'info');
        });
    }

    // Email Notification
    const emailNotif = document.getElementById('emailNotif');
    if (emailNotif) {
        emailNotif.checked = localStorage.getItem('emailNotif') !== 'false';
        emailNotif.addEventListener('change', function() {
            localStorage.setItem('emailNotif', this.checked);
            showToast(this.checked ? 'Notifikasi diaktifkan' : 'Notifikasi dinonaktifkan', 'info');
        });
    }

    // ============ DELETE ACCOUNT ============
    const deleteAccountBtn = document.getElementById('deleteAccountBtn');
    if (deleteAccountBtn) {
        deleteAccountBtn.addEventListener('click', function() {
            const confirmDelete = confirm('Apakah Anda yakin ingin menghapus akun? Tindakan ini TIDAK DAPAT DIBATALKAN!');
            if (!confirmDelete) return;
            
            const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';
            
            fetch('/user/delete_account', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showToast('Akun berhasil dihapus. Anda akan dialihkan...', 'success');
                    setTimeout(() => {
                        window.location.href = '/';
                    }, 2000);
                } else {
                    showToast(data.message || 'Gagal menghapus akun', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('Terjadi kesalahan saat menghapus akun', 'error');
            });
        });
    }

    // ============ LOGOUT ============
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            window.location.href = '/logout';
        });
    }

    // ============ DISPLAY FUNCTIONS ============
    function updateDisplay() {
        const elements = {
            displayName: userData.name || 'Nama Pengguna',
            displayUsername: '@' + (userData.username || 'username'),
            displayUsername2: userData.username || '-',
            displayEmail: userData.email || '-',
            displayBirth: userData.born_place || '-',
            displayDate: userData.born_date || '-'
        };

        for (const [id, value] of Object.entries(elements)) {
            const el = document.getElementById(id);
            if (el) el.textContent = value;
        }
    }

    function showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = 'toast ' + type;
        toast.textContent = message;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.remove();
        }, 4000);
    }

    // Initialize display
    updateDisplay();

    // Initialize AOS if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out'
        });
    }

    console.log('Profile page initialized', userData);
});
