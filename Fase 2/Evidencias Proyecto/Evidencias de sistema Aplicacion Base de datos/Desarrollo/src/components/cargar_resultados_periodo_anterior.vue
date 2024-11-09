<template>
    <link rel="stylesheet" href="src\assets\cargar_resultados_periodo_anterior.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
<body>
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
        </div>
        
    </header>
    

</body>
    <div class="main">
      <Menu_P v-if="!isCollapsed"/>
      <main id="cards">
            <div class="general">
                <div class="container">
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
                          <!-- Botón para cargar resultados -->
                            <a id="guardar" type="submit" class="btn btn-primary" href="/res_periodo_anterior">Confirmar</a>
                        </div>  
                        <!-- Sección de resultados -->
                        <div v-if="resultados.length > 0" class="resultados-section">
                          <h2>Resultados del procesamiento: {{ selectedFile }}</h2>
                          <ul>
                            <li v-for="(resultado, index) in resultados" :key="index">
                              {{ resultado }}
                            </li>
                          </ul>
                        </div>
                    </div>
            </div>
          </main>
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
      usuarioLogueado: '', // Ejemplo de usuario logueado
      resultados: [],
      directories: [],
      selectedDirectory: null,
      currentFiles: [],
      nuevoDirectorio: '',
      contenidoArchivo: '',
      archivo: null,  // Archivo seleccionado para subir
      isCollapsed: true,
      busqueda: '', // Campo para la búsqueda
      selectedDirectoryToLoad: null, // Directorio seleccionado para cargar resultados
      resultadosCargados: [], // Resultados cargados del periodo anterior
      directorios: [], // Directorios disponibles
      procesamientos: [], // Lista de procesamientos
      directorioSeleccionado: "", // Directorio seleccionado
      procesamientoSeleccionado: "", // Procesamiento seleccionado
    };
  },
  methods: {
    //Obtener los directorios disponibles
    async obtenerDirectorios() {
      try {
        const response = await fetch('/api/directorios');
        const data = await response.json();
        this.directorios = data.directorios;
      } catch (error) {
        console.error('Error al obtener directorios:', error);
      }
    },

    // Obtener los procesamientos disponibles para un directorio seleccionado
    async obtenerProcesamientos() {
      if (this.directorioSeleccionado) {
        try {
          const response = await fetch(`/api/procesamientos/${this.directorioSeleccionado}`);
          const data = await response.json();
          this.procesamientos = data.procesamientos;
        } catch (error) {
          console.error('Error al obtener procesamientos:', error);
        }
      }
    },

    // Cargar los resultados del procesamiento seleccionado
    async cargarResultados() {
      if (this.directorioSeleccionado && this.procesamientoSeleccionado) {
        try {
          const response = await fetch(`/api/resultados/${this.directorioSeleccionado}/${this.procesamientoSeleccionado}`);
          const data = await response.json();
          this.resultados = data.resultados;
        } catch (error) {
          console.error('Error al cargar resultados:', error);
        }
      }
    },
    // Función para cargar los directorios disponibles
    async cargarDirectorios() {
      try {
        const response = await axios.get("http://localhost:8000/directorios");
        this.directorios = response.data; // Almacenar los directorios en el arreglo
      } catch (error) {
        console.error("Error al cargar los directorios:", error);
        alert("Error al cargar los directorios.");
      }
    },

    // Función para cargar los resultados del periodo anterior
    async cargarResultadosPeriodoAnterior() {
      if (!this.selectedDirectoryToLoad) {
        alert("Por favor seleccione un directorio para cargar los resultados del periodo anterior.");
        return;
      }
      try {
        const response = await axios.get(`http://localhost:8000/resultados_periodo_anterior/${this.selectedDirectoryToLoad}`);
        this.resultadosCargados = response.data; // Almacenar los resultados en el arreglo
        alert("Resultados del periodo anterior cargados exitosamente.");
      } catch (error) {
        console.error("Error al cargar resultados del periodo anterior:", error);
        alert("Error al cargar resultados del periodo anterior.");
      }
    },
    // Obtener lista de directorios
    async fetchDirectories() {
      try {
        const response = await axios.get('http://localhost:8000/directorios');
        this.directories = response.data;
      } catch (error) {
        console.error("Error al obtener directorios:", error);
      }
    },
    // Seleccionar un directorio y obtener sus archivos
    async selectDirectory(directory) {
      this.selectedDirectory = directory;
      try {
        const response = await axios.get(`http://localhost:8000/directorios/${directory}/archivos`);
        this.currentFiles = response.data;
      } catch (error) {
        console.error("Error al obtener archivos del directorio:", error);
      }
    },
    // Crear un nuevo directorio
    async crearDirectorio() {
      if (!this.nuevoDirectorio) {
        alert("Por favor ingrese el nombre del directorio.");
        return;
      }
      try {
        const response = await axios.post('http://localhost:8000/directorios', {
          nombre_directorio: this.nuevoDirectorio
        });
        alert("Directorio creado exitosamente: " + response.data.nombre_directorio);
        this.fetchDirectories();
        this.nuevoDirectorio = '';
      } catch (error) {
        console.error("Error al crear directorio:", error);
        alert("Error al crear el directorio.");
      }
    },
    // Eliminar un directorio
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
    // Manejar la selección de archivos para subir
    onFileChange(event) {
      this.archivo = event.target.files[0];
    },
    // Subir archivo al directorio seleccionado
    async subirArchivo() {
      if (!this.archivo || !this.selectedDirectory) {
        alert("Seleccione un archivo y un directorio antes de subir.");
        return;
      }
      const formData = new FormData();
      formData.append("file", this.archivo);
      try {
        await axios.post(`http://localhost:8000/directorios/${this.selectedDirectory}/subir_archivo`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        alert("Archivo subido exitosamente.");
        this.selectDirectory(this.selectedDirectory);  // Recargar archivos del directorio
        this.archivo = null;  // Limpiar archivo seleccionado
      } catch (error) {
        console.error("Error al subir archivo:", error);
        alert("Error al subir archivo.");
      }
    },
    // Ver contenido de un archivo
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
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
  },
  mounted() {
    this.fetchDirectories();
    this.cargarDirectorios(); 
    this.obtenerDirectorios();
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


