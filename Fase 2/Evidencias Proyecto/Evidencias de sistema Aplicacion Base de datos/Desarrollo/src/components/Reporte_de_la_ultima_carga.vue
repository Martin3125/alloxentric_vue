<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_la_ultima_carga.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <header>
        <div id="logo_header">
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>

        <div id="menu">
        </div>
    </header>
<div id="general">
  <Menu_P  /> 
    <main id="cards">
        <div id="arriba">
            <div class="card-body"  id="Titulo" >
                <h5 class="card-title1">Informes</h5>
            </div>
            <div class="card-body" id="usuario" >
                <h5 class="card-title2">Usuario</h5>
            </div>
        </div>
        <div  id="card"  class="card">
          <div class="container">
            <!-- Header de la tabla -->
            <div class="table_header">
              <h2>Reporte de la ultima carga</h2>
              <!-- <button @click="crearProducto">Crear nuevo</button> -->
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
              <div class="input_search">
                <input v-model="busqueda" type="search" placeholder="Buscar" />
                <i class="bi bi-search" id="search"></i>
              </div>
            </div>

            <!-- Tabla de productos -->
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nombre del documento</th>
                  <th>Fecha de carga</th>  
                  <th>Registro de gente</th>
                  <th>Tipo de acción</th>
                  <th>Cantidad de gente a contactar</th>
                  <th>Precio</th>
                  <th>Acciones de cobranza</th>
                  <th>Total deudores</th>
                  <th>Operaciones</th> <!-- (Descargar) -->
                </tr>
              </thead>
              <tbody>
                <tr v-for="resultado in paginatedResultados" :key="resultado.id">
                  <td>{{ resultado.Id_resultados }}</td>
                  <td>{{ resultado.nombre }}</td>
                  <td>{{ resultado.fecha }}</td>
                  <td>{{ resultado.registro }}</td>
                  <td>{{ resultado.tipo }}</td>
                  <td>{{ resultado.cantidad }}</td>
                  <td>{{ resultado.precio }}</td>
                  <td>
                    <ul v-for="(prediccion, i) in resultado.predicciones" :key="i">
                    
                       {{ prediccion.accion_predicha }}
                        
                      </ul>
                    </td>
                    <td>
                      <ul v-for="(prediccion, i) in resultado.predicciones" :key="i">
                        
                       {{ prediccion.total_deudores }}
                       
                      </ul>
                    </td>
                  <td>
                    <i class="bi bi-pencil-square" @click="editarResultado(resultado)"></i>
                    <i class="bi bi-trash" @click="eliminarResultado(resultado._id)"></i>
                  </td>
                  
              </tr>
              <!-- <tr v-for="(resultado, index) in predictions" :key="index">
                            <td style="border: 1px solid black;">{{ resultado.accion_predicha }}</td>
                            <td style="border: 1px solid black;">{{ resultado.total_deudores }}</td>
                        </tr> -->
                       
              </tbody>
              <tbody>
                  <tr v-for="(prediccion, _id) in predicciones" :key="_id">
                      <td style="border: 1px solid black;">{{ prediccion.accion_predicha }}</td>
                      <td style="border: 1px solid black;">{{ prediccion.total_deudores }}</td>
                  </tr>
              </tbody>
            </table>

            <!-- Footer de la tabla -->
            <div class="table_footer">
              <p>Total de filas: {{ paginatedResultados.length }}</p>
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
    this.fetchPredicciones();
  },
  components: {
    Menu_P,
  },
  data() {
    return {
      busqueda: "",
      tipoSeleccionado: "",
      resultados: [],
      predicciones: [], 
      currentPage: 1,
      itemsPerPage: 5,
      // predictions: JSON.parse(localStorage.getItem('predicciones')) || [], // Recupera las predicciones del local storage
    };
  },
  computed: {
    resultadosFiltrados() {
      return this.resultados.filter((resultado) => {
        const coincideBusqueda = resultado.nombre.toLowerCase().includes(this.busqueda.toLowerCase());
        const coincideTipo = !this.tipoSeleccionado || resultado.tipo === this.tipoSeleccionado;
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
    async fetchPredicciones() {
        try {
            const response = await axios.get('/api/predicciones');
            if (response.data && response.data.predicciones) {
                this.predicciones = response.data.predicciones; // Asigna las predicciones al array
            }
        } catch (error) {
            console.error('Error al obtener las predicciones:', error);
        }
    },
  },
};
</script>

<style scoped>

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

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
	box-shadow: 8px 8px 5px 0px #bdbdbdbf;
	width: 90%;
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
	background-color: #27bb13;
	color: #ffffff;
	padding: 10px 30px;
	border-radius: 20px;
	text-transform: uppercase;
	font-size: 14px;
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

</style>