function typeKey(character) {
    const output = document.getElementById('output');
    output.innerText += character;

}
function backspace() {
    const output = document.getElementById('output');
    output.innerText = output.innerText.slice(0, -1);
}

function space() {
    const output = document.getElementById('output');
    output.innerText  += "  ";
}


