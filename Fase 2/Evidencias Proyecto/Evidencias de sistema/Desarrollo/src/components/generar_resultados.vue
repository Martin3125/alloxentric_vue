<template>
    <link rel="stylesheet" href="src/assets/generar_resultados.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">

    <header>
      <div id="logo_header">
        <button class="toggle-btn" @click="toggleSidebar">
            <span class="icon" v-if="isCollapsed">☰</span>
            <span class="icon" v-else>✖</span>
        </button>
        <img src="@/assets/2.png" alt="logo">
        <h2>Alloxentric</h2>
      </div>
      <div class="input_search" >
        <input v-model="busqueda" type="search" placeholder="Buscar" />
        <i class="bi bi-search" id="search"></i>
      </div>
      <div class="card-body">
        <h5 class="card-title2">Usuario{{ usuarioLogueado }}</h5>
      </div>

      <div id="menu">
        <!-- Menu content can be added here -->
      </div>
    </header>

    <div class="main">
      <Menu_P v-if="!isCollapsed"/>
      <main id="cards"> 
        <div class="general">
          <div class="container">
            <div class="main-documentos">
              <div class="mb-3" id="select_documentos">
                <input class="form-control" type="file" @change="handleFileUpload" style="width: 100%;">
              </div>
            </div>
            <div class="main-procesamiento">
              <div class="lista-documentos">
                <h2 style="text-align: center;">Documentos subidos</h2>
                <br>
                <div v-for="(doc, index) in uploadedDocuments" :key="index" class="clear-doc">
                  <p>{{ doc.name }}</p>
                  <a href="#" @click.prevent="removeDocument(index)"><img src="@/assets/clear.png" alt=""></a>
                </div>
              </div>    
            </div>
              <!-- <div class="b_procesar">
              <button class="btn btn-primary" style="width: 100%;" @click="openModal()">Iniciar Ahora</button>
            </div>-->
            <!-- <div class="b_procesar">
              <button class="btn btn-primary" style="width: 100%;" @click="openModal2()">Iniciar Después</button>
            </div>  -->
            <div class="b_procesar">
                  <button class="btn btn-primary" style="width: 100%;" @click="openModal2()" >Iniciar Procesamiento</button>
                  <!-- Mensajes de Éxito y Error -->
                    <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
                    <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
              </div>
            <!-- <div class="b_procesar">
              <button class="btn btn-primary" style="width: 100%;" @click="iniciarDespues()">Iniciar Después</button>
            </div>  -->            
          </div>
        </div>
      </main>
          
        
  <!-- ------------------------Modal de Iniciar Después------------------------------------------------ -->
      <div class="modal" tabindex="-1" id="modal_pesos2">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <p>¿Quiere modificar los pesos de sus acciones de cobranza?</p>
            </div>
            <div class="modal-footer">
              <a class="btn btn-secondary" href="/cobranza">SI</a>
              <a class="btn btn-primary" data-bs-dismiss="modal" type="submit" @click="iniciarDespues()">NO</a>
            </div>
          </div>
        </div>
      </div>
  <!-- ------------------------Modal de Programar procesamiento------------------------------------------------ -->
      <div class="modal" tabindex="-1" id="modal_programar">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h2 style="text-align: center;">Programar procesamiento</h2>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="padding: 10%;">
              <form @submit.prevent="g_resultados">
                <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                  <input v-model="nombre" class="form-control" type="text" name="nombre_procesamiento" placeholder="Nombre del procesamiento">
                </div>
                <br>
                <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                  <input v-model="fecha" class="form-control" type="date" name="fecha_procesamiento">
                </div>
                <br>
                <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                  <input v-model="hora" class="form-control" type="time" name="hora_procesamiento">
                </div>
                <br>
                <div class="btn_despues" style="margin: auto; display: flex; justify-content: center;">
                  <button type="submit"  data-bs-dismiss="modal" style="width: 40%;" @click="uploadFile">Confirmar</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
  <!-- ------------------------Modal de Iniciar procesamiento------------------------------------------------ -->
      <div class="modal" tabindex="-1" id="modal_pesos">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <p>¿Quiere modificar los pesos de sus acciones de cobranza?</p>
            </div>
            <div class="modal-footer">
              <a class="btn btn-secondary" href="/cobranza">SI</a>
              <a class="btn btn-primary"  type="submit" @click="uploadFile">NO</a>
              <!-- href="/resultados" -->
            </div>
          </div>
        </div>
      </div>
    </div>    
    <!-- ------------------------Mensaje de Iniciando Procesamiento------------------------------------------------ -->

    <div class="toast-container position-fixed bottom-0 end-0 p-3">
      <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <strong class="me-auto">Iniciando Procesamiento</strong>
          <small>11 mins ago</small>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
          El archivo está siendo procesado. Esto puede tardar unos minutos.
        </div>
      </div>
    </div>

