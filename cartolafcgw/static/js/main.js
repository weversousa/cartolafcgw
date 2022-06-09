
document.querySelectorAll('input[name="posicao"]').forEach(input => {
    input.addEventListener('change', () => {
        document.querySelectorAll('label').forEach(label => {
            if (input.id === label.getAttribute('for')) {
                label.classList.add('check');
            } else {
                label.classList.remove('check');
            }
        });
    });
    // console.log(input.checked)
});