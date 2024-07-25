function sendMessage() {
    var userInput = document.getElementById('user-input');
    var message = userInput.value.trim();
    
    if (message) {
        addMessage('user', message);
        userInput.value = '';
        
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({message: message}),
        })
        .then(response => response.json())
        .then(data => {
            addMessage('ai', data.response);
        });
    }
}

function addMessage(sender, text) {
    var chatMessages = document.getElementById('chat-messages');
    var messageElement = document.createElement('div');
    messageElement.classList.add('message', sender + '-message');
    messageElement.textContent = text;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});