<template>
   <link rel="stylesheet" href="src\assets\Inicio.css">
   <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
   <header>
    <div id="logo_header">
      <img src="@/assets/2.png" alt="logo" />
      <h2>Alloxentric</h2>
    </div>
    <div id="menu"></div>
  </header>

  <div class="my-component">
    <div id="general">
      <Menu_P />
      <main id="cards">
        <div id="arriba">
          <div class="input_search" id="Titulo2">
            <input v-model="busqueda" type="search" placeholder="Buscar" />
            <i class="bi bi-search" id="search"></i>
          </div>
          <div class="card-body" id="usuario">
            <h5 class="card-title2">Usuario</h5>
          </div>
        </div>

        <div id="bodycard">
          <div class="container">
            <div class="table_header">
              <h2>Últimos archivos subidos</h2>
              <select v-model="itemsPerPage" @change="updatePagination">
                <option value="5">5 filas</option>
                <option value="10">10 filas</option>
                <option value="20">20 filas</option>
              </select>
            </div>

            <table id="documentTable">
              <thead>
                <tr>
                  <th>Archivos</th>
                  <th>Fechas</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="archivo in paginatedArchivos" :key="archivo.Id_archivo">
                  <td>{{ archivo.nombre }}</td>
                  <td>{{ archivo.fecha }}</td>
                </tr>
              </tbody>
            </table>

            <div class="pagination">
              <button @click="prevPage" :disabled="currentPage === 1">Anterior</button>
              <span>Página {{ currentPage }} de {{ totalPages }}</span>
              <button @click="nextPage" :disabled="currentPage === totalPages">Siguiente</button>
            </div>
          </div>

          <div class="container2">
            <div class="table_header">
              <h2>Procesamientos programados</h2>
              <select v-model="itemsPerPage" @change="updatePagination">
                <option value="5">5 filas</option>
                <option value="10">10 filas</option>
                <option value="20">20 filas</option>
              </select>
            </div>

            <table id="documentTable">
              <thead>
                <tr>
                  <th>Nombre del procesamiento</th>
                  <th>Fechas</th>
                  <th>Hora</th>
                  <th>Cancelar</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="procesamiento in paginatedProcesamientos" :key="procesamiento.Id_procesamiento">
                  <td>{{ procesamiento.nombre }}</td>
                  <td>{{ procesamiento.fecha }}</td>
                  <td>{{ procesamiento.hora }}</td>
                  <td>
                    <i class="bi bi-pencil-square" @click="editarResultado(procesamiento)"></i>
                    <i class="bi bi-trash" @click="deleteProcesamiento(procesamiento.Id_procesamiento)"><img src="@/assets/clear.png" alt=""></i>
                  </td>
                </tr>
              </tbody>
            </table>

            <div class="pagination">
              <button @click="prevPage" :disabled="currentPage === 1">Anterior</button>
              <span>Página {{ currentPage }} de {{ totalPages }}</span>
              <button @click="nextPage" :disabled="currentPage === totalPages">Siguiente</button>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>


