'use strict';

function fun(f) {
    console.log('I am in the land of fun')
    f()
    console.log('Now back to reality')
}

//function ff() {
//  console.log('This is function ff')
//}


fun( () => {console.log('This is my first arrow function')})
fun( () => {console.log('This is my second arrow function')})


let n = 0
function baby () {
    document.querySelector( '#metropuli').innerHTML = `Hello, my ${n++} HTML page!`
}
let interval = setInterval(baby, 1000);
//set time or setInterval (BOM)



const button1 = document.getElementById('btn1');
button1.addEventListener('click', () => {clearInterval(interval)});

const button2 = document.getElementById('btn2');
button2.addEventListener('click', () => {interval = setInterval(baby, 1000 )});