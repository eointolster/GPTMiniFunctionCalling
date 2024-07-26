let conversation = [];

function sendMessage() {
    var userInput = document.getElementById('user-input');
    var message = userInput.value.trim();
    
    if (message) {
        conversation.push({"role": "user", "content": message});
        addMessage('user', message);
        userInput.value = '';
        
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({conversation: conversation}),
        })
        .then(response => response.json())
        .then(data => {
            if (data.conversation) {
                conversation = data.conversation;
                let aiResponse = conversation[conversation.length - 1].content;
                addMessage('ai', aiResponse);
            } else if (data.response) {
                addMessage('ai', data.response);
                conversation.push({"role": "assistant", "content": data.response});
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            addMessage('ai', 'Sorry, an error occurred.');
        });
    }
}

function addMessage(sender, text) {
    var chatMessages = document.getElementById('chat-messages');
    var messageElement = document.createElement('div');
    messageElement.classList.add('message', sender + '-message');
    
    // Convert the text to HTML, preserving line breaks and lists
    var formattedText = text
        .replace(/\n/g, '</p><p>')
        .replace(/^\d+\.\s/gm, '<ol><li>') + '</li></ol>';
    
    formattedText = '<p>' + formattedText + '</p>';
    formattedText = formattedText
        .replace(/<\/p><p><ol>/g, '<ol>')
        .replace(/<\/ol><\/p><p>/g, '</ol>')
        .replace(/<p><\/p>/g, '');
    
    messageElement.innerHTML = formattedText;
    
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
