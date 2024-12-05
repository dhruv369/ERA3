const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const clearButton = document.getElementById('clearButton');
const identifyButton = document.getElementById('identifyButton');
const result = document.getElementById('result');

let isDrawing = false;

function startDrawing(e) {
    isDrawing = true;
    draw(e);
}

function stopDrawing() {
    isDrawing = false;
    ctx.beginPath();
}

function draw(e) {
    if (!isDrawing) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineWidth = 20;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    result.textContent = '-';
}

function identifyDigit() {
    const imageData = canvas.toDataURL('image/png');
    
    fetch('/identify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }),
    })
    .then(response => response.json())
    .then(data => {
        result.textContent = data.digit;
    })
    .catch(error => {
        console.error('Error:', error);
        result.textContent = 'Error';
    });
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

clearButton.addEventListener('click', clearCanvas);
identifyButton.addEventListener('click', identifyDigit);

clearCanvas();

document.getElementById('showAnimal').addEventListener('click', function() {
    const selectedAnimal = document.querySelector('input[name="animal"]:checked');
    if (selectedAnimal) {
        fetch('/get_animal', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `animal=${selectedAnimal.value}`
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('animalImage').innerHTML = `<img src="${data.image}" alt="${selectedAnimal.value}">`;
        });
    }
});

document.getElementById('uploadFile').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('file', file);
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('fileInfo').textContent = data.error;
            } else {
                document.getElementById('fileInfo').innerHTML = `
                    <p>Name: ${data.name}</p>
                    <p>Size: ${data.size}</p>
                    <p>Type: ${data.type}</p>
                `;
            }
        });
    }
});
