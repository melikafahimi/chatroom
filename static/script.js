function sendMessage() {
  const username = document.getElementById("username").value;
  const message = document.getElementById("message").value;

  if (!username || !message) return;

  fetch("/send", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({username, message})
  }).then(() => {
    document.getElementById("message").value = "";
    loadMessages();
  });
}

function loadMessages() {
  fetch("/messages")
    .then(r => r.json())
    .then(data => {
      const box = document.getElementById("messages");
      box.innerHTML = "";
      data.forEach(m => {
        const d = document.createElement("div");
        d.className = "msg";
        d.innerText = m.username + ": " + m.message;
        box.appendChild(d);
      });
      box.scrollTop = box.scrollHeight;
    });
}

setInterval(loadMessages, 1000);
