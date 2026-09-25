async function sendMessage() {
  const msgEl = document.getElementById("msg");
  const chatEl = document.getElementById("chatbox");
  const text = msgEl.value.trim();
  if (!text) return;
  chatEl.innerHTML += `<div><b>You:</b> ${escapeHtml(text)}</div>`;
  msgEl.value = "";
  try {
    const res = await fetch("/api/ai/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    // Robust handling: response might be JSON or HTML (error page)
    const contentType = res.headers.get("content-type") || "";
    if (res.ok) {
      if (contentType.includes("application/json")) {
        const data = await res.json();
        if (data.reply) {
          chatEl.innerHTML += `<div><b>AI:</b> ${escapeHtml(data.reply)}</div>`;
        } else if (data.error) {
          chatEl.innerHTML += `<div style="color:red"><b>Error:</b> ${escapeHtml(data.error)}</div>`;
        } else {
          chatEl.innerHTML += `<div style="color:gray"><b>AI:</b> (tidak ada jawaban)</div>`;
        }
      } else {
        // fallback: non-JSON success response
        const textResp = await res.text();
        chatEl.innerHTML += `<div><b>AI:</b> ${escapeHtml(textResp)}</div>`;
      }
    } else {
      // error status: try json then text
      let errText = "";
      if (contentType.includes("application/json")) {
        const data = await res.json().catch(() => ({}));
        errText = data && data.error ? data.error : JSON.stringify(data);
      } else {
        errText = await res.text().catch(() => res.statusText);
      }
      chatEl.innerHTML += `<div style="color:red"><b>Error:</b> ${escapeHtml(errText)}</div>`;
    }
  } catch (e) {
    chatEl.innerHTML += `<div style="color:red"><b>Error:</b> ${escapeHtml(String(e))}</div>`;
  }
  chatEl.scrollTop = chatEl.scrollHeight;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

document.addEventListener("DOMContentLoaded", () => {
  const sendBtn = document.getElementById("send");
  const msg = document.getElementById("msg");
  if (sendBtn) sendBtn.addEventListener("click", sendMessage);
  if (msg) msg.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      sendMessage();
    }
  });
});