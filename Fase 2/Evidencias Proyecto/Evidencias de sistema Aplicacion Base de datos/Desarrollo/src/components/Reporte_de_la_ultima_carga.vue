<template>
  <link rel="stylesheet" href="src/assets/Reporte_de_la_ultima_carga.css">
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
      <div class="input_search">
          <input v-model="busqueda" type="search" placeholder="Buscar" />
          <i class="bi bi-search" id="search"></i>
      </div>
      <div class="card-body">
          <h5 class="card-title2">Usuario: {{ usuarioLogueado }}</h5>
      </div>
  </header>
  <div id="general">
      <Menu_P v-if="!isCollapsed"/>
      <main id="cards">
          <div id="card" class="card">
              <div class="container">
                  <!-- Header de la tabla -->
                  <div class="table_header">
                      <h2>Reporte de la última carga</h2>
                      <select v-model="tipoSeleccionado">
                          <option value="" selected>Tipo de acción</option>
                          <option value="Sin acciones">Sin acciones</option>
                          <option value="Correo electrónico">Correo electrónico</option>
                          <option value="SMS">SMS</option>
                          <option value="Whatsapp">Whatsapp</option>
                          <option value="Llamada por bot">Llamada por bot</option>
                          <option value="Llamada directa">Llamada directa</option>
                          <option value="Acciones judiciales">Acciones judiciales</option>
                      </select>
                  </div>

                  <!-- Tabla de productos -->
                  <table>
                      <thead>
                          <tr>
                              <th>#</th>
                              <th>ID Procesamiento</th>
                              <th>Documento Cargado</th>
                              <th>Fecha de Carga</th>
                              <th>Registro de Deudores</th>
                              <th>Acciones de Cobranza</th>
                              <th>Deudores a Contactar</th>
                              <th>Precio</th>
                              <th>Operaciones</th>
                              <th>Predicción de Cobranza</th>
                              
                          </tr>
                      </thead>
                      <tbody>
                          <tr v-for="(resultado, index) in paginatedResultados" :key="index">
                              <td>{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                              <td>{{ resultado.id_procesamiento }}</td>
                              <td>{{ resultado.documento_cargado }}</td>
                              <td>{{ resultado.fecha_carga }}</td>
                              <td>{{ resultado.registro_deudores }}</td>
                              <td>{{ resultado.acciones_cobranza }}</td>
                              <td>{{ resultado.deudores_contactar }}</td>
                              <td>{{ resultado.precio }}</td>
                              <td>
                                  <i class="bi bi-pencil-square" @click="editarResultado(resultado)"></i>
                                  <i class="bi bi-trash" @click="eliminarResultado(resultado._id)"></i>
                              </td>
                              <!-- <td>{{ resultado.predicciones }}</td> -->
                              <td v-for="(prediccion, pIndex) in resultado.predicciones" :key="pIndex">
                                {{ prediccion.accion_predicha }} ({{ prediccion.total_deudores }})
                            </td>
                          </tr>
                      </tbody>
                  </table>

                  <!-- Footer de la tabla con paginación -->
                  <div class="table_footer">
                      <p>Total de filas: {{ resultadosFiltrados.length }}</p>
                      <div class="pagination">
                          <button @click="changePage(1)" :disabled="currentPage === 1">Primera</button>
                          <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1">Anterior</button>
                          <span>Página {{ currentPage }} de {{ totalPages }}</span>
                          <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">Siguiente</button>
                          <button @click="changePage(totalPages)" :disabled="currentPage === totalPages">Última</button>
                      </div>
                  </div>
              </div>
          </div>
      </main>
  </div>
</template>

<script>
import { initializeFilter } from './js/filtro.js';
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
  name: 'Reporte_ultima_carga',
  mounted() {
      initializeFilter();
      this.fetchResultados();
  },
  components: {
      Menu_P,
  },
  data() {
      return {
          busqueda: "",
          tipoSeleccionado: "",
          resultados: [],
          currentPage: 1,
          itemsPerPage: 5, // Mostrará solo 5 registros por página
          isCollapsed: true,
      };
  },
  computed: {
      resultadosFiltrados() {
          return this.resultados.filter((resultado) => {
              const coincideBusqueda = resultado.documento_cargado.toLowerCase().includes(this.busqueda.toLowerCase());
              const coincideTipo = !this.tipoSeleccionado || resultado.acciones_cobranza === this.tipoSeleccionado;
              return coincideBusqueda && coincideTipo;
          });
      },
      paginatedResultados() {
          const start = (this.currentPage - 1) * this.itemsPerPage;
          const end = start + this.itemsPerPage;
          return this.resultadosFiltrados.slice(start, end);
      },
      totalPages() {
          return Math.ceil(this.resultadosFiltrados.length / this.itemsPerPage);
      }
  },
  methods: {
      async fetchResultados() {
          try {
              const response = await axios.get('http://localhost:8000/resultados');
              this.resultados = response.data;
          } catch (error) {
              console.error('Error fetching data:', error);
          }
      },
      changePage(page) {
          this.currentPage = page;
      },
      editarResultado(resultado) {
          console.log("Editar resultado", resultado);
      },
      async eliminarResultado(id) {
          try {
              await axios.delete(`http://localhost:8000/resultados/${id}`);
              this.fetchResultados();
          } catch (error) {
              console.error('Error deleting result:', error);
          }
      },
      toggleSidebar() {
          this.isCollapsed = !this.isCollapsed;
      },
  },
};
</script>



<style scoped>

body {
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 100vh;
	font-family: "Raleway", sans-serif;
	background-color: #eef4fd;
}

.container {
	display: flex;
	flex-direction: column;
	box-shadow: 8px 8px 8px 8px #bdbdbdbf;
	width: 90%;
  height: 80%;
	background-color: #ffffff;
	border-radius: 30px;
  justify-content: center;
  margin: auto;
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
	background-color: #06B7B2;
	color: #ffffff;
	padding: 10px 30px;
	border-radius: 20px;
	text-transform: uppercase;
	cursor: pointer;
}

button:hover {
	background-color: #06B7B2;
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
	width: 400px;
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
.toggle-btn{
  background-color: #06B7B2;
}

button {
  outline: none;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  background-color: #06B7B2;
  color: white;
}

.card-title2{
    display: flex;
    justify-content:center;
    margin: auto;
    font-weight: 600;

}
</style>