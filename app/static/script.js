function addNumberFields() {
    const numCount = document.getElementById('num_count').value;
    const numbersDiv = document.getElementById('numbers');
    numbersDiv.innerHTML = '';
    for (let i = 0; i < numCount; i++) {
        const label = document.createElement('label');
        label.textContent = `กรุณากรอกตัวเลขที่ ${i + 1}: `;
        label.className = 'form-label';
        const input = document.createElement('input');
        input.type = 'number';
        input.name = `num${i + 1}`;
        input.className = 'form-control mb-2';
        input.required = true;
        numbersDiv.appendChild(label);
        numbersDiv.appendChild(input);
    }
}