// function typeKey(character) {
//     const output = document.getElementById('output');
//     output.innerText += character;

//  }
// function backspace() {
//     const output = document.getElementById('output');
//     output.innerText = output.innerText.slice(0, -1);
// }

// function space() {
//     const output = document.getElementById('output');
//     output.innerText  += "  ";
// }

// const buttons = document.querySelectorAll('.btn');
// const textarea = document.querySelectorAll('textarea');

// buttons.forEach(btn => {
//     btn.addEventListener('click', () => {
//         textarea.value += btn.innerText
//     });
// })

// const buttons = document.querySelectorAll('.btn')
const buttons = document.querySelectorAll('.key')
const textarea = document.querySelector('textarea')

const delete_btn = document.querySelector('.delete')
const space_btn = document.querySelector('.space')
const enter_btn = document.querySelector('.enter')

let chars = []

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        textarea.value += btn.innerText
        chars = textarea.value.split('')
    })
})

delete_btn.addEventListener('click', () => {
    chars.pop()
    textarea.value = chars.join('')
})

space_btn.addEventListener('click', () => {
    chars.push(' ')
    textarea.value = chars.join('')
})
enter_btn.addEventListener('click', () => {
    textarea.value += '\n'
    
});

