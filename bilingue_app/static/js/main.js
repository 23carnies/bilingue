let engFront = document.getElementById('flipMe')
let engBack = document.getElementById('backEng')
let spanFront = document.getElementById('spanFlip')
let spanBack = document.getElementById('flipBackSpan')

function flip() {
    engFront.classList.add('flipped');
}
function flipBackEng() {
    engBack.classList.add('flipped');
}
function flipSpan() {
    spanFront.classList.add('flipped');
}
function flipBackSpan() {
    spanBack.classList.add('flipped');
}