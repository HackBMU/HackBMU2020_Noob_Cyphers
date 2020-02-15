var mailInput = document.getElementById('usrnm');
var passInput = document.getElementById('psd');
var msg = document.querySelector('.msg');
var full = document.getElementById('form2');

full.addEventListener('submit',onsubmit);
function onsubmit(e){
    if(mailInput.value===''||passInput.value===''){
        msg.classList.add('msg-orange');
        msg.innerHTML='Please enter all fields';

        setTimeout(()=>msg.remove(),3000);
    }
}

