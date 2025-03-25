const API_URL = 'http://localhost:8000';

document.getElementById('enhance-btn').addEventListener('click', async () => {
    const originalPrompt = document.getElementById('original-prompt').value;
    const loadingElement = document.getElementById('loading');
    const enhancedPromptElement = document.getElementById('enhanced-prompt');

    if (!originalPrompt.trim()) {
        alert('Please enter a prompt first');
        return;
    }

    try {
        loadingElement.classList.remove('hidden');
        enhancedPromptElement.textContent = '';

        const response = await fetch(`${API_URL}/rephrase`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: originalPrompt }),
        });

        const data = await response.json();
        enhancedPromptElement.textContent = data.enhanced_prompt;
    } catch (error) {
        let errorMessage = 'Error: Could not enhance prompt. ';
        if (!error.response) {
            errorMessage += 'Is the backend server running?';
        }
        enhancedPromptElement.textContent = errorMessage;
        console.error('Error:', error);
    } finally {
        loadingElement.classList.add('hidden');
    }
});
