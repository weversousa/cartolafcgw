let active = 1;

document.querySelector('#wrapperLiga').addEventListener('scroll', function (event) {
    document.querySelectorAll('#wrapperLiga .c-card').forEach(function (card) {
        if (card.getBoundingClientRect().x < 200) {
            active = card.getAttribute('posicao');
        }
    });
    document.querySelectorAll('#indicatorLiga > div > span').forEach(function (span) {
        if (span.getAttribute('posicao') == active) {
            span.classList.add('active');
        } else {
            span.classList.remove('active');
        }
    });
});

document.querySelector('#wrapperMes').addEventListener('scroll', function (event) {
    document.querySelectorAll('#wrapperMes .c-card').forEach(function (card) {
        if (card.getBoundingClientRect().x < 200) {
            active = card.getAttribute('posicao');
        }
    });
    document.querySelectorAll('#indicatorMes > div > span').forEach(function (span) {
        if (span.getAttribute('posicao') == active) {
            span.classList.add('active');
        } else {
            span.classList.remove('active');
        }
    });
});
