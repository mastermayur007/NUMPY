document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('checkerboard-form');
    const resultDiv = document.getElementById('checkerboard-output');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const n = document.getElementById('size').value;

        fetch('http://127.0.0.1:5000/checkbord', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ size: n })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = '';
            if (data.error) {
                resultDiv.textContent = data.error;
                return;
            }
            const checkerboard = data;
            checkerboard.forEach(row => {
                const rowDiv = document.createElement('div');
                rowDiv.classList.add('row');
                row.forEach(cell => {
                    const cellDiv = document.createElement('div');
                    cellDiv.classList.add('cell');
                    cellDiv.style.backgroundColor = cell === 0 ? 'white' : 'black';
                    rowDiv.appendChild(cellDiv);
                });
                resultDiv.appendChild(rowDiv);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = 'An error occurred while generating the checkerboard.';
        });
    });
});