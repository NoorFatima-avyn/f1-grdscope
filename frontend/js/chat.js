const chatToggle = document.getElementById('chat-toggle');
const chatBox = document.getElementById('chat-box');
const chatClose = document.getElementById('chat-close');
const chatInput = document.getElementById('chat-input');
const chatSend = document.getElementById('chat-send');
const chatMessages = document.getElementById('chat-messages');

chatToggle.addEventListener('click', () => {
    chatBox.style.display = chatBox.style.display === 'none' ? 'flex' : 'none';
});

chatClose.addEventListener('click', () => {
    chatBox.style.display = 'none';
});

async function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    appendMessage('user', message);
    chatInput.value = '';

    appendMessage('bot', '...');

    const response = await fetch('http://127.0.0.1:5000/api/chat/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, year: currentYear })
    });

    const data = await response.json();
    const botMessages = chatMessages.querySelectorAll('.bot-msg');
    botMessages[botMessages.length - 1].textContent = data.response;
}

function appendMessage(type, text) {
    const div = document.createElement('div');
    div.textContent = text;
    div.style.cssText = `
        padding: 8px 12px;
        border-radius: 8px;
        margin: 4px 0;
        max-width: 85%;
        font-size: 0.85rem;
        line-height: 1.4;
        ${type === 'user' 
            ? 'background:#E8002D;color:white;align-self:flex-end;' 
            : 'background:#222;color:#ccc;align-self:flex-start;'}
    `;
    if (type === 'bot') div.classList.add('bot-msg');
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

chatSend.addEventListener('click', sendMessage);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});