<script>
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
  name: 'Inicio-',
  components: { Menu_P },
  data() {
    return {
      busqueda: "",
      archivos: [],
      procesamientos: [],
      itemsPerPage: 5,
      currentPage: 1,
      maxVisiblePages: 5,
    };
  },
  computed: {
    filteredArchivos() {
      return this.archivos.filter((archivo) => archivo.nombre.toLowerCase().includes(this.busqueda.toLowerCase()));
    },
    filteredProcesamientos() {
      return this.procesamientos.filter((procesamiento) => procesamiento.nombre.toLowerCase().includes(this.busqueda.toLowerCase()));
    },
    paginatedArchivos() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.filteredArchivos.slice(start, start + this.itemsPerPage);
    },
    paginatedProcesamientos() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.filteredProcesamientos.slice(start, start + this.itemsPerPage);
    },
    totalPages() {
      return Math.ceil(this.filteredArchivos.length / this.itemsPerPage);
    },
    visiblePages() {
      const start = Math.max(1, this.currentPage - Math.floor(this.maxVisiblePages / 2));
      const end = Math.min(this.totalPages, start + this.maxVisiblePages - 1);
      return Array.from({ length: end - start + 1 }, (_, i) => start + i);
    }

  },
  methods: {
    async getArchivos() {
      try {
        const response = await axios.get('http://localhost:8000/api/inicio');
        this.archivos = response.data;
      } catch (error) {
        console.error("Error al obtener los archivos:", error);
      }
    },
    async getProcesamientos() {
      try {
        const response = await axios.get('http://localhost:8000/api/procesamiento_P');
        this.procesamientos = response.data;
      } catch (error) {
        console.error("Error al obtener los procesamientos:", error);
      }
    },
    updatePagination() {
      this.currentPage = 1;
    },
    prevPage() {
      if (this.currentPage > 1) this.currentPage--;
    },
    nextPage() {
      if (this.currentPage < this.totalPages) this.currentPage++;
    },
    goToPage(page) {
      if (page > 0 && page <= this.totalPages) {
        this.currentPage = page;
      }
    },
    async deleteProcesamiento(procesamiento_id) {
      try {
        await axios.delete(`http://localhost:8000/api/procesamiento_P/${procesamiento_id}`);
        this.procesamientos = this.procesamientos.filter((p) => p.Id_procesamiento !== procesamiento_id);
      } catch (error) {
        console.error("Error al eliminar el procesamiento:", error);
      }
    },
  },
  mounted() {
    this.getArchivos();
    this.getProcesamientos();
  },
};
</script>

<style>
.table-responsive {
  overflow-x: auto;
}
.container {
	display: flex;
	flex-direction: column;
	box-shadow: 8px 8px 5px 0px #bdbdbdbf;
	width: 90%;
	background-color: #ffffff;
	border-radius: 30px;
  
}

.container2 {
	display: flex;
	flex-direction: column;
	box-shadow: 8px 8px 5px 0px #bdbdbdbf;
	width: 90%;
	background-color: #ffffff;
	border-radius: 30px;
   margin: auto;
}

.container, .container2 {
    width: 90%;
    height: 40vh;
    padding: 15px;
    display: flex;
    justify-content: space-between;
}
.table_header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 20px 30px 0;
}

button {
	outline: none;
	border: none;
	background-color: #27bb13;
	color: #ffffff;
	padding: 10px 30px;
	border-radius: 20px;
	text-transform: uppercase;
	cursor: pointer;
}

button:hover {
	background-color: #27bb13;
}

select {
	border: none;
	border-bottom: 1px solid #c9c9c9;
	width: 200px;
	padding: 10px 0;
	font-size: 16px;
}

.input_search {
	position: relative;
}

.input_search input {
	border-radius: 30px;
	width: 40%;
	outline: none;
	padding: 10px 20px;
	border: 1px solid #c9c9c9;
	box-sizing: border-box;
	padding-right: 50px;
}

.input_search #search {
	position: absolute;
	top: 50%;
	right: 0;
	margin-right: 1rem;
	transform: translate(-50%, -50%);
}

table {
	border-spacing: 0;
	margin-top: 1rem;
}

thead {
	background-color: #fff7b3;
}

th {
	padding: 10px;
}

tbody tr {
	border-bottom: 1px solid #dfdfdf;
}

tbody td {
	padding: 10px;
	border-bottom: 1px solid #dfdfdf;
	text-align: center;
}

tbody td #icons {
	font-size: 20px;
	cursor: pointer;
	margin-left: 10px;
	color: #797979;
}

tbody tr:hover {
	background-color: #f5f5f5;
}

.table_fotter {
	margin-top: 1rem;
	padding: 0 30px 20px;
}

.pagination {
  display: flex;
  gap: 5px;
  justify-content: center;
  align-items: center;
  margin-top: 15px;
}

button {
  outline: none;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  background-color: #27bb13;
  color: white;
}

button:disabled {
  background-color: #27bb13;
}

button.active {
  background-color: #ffa500; /* Cambiar color para la página activa */
}
</style>
