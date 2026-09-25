function updateConvTitle() {
    const conv = conversations.find(c => c.id === currentConvId);
    if (!conv) return;
    conv.title = document.getElementById('conv-title').value;
    renderConversationList();
}

// Sync judul input saat memilih percakapan
async function selectConversation(id) {
    currentConvId = id;
    renderConversationList();
    const conv = conversations.find(c => c.id === id);
    document.getElementById('conv-title').value = conv ? conv.title : '';
    renderChat(conv ? conv.messages : []);
}
// State percakapan
let conversations = [];
let currentConvId = null;

// Load daftar percakapan saat halaman dibuka
window.addEventListener('DOMContentLoaded', async () => {
    await loadConversations();
    if (conversations.length > 0) {
        selectConversation(conversations[0].id);
    } else {
        newConversation();
    }
});

async function loadConversations() {
const res = await fetch('/api/ai/conversation_archive');
    conversations = await res.json();
    renderConversationList();
}

function renderConversationList() {
    const list = document.getElementById('conversation-list');
    list.innerHTML = '';
    for (const conv of conversations) {
        const li = document.createElement('li');
        li.style.marginBottom = '8px';
        li.innerHTML = `<a href="#" onclick="selectConversation('${conv.id}')" style="text-decoration:none;color:${conv.id===currentConvId?'#4f46e5':'#222'};font-weight:${conv.id===currentConvId?'bold':'normal'};">${escapeHtml(conv.title||'Tanpa Judul')}</a> <span style='color:gray;font-size:0.9em;'>${conv.timestamp||''}</span>`;
        list.appendChild(li);
    }
}

function renderChat(messages) {
    const chatEl = document.getElementById('chatbox');
    chatEl.innerHTML = '';
    if (!messages || messages.length === 0) {
        chatEl.innerHTML = `<div class="chat-message ai-msg"><div class="message-bubble">Halo User 👋<br>Ada yang bisa saya bantu hari ini?</div></div>`;
        return;
    }
    for (const msg of messages) {
        const isUser = msg.startsWith('You : ');
        chatEl.innerHTML += `<div class="chat-message ${isUser?'user-msg':'ai-msg'}"><div class="message-bubble">${escapeHtml(msg)}</div></div>`;
    }
    chatEl.scrollTop = chatEl.scrollHeight;
}

function newConversation() {
    const title = prompt('Judul percakapan baru:') || 'Percakapan Baru';
    const now = new Date();
    const conv = {
        id: 'local-'+Date.now(),
        title,
        messages: [],
        timestamp: now.toISOString().slice(0,19).replace('T',' ')
    };
    conversations.unshift(conv);
    currentConvId = conv.id;
    renderConversationList();
    renderChat([]);
}

