document.getElementById('ocrForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const filename = document.getElementById('filename').value;
    const extractedText = document.getElementById('extractedText').value;

    const response = await fetch('/ocr/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filename, extracted_text: extractedText }),
    });

    const result = await response.json();
    alert(result.message);
});

document.getElementById('ragForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const queryText = document.getElementById('ragQuery').value;

    const response = await fetch('/rag/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: queryText }),
    });

    const result = await response.json();
    alert(`Response: ${result.response}`);
});

document.getElementById('getAlerts').addEventListener('click', async () => {
    const response = await fetch('/alerts');
    const alerts = await response.json();

    const alertsList = document.getElementById('alertsList');
    alertsList.innerHTML = '';
    alerts.forEach(alert => {
        const li = document.createElement('li');
        li.textContent = `ID: ${alert.id}, Issue: ${alert.issue}, Red Alert: ${alert.red_alert}`;
        alertsList.appendChild(li);
    });
});
