<template>
    <link rel="stylesheet" href="src\assets\cargar_resultados_periodo_anterior.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
<body>
    <header>
        <div id="logo_header">
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>

        <div id="menu">
        </div>
        
    </header>
    

</body>
    <div class="main">
        <Menu_P  />
            <div class="general">
                <div id="arriba">
                    <div class="card-body"  id="Titulo1" >
                        <h5 class="card-title1">Cargar resultados</h5>
                    </div>
                    <div class="card-body" id="usuario">
                        <h5 class="card-title2">Usuario</h5>
                    </div>
                </div>
                <div class="resultados">
                    <div class="main-resultados">
                        <div class="mb-3" id="select_resultados">
                            <!-- <input   id="formFile" style="width: 100%;"> -->
                             <!-- Crear un nuevo directorio -->
                             <div class="create-directory d-flex align-items-center mb-3">
                                <input v-model="nuevoDirectorio" class="form-control" placeholder="Nuevo Directorio" id="formFile" style="width: 100%; margin-right: 10px;" />
                                <button @click="crearDirectorio" class="btn btn-success" id="formFile">Crear</button>
                            </div>

                        </div>
                    </div>
                    <div class="main-directorios">    
                        <div class="lugar">
                            <div class="home">
                                <h3 style="color: white; text-align: center;">Home</h3>
                            </div>
                            <div class="dir">
                                <h3 style="color: white; text-align: center;">Directorios</h3>
                            </div>     
                        </div>
                            <div class="main-content">
                                <!-- Sidebar para directorios -->
                                <aside class="sidebar" style="max-height: 300px; overflow-y: auto;">
                                    <h2>Directorios</h2>
                                    <ul class="directory-list">
                                        <li v-for="directory in directories" :key="directory" 
                                            :class="{ active: directory === selectedDirectory }" 
                                            @click="selectDirectory(directory)">
                                            {{ directory }}
                                            <button @click.stop="eliminarDirectorio(directory)" class="delete-btn">❌</button>
                                        </li>
                                    </ul>
                                </aside>

                                <!-- Contenido principal: archivos del directorio -->
                                <section class="file-section" style="max-height: 300px; overflow-y: auto;">
                                    <h2>Archivos en {{ selectedDirectory || '...' }}</h2>
                                    <ul v-if="selectedDirectory" class="file-list">
                                        <li v-for="file in currentFiles" :key="file" @click="verArchivo(file)">
                                            {{ file }}
                                        </li>
                                    </ul>
                                    
                                    <!-- Subir archivo si hay un directorio seleccionado -->
                                    <div v-if="selectedDirectory" class="upload-section">
                                        <input type="file" @change="onFileChange" />
                                        <button @click="subirArchivo" class="upload-btn">Subir Archivo</button>
                                    </div>
                                </section>
                            </div>
                        </div>
                        <div class="b_confirmar">
                            <a id="guardar" type="submit" class="btn btn-primary" href="/res_periodo_anterior">Confirmar</a>
                        </div>  
                    </div>
            </div>  
        </div>
</template>

