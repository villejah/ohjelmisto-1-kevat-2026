const trigger = document.querySelector('#trigger');
const target = document.querySelector('#target');

// Kun hiiri menee päälle
trigger.addEventListener('mouseover', () => {
    // Lisätään img/ polun alkuun
    target.src = 'img/picB.jpg';
});

// Kun hiiri poistuu
trigger.addEventListener('mouseout', () => {
    // Lisätään img/ polun alkuun
    target.src = 'img/picA.jpg';
});