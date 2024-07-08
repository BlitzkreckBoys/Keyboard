let string = "";
let buttons = document.querySelectorAll('.button');



buttons.forEach(button => {
    button.addEventListener('click', (event) => {
        if (event.target.innerHTML == '=') {
            try {
                string = eval(string);
                document.querySelector('input').value = string;
            }catch (e) {
                alert('Invalid expression');
            }
        }
        else if (event.target.innerHTML == 'C') {
            string = '';
            document.querySelector('input').value = string;
        }

        else {
            string = string + event.target.innerText;
            document.querySelector('input').value = string;
        }
         
    });
});