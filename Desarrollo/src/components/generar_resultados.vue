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
            
          </div>

          <div class="b_procesar">
            <button class="btn btn-primary" style="width: 100%;" @click="openModal()">Iniciar Ahora</button>
          </div>
          <div class="b_procesar">
            <button class="btn btn-primary" style="width: 100%;" @click="openModal2()">Iniciar Después</button>
          </div>
          <div class="b_procesar">
            <button class="btn btn-primary" style="width: 100%;" @click="uploadFile">Iniciar Procesamiento</button>
        </div>

        <!-- Sección para mostrar los resultados de la predicción -->
        <div v-if="predictions.lstm_prediction && predictions.kmeans_prediction" class="predictions">
            <h3>Resultados de la Predicción</h3>
            <p><strong>Predicción LSTM:</strong> {{ predictions.lstm_prediction }}</p>
            <p><strong>Predicción K-Means:</strong> {{ predictions.kmeans_prediction }}</p>
        </div>
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

    

  </template>
  
  <script>
  import { openModal, openModal2, cerrarModal, cerrarModal2, cerrarModalProgramar, iniciarDespues } from './js/generar_resultados.js';
  import Menu_P from './Menu-.vue';
  
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
        predictions: {},  // Para almacenar las predicciones
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
        const response = await fetch('http://127.0.0.1:8000/api/upload', {  // Ajusta la ruta si es necesario
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
            // Aquí puedes manejar los resultados de la predicción
            this.predictions = data;
            this.$router.push('/generar_resultados');
          }
        } catch (error) {
          console.error('Error en la solicitud:', error);
        }
      },
      async g_resultados() {
        try {
          const userData = {
            nombre: this.nombre,
            fecha: this.fecha,
            hora: this.hora
          };
          const respuesta = await fetch('http://127.0.0.1:8000/api/procesamiento_P', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
          });
  
          if (!respuesta.ok) {
            const errorData = await respuesta.json();
            console.error('Error en la respuesta:', errorData);
            this.errorMessage = errorData.detail || 'Error en el registro';
          } else {
            const data = await respuesta.json();
            console.log(data);
            this.cerrarModalProgramar();
            this.$router.push('/generar_resultados'); // Aquí puedes redirigir al usuario o limpiar el formulario
          }
        } catch (error) {
          console.error('Error en la solicitud:', error);
        }
      }
    }
  };
  </script>
  