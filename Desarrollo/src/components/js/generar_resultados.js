export function openModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos'));
    myModal.show();
}

export function cerrarModal() {
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos'));
    myModal.hide();
    
}
export function openModal2() {
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos2'));
    myModal.show();
}

export function cerrarModal2(){
    var myModal = new bootstrap.Modal(document.getElementById('modal_pesos2'));
    myModal.hide();
    
    
}
export function iniciarDespues(){
    var iniciar = new bootstrap.Modal(document.getElementById('modal_programar'))
    iniciar.show()
}

export function cerrarModalProgramar() {
        const modal = document.getElementById('modal_programar');
        const modalInstance = bootstrap.Modal.getInstance(modal);
        if (modalInstance) {
          modalInstance.hide();
        }
      }
      
    // Código para cerrar el modal
    //


const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastTrigger.addEventListener('click', () => {
    toastBootstrap.show()
    })
}
