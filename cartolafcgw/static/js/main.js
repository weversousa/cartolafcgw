// document.querySelectorAll('input[name="posicao"]').forEach(input => {
//     input.addEventListener('change', () => {
//         document.querySelectorAll('label').forEach(label => {
//             if (input.id === label.getAttribute('for')) {
//                 label.classList.add('check');
//             } else {
//                 label.classList.remove('check');
//             }
//         });
//     });
//     // console.log(input.checked)
// });


const wrapper = document.querySelector('section.wrapper');
let pressed = false
let startX = 0;

wrapper.addEventListener('mousedown', function (event) {
    pressed = true;
    startX = event.clientX;
    this.style.cursor = 'grabbing';
});

wrapper.addEventListener('mouseleave', function (event) {
    pressed = false;
});

wrapper.addEventListener('mouseup', function (event) {
    pressed = true;
    this.style.cursor = 'grab';
});

wrapper.addEventListener('mousemove', function (event) {
    if (!pressed) {
        return
    }
    this.scrollLeft += startX - event.clientX;
});