async function saveConversation() {
    const conv = conversations.find(c => c.id === currentConvId);
    if (!conv) return alert('Pilih percakapan dulu!');
    // Sinkron judul dari input
    const titleInput = document.getElementById('conv-title');
    conv.title = titleInput.value.trim() || 'Percakapan';
    // Ambil hanya penggalan percakapan aktif
    const messages = conv.messages;
    if (!messages || messages.length === 0) return alert('Belum ada percakapan untuk disimpan.');
    let res;
    if (conv.id && !conv.id.startsWith('local-')) {
        // Update percakapan lama
        res = await fetch(`/api/ai/update_conversation/${conv.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: conv.title, messages })
        });
    } else {
        // Simpan baru
        res = await fetch('/api/ai/save_conversation', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: conv.title, messages })
        });
    }
    if (res.ok) {
        await loadConversations();
        if (currentConvId.startsWith('local-') && conversations.length > 0) {
            selectConversation(conversations[0].id);
        }
        alert('Percakapan berhasil disimpan!');
    } else {
        alert('Gagal menyimpan percakapan.');
    }
}

async function deleteConversation() {
    if (!currentConvId) return alert('Pilih percakapan yang ingin dihapus!');
    if (!confirm('Yakin ingin menghapus percakapan ini?')) return;
    // Hapus di backend jika sudah tersimpan
    if (!currentConvId.startsWith('local-')) {
        await fetch(`/api/ai/delete_conversation/${currentConvId}`, { method: 'DELETE' });
        await loadConversations();
        if (conversations.length > 0) selectConversation(conversations[0].id);
        else newConversation();
    } else {
        // Hapus lokal
        conversations = conversations.filter(c => c.id !== currentConvId);
        if (conversations.length > 0) selectConversation(conversations[0].id);
        else newConversation();
    }
}

// Kirim pesan dan auto-tambah ke percakapan aktif
async function sendMessage() {
    const msgEl = document.getElementById('msg');
    const chatEl = document.getElementById('chatbox');
    const text = msgEl.value.trim();
    if (!text) return;
    const conv = conversations.find(c => c.id === currentConvId);
    if (!conv) return alert('Pilih percakapan dulu!');
    // Tambah pesan user
    conv.messages.push('You : ' + text);
    renderChat(conv.messages);
    msgEl.value = '';
    // Kirim ke backend AI
    try {
        const res = await fetch('/api/ai/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const contentType = res.headers.get('content-type') || '';
        let aiReply = '';
        if (res.ok) {
            const data = contentType.includes('application/json') ? await res.json() : { response: await res.text() };
            aiReply = data.reply || data.response || '(tidak ada jawaban)';
        } else {
            aiReply = 'Error: ' + (await res.text());
        }
        conv.messages.push('AI : ' + aiReply);
        renderChat(conv.messages);
    } catch (e) {
        conv.messages.push('AI : Error: ' + e.message);
        renderChat(conv.messages);
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

document.getElementById('msg').addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

// Tampilkan arsip judul percakapan
async function showArchive() {
    try {
        const res = await fetch('/api/ai/conversation_archive');
        if (!res.ok) throw new Error('Gagal mengambil arsip.');
        const data = await res.json();
        // data: [{id, title, timestamp}]
        let html = '<h4>Arsip Percakapan</h4><ul style="list-style:none;padding:0;">';
        if (data.length === 0) html += '<li>(Belum ada arsip)</li>';
        for (const conv of data) {
            html += `<li><a href="#" onclick="viewConversation('${conv.id}')">${conv.title}</a> <span style='color:gray;font-size:0.9em;'>(${conv.timestamp})</span></li>`;
        }
        html += '</ul>';
        showModal(html);
    } catch (e) {
        showModal('Gagal mengambil arsip: ' + e.message);
    }
}

// Tampilkan isi percakapan arsip
async function viewConversation(id) {
    try {
        const res = await fetch(`/api/ai/conversation/${id}`);
        if (!res.ok) throw new Error('Gagal mengambil isi percakapan.');
        const data = await res.json();
        let html = `<h4>${data.title}</h4><ul style='list-style:none;padding:0;'>`;
        for (const msg of data.messages) {
            html += `<li style='margin-bottom:8px;'>${msg}</li>`;
        }
        html += '</ul>';
        showModal(html);
    } catch (e) {
        showModal('Gagal mengambil isi percakapan: ' + e.message);
    }
}

// Modal sederhana untuk menampilkan arsip
function showModal(content) {
    let modal = document.getElementById('archive-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'archive-modal';
        modal.style.position = 'fixed';
        modal.style.top = '0';
        modal.style.left = '0';
        modal.style.width = '100vw';
        modal.style.height = '100vh';
        modal.style.background = 'rgba(0,0,0,0.3)';
        modal.style.zIndex = '9999';
        modal.style.display = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        modal.innerHTML = `<div style='background:#fff;padding:30px;border-radius:12px;max-width:400px;width:90%;box-shadow:0 4px 24px rgba(0,0,0,0.2);position:relative;'>${content}<br><button onclick='document.getElementById("archive-modal").remove()' style='margin-top:10px;'>Tutup</button></div>`;
        document.body.appendChild(modal);
    } else {
        modal.querySelector('div').innerHTML = content + "<br><button onclick='document.getElementById(\"archive-modal\").remove()' style='margin-top:10px;'>Tutup</button>";
        modal.style.display = 'flex';
    }
}
