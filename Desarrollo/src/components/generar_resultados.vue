<template>
    <div id="app">
      <link rel="stylesheet" href="src/assets/generar_resultados.css">
      <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
  
      <header>
        <div id="logo_header">
          <img src="@/assets/2.png" alt="logo">
          <h2>Alloxentric</h2>
        </div>
        <div id="menu">
          <!-- Menu content can be added here -->
        </div>
      </header>
  
      <div class="main">
        <Menu_P />
        <div class="general">
          <div class="general-resultados">
            <div class="pag-resultados">
              <h5 style="margin-top: 3%;">Generar resultados</h5>
            </div>
  
            <div class="user">
              <h5 style="margin-top: 3%;">Usuario</h5>
            </div>
          </div>
  
          <div class="resultados">
          <div class="main-documentos">
            <div class="mb-3" id="select_documentos">
              <input class="form-control" type="file" @change="handleFileUpload" style="width: 100%;">
            </div>

            <div class="mb-3" id="btn_documentos">
              <button type="submit" id="btn_documentos" class="btn btn-secondary" style="width: 100%; background-color: black;" @click="uploadFile">Subir</button>
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
            <div class="b_procesar">
                <button class="btn btn-primary" style="width: 100%;" @click="uploadFile">Iniciar Procesamiento</button>
            </div>
                
          </div>

          <!-- <div class="b_procesar">
            <button class="btn btn-primary" style="width: 100%;" @click="openModal()">Iniciar Ahora</button>
          </div>
          <div class="b_procesar">
            <button class="btn btn-primary" style="width: 100%;" @click="openModal2()">Iniciar Después</button>
          </div> -->
          
        </div>
      </div>
    </div>
  
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
              <a class="btn btn-primary" type="submit" @click="iniciarDespues()">NO</a>
            </div>
          </div>
        </div>
      </div>
  
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
                  <button type="submit" class="btn btn-success" style="width: 40%;">Confirmar</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
  
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
              <a class="btn btn-primary" href="/resultados" type="submit">NO</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
    <h1>Predicción de Acciones de Deudores</h1>

    <form @submit.prevent="getPredictions">
      <!-- Puedes añadir campos para cargar datos si es necesario -->
      <button type="submit">Obtener Predicciones</button>
    </form>

    <div v-if="predictions.length">
      <h2>Resultados de Predicción</h2>
      <table>
        <thead>
          <tr>
            <th>Acción Predicha</th>
            <th>Deudores</th>
            <th>Total Deudores</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in predictions" :key="index">
            <td>{{ item.accion_predicha }}</td>
            <td>{{ item.deudores }}</td>
            <td>{{ item.total_deudores }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

    

  </template>
  
  <script>
  import { openModal, openModal2, cerrarModal, cerrarModal2, cerrarModalProgramar, iniciarDespues } from './js/generar_resultados.js';
  import Menu_P from './Menu-.vue';
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
      };
    },
    methods: {
      openModal,
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
      async uploadFile() {
        if (!this.file) {
          alert('Por favor, selecciona un archivo para subir.');
          return;
        }
        const formData = new FormData();
        formData.append('file', this.file);
  
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
</style>