<script>
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
  name: 'cargar_resultados',
  components: {
    Menu_P,
  },
  data() {
    return {
      directories: [],
      selectedDirectory: null,
      currentFiles: [],
      nuevoDirectorio: '',
      contenidoArchivo: '',
      archivo: null,  // Archivo seleccionado para subir
    };
  },
  methods: {
    async fetchDirectories() {
      try {
        const response = await axios.get('http://localhost:8000/directorios');
        this.directories = response.data;
      } catch (error) {
        console.error("Error al obtener directorios:", error);
      }
    },
    async selectDirectory(directory) {
      this.selectedDirectory = directory;
      try {
        const response = await axios.get(`http://localhost:8000/directorios/${directory}/archivos`);
        this.currentFiles = response.data;
      } catch (error) {
        console.error("Error al obtener archivos del directorio:", error);
      }
    },
    async crearDirectorio() {
      if (!this.nuevoDirectorio) {
        alert("Por favor ingrese el nombre del directorio.");
        return;
      }
      
      try {
        const response = await axios.post('http://localhost:8000/directorios', {
          nombre_directorio: this.nuevoDirectorio
        });
        if (response.status === 200) {
        // Suponiendo que el servidor devuelve el nombre del directorio creado
        alert("Directorio creado exitosamente: " + response.data.nombre_directorio);
    }
        alert("Directorio creado exitosamente: " + this.nuevoDirectorio);
        this.fetchDirectories();
        this.nuevoDirectorio = '';
      } catch (error) {
        console.error("Error al crear directorio:", error);
        alert("Error al crear el directorio: " + error.response.data.detail);
      }
    },
    async eliminarDirectorio(directory) {
      if (!confirm(`¿Seguro que deseas eliminar el directorio: ${directory}?`)) {
        return;
      }
      
      try {
        await axios.delete(`http://localhost:8000/directorios/${directory}`);
        alert("Directorio eliminado exitosamente.");
        this.fetchDirectories();
      } catch (error) {
        console.error("Error al eliminar el directorio:", error);
        alert("Error al eliminar el directorio.");
      }
    },
    onFileChange(event) {
      this.archivo = event.target.files[0];  // Guardar el archivo seleccionado
    },
    async subirArchivo() {
      if (!this.archivo || !this.selectedDirectory) {
        alert("Seleccione un archivo y un directorio antes de subir.");
        return;
      }
      
      const formData = new FormData();
      formData.append("file", this.archivo);

      try {
        await axios.post(`http://localhost:8000/directorios/${this.selectedDirectory}/subir_archivo`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        alert("Archivo subido exitosamente.");
        this.selectDirectory(this.selectedDirectory);  // Recargar archivos del directorio
        this.archivo = null;  // Limpiar archivo seleccionado
      } catch (error) {
        console.error("Error al subir archivo:", error);
        alert("Error al subir archivo.");
      }
    },
    async verArchivo(file) {
      try {
        const response = await axios.get(`http://localhost:8000/directorios/${this.selectedDirectory}/archivos/${file}`);
        this.contenidoArchivo = response.data.contenido;
      } catch (error) {
        console.error("Error al ver el archivo:", error);
        alert("Error al ver el archivo.");
      }
    },
    cerrarModalArchivo() {
      this.contenidoArchivo = '';  // Cerrar modal
    },
    confirmar() {
      alert("Resultados confirmados.");
    },
  },
  mounted() {
    this.fetchDirectories();
  }
};

</script>
<style>
/* Estilos generales */
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.app-header {
  background-color: #007bff;
  color: white;
  padding: 1rem;
  text-align: center;
}

.main-content {
  display: flex;
  flex: 1;
}

.sidebar {
  background-color: #f8f9fa;
  padding: 1rem;
  width: 250px;
}

.directory-list {
  list-style: none;
  padding: 0;
}

.directory-list li {
  cursor: pointer;
  padding: 0.5rem;
  border-bottom: 1px solid #ddd;
}

.directory-list li.active {
  background-color: #007bff;
  color: white;
}

.delete-btn {
  background: none;
  border: none;
  color: red;
  float: right;
  cursor: pointer;
}

.create-directory {
  margin-top: 1rem;
}

.create-btn {
  background-color: #007bff;
  color: white;
  padding: 0.5rem;
  border: none;
  cursor: pointer;
}

.file-section {
  flex: 1;
  padding: 1rem;
}

.file-list {
  list-style: none;
  padding: 0;
}

.file-list li {
  cursor: pointer;
  padding: 0.5rem;
  border-bottom: 1px solid #ddd;
}

.upload-section {
  margin-top: 1rem;
}

.upload-btn {
  background-color: #28a745;
  color: white;
  padding: 0.5rem;
  border: none;
  cursor: pointer;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 5px;
  width: 80%;
  max-width: 600px;
}

.modal-content pre {
  background-color: #f8f9fa;
  padding: 1rem;
  border-radius: 5px;
  white-space: pre-wrap;
}

.modal-content button {
  background-color: #007bff;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  cursor: pointer;
}
.sidebar, .file-section {
    max-height: 300px;
    overflow-y: auto;
}

.directory-list, .file-list {
    list-style: none;
    padding: 0;
}

.directory-list li, .file-list li {
    margin: 5px 0;
    padding: 8px;
    cursor: pointer;
}

.directory-list li.active {
    background-color: #20a82b;
    font-weight: bold;
}

</style>


