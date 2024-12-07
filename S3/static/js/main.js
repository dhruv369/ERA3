document.getElementById('fileInput').addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        if (data.image) {
            const img = document.getElementById('displayImage');
            img.src = data.image;
            img.style.display = 'block';
        }
    } catch (error) {
        console.error('Error uploading file:', error);
    }
});

async function preprocessImage() {
    const method = document.getElementById('preprocessMethod').value;
    try {
        const response = await fetch(`/preprocess/${method}`, {
            method: 'POST'
        });
        const data = await response.json();
        
        if (data.image) {
            const img = document.getElementById('displayImage');
            img.src = data.image;
            img.style.display = 'block';
        }
    } catch (error) {
        console.error('Error preprocessing image:', error);
    }
}

async function augmentImage() {
    const method = document.getElementById('augmentMethod').value;
    try {
        const response = await fetch(`/augment/${method}`, {
            method: 'POST'
        });
        const data = await response.json();
        
        if (data.image) {
            const img = document.getElementById('displayImage');
            img.src = data.image;
            img.style.display = 'block';
        }
    } catch (error) {
        console.error('Error augmenting image:', error);
    }
} 