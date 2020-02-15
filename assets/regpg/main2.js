var mailInput = document.getElementById('eml');
var passInput = document.getElementById('psd');
var userInput = document.getElementById('usrnm');
var fnameInput = document.getElementById('fnm');
var lnameInput = document.getElementById('lnm');
var msg = document.querySelector('.msg');
var full = document.getElementById('form2');

full.addEventListener('submit',onsubmit);
function onsubmit(e){
    if(mailInput.value===''||passInput.value===''||userInput.value===''||fnameInput.value===''||lnameInput.value===''){
        msg.classList.add('msg-orange');
        msg.innerHTML='Please enter all fields';

        setTimeout(()=>msg.remove(),3000);
    }
}