</template>

<script>
import { openModal, openModal2, cerrarModal, cerrarModal2, cerrarModalProgramar, iniciarDespues } from './js/generar_resultados.js';
import Menu_P from './Menu-.vue';
import bootstrap from'bootstrap/dist/js/bootstrap.bundle.min.js';
import axios from 'axios';



export default {
  name: 'generar_resultados',
  components: {
    Menu_P,
  },
  data() {
    return {
      nombre: '',
      fecha: '',
      hora: '',
      file: null,
      uploadedDocuments: [],
      predictions: [],  // Cambia a un array para manejar múltiples predicciones
      isCollapsed: true,
      successMessage: '',
      errorMessage: ''
    };
  },
  methods: {
    openModal,
    closeModal() {
      this.isModalOpen = false;
      this.nombre = '';
      this.fecha = '';
      this.hora = '';
    },
    cerrarModal,
    openModal2,
    cerrarModal2,
    iniciarDespues,
    cerrarModalProgramar,
    handleFileUpload(event) {
      this.file = event.target.files[0];
      if (this.file) {
        this.uploadedDocuments.push(this.file);
      }
    },
    removeDocument(index) {
      this.uploadedDocuments.splice(index, 1);
    },
    async g_resultados() {
      try {
        // Enviar datos al backend para crear un nuevo procesamiento
        await axios.post('http://localhost:8000/api/procesamiento_P', {
          nombre: this.nombre,
          fecha: this.fecha,
          hora: this.hora
        });
        this.successMessage = 'Procesamiento registrado exitosamente';
        this.clearMessages();
        this.closeModal();
        this.fetchProcesamientos(); // Refrescar la lista de procesamientos
      } catch (error) {
        console.error("Error al programar el procesamiento:", error);
        this.errorMessage = 'Error al programar el procesamiento:';
        this.clearMessages();
      }
    },
    async fetchProcesamientos() {
      try {
        // Obtener la lista de procesamientos programados desde el backend
        const response = await axios.get('http://localhost:8000/api/procesamiento_P');
        this.procesamientos = response.data;
      } catch (error) {
        console.error("Error al obtener procesamientos:", error);
        this.errorMessage = 'Error al obtener procesamientos:';
        this.clearMessages();
      }
    },
    async deleteProcesamiento(procesamientoId) {
      try {
        // Eliminar un procesamiento programado por ID
        await axios.delete(`http://localhost:8000/api/procesamiento_P/${procesamientoId}`);
        this.successMessage = 'Procesamiento eliminado exitosamente';
        this.fetchProcesamientos(); // Refrescar la lista después de eliminar
        this.clearMessages();
      } catch (error) {
        console.error("Error al eliminar procesamiento:", error);
        this.errorMessage = 'Error al eliminar procesamiento';
        this.clearMessages();
      }
    },
    async uploadFile() {
      if (!this.file) {
        // alert('Por favor, selecciona un archivo para subir.');
        this.successMessage ='Por favor, selecciona un archivo para subir.';
        this.clearMessages();
        // Cerrar el modal si la carga fue exitosa
        this.closeModal2();
        return;
      }
      
      const formData = new FormData();
      formData.append('file', this.file);
      const toastLiveExample = document.getElementById('liveToast');
      const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
      toastBootstrap.show();

      try {
        const response = await fetch('http://127.0.0.1:8000/api/upload', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          const errorData = await response.json();
          console.error('Error en la respuesta:', errorData);
          alert('Error al subir el archivo: ' + (errorData.detail || 'Error desconocido'));
        } else {
          const data = await response.json();
          console.log('Resultados de predicción:', data);

          // Asegúrate de que la estructura de data sea correcta
          if (data.status === 'success' && data.predicciones) {
            this.predictions = data.predicciones; // Almacena las predicciones
            localStorage.setItem('predicciones', JSON.stringify(this.predictions)); // Guarda en local storage
            this.$router.push('/resultados'); // Redirige a resultados.vue
            
          } else {
            console.log('No se encontraron predicciones.');
          }
        }
      } catch (error) {
        console.error('Error en la solicitud:', error);
      }
    },
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
    clearMessages() {
      setTimeout(() => {
        this.successMessage = '';
        this.errorMessage = '';
      }, 5000);
    },
    mounted() {
    // Cargar los procesamientos cuando el componente se monta
    this.fetchProcesamientos();
  }
  }
};
</script>

<style>
/* Agrega estilos para darle formato a la tabla o a la página */
table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid black;
padding: 8px;
text-align: center;
}
.input_search input {
border-radius: 30px;
width: 40%;
outline: none;
padding: 10px 20px;
border: 1px solid #c9c9c9;
box-sizing: border-box;
padding-right: 50px;
margin-left: 15%;
}
.card-title2{
  display: flex;
  justify-content:center;
  margin: auto;
  font-weight: 600;

}

</style>