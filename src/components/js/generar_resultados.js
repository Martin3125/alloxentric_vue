function openModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos'));
    myModal.show();
}

function cerrarModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos'));
    myModal.hide();
    
}
function openModal2() {
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos2'));
    myModal.show();
}

function cerrarModal2(){
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos2'));
    myModal.hide();
    
}
function iniciarDespues(){
    var iniciar = new bootstrap.Modal(document.getElementById('modal_programar'))
    iniciar.show()
}

function cerrarModalProgramar() {
    var iniciar = new bootstrap.Modal(document.getElementById('modal_programar'))
    iniciar.hide()
}
