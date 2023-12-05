document.getElementById('sendBtn').addEventListener('click', () => {
    const key = document.getElementById('key').value;
    const value = document.getElementById('value').value;

    fetch('/set', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key, value }),
    }).then(response => response.json()).then(data => {
        document.getElementById('response').innerText = JSON.stringify(data);
    });
});

document.getElementById('getBtn').addEventListener('click', () => {
    const key = document.getElementById('key').value;

    fetch(`/get/${key}`).then(response => response.json()).then(data => {
        document.getElementById('response').innerText = JSON.stringify(data);
    });
});
