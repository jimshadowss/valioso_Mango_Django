// Importing 'crypto' module
function hashear(string) {

    let hash = 0;

    if (string.length == 0) return hash;

    for (i = 0; i < string.length; i++) {
        char = string.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }

    return hash;
}



users=['lucas']
passwds=[hashear('pass')]






document.querySelector('#enviarr').addEventListener('click',(e)=>{
    e.preventDefault();
    let user=document.querySelector('#nombree');
    let pass=hashear(document.querySelector('#passwordd').value);
    if (users.includes(user.value)&&passwds.includes(pass)){
        window.location.href="mi_tienda";
    }else{
        document.write('Contraseña incorrecta');
    }
})