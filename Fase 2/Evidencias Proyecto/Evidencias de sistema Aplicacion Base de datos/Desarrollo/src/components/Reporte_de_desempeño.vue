<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_desempeño.css">
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
        </div>
    </header>
    
<div id="general">
  <Menu_P v-if="!isCollapsed"/>
      <main id="cards">
          <!-- <div id="card" class="card"> -->
            <div class="container">
              <div class="table_header">
                  <h2>Reportes de Desempeño</h2>
                  <select v-model="tipoSeleccionado">
                      <option value="" selected>Todos</option>
                      <option value="Acciones judiciales">Acciones judiciales</option>
                      <option value="Correo electronico">Correo electrónico</option>
                      <option value="Llamada directa">Llamada directa</option>
                      <option value="Llamada por bot">Llamada por bot</option>
                      <option value="SMS">SMS</option>
                      <option value="Sin acciones">Sin acciones</option>
                  </select>
              </div>
              
              <table class="table-wrapper">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>ID Procesamiento</th>
                      <th>Acción de Cobranza</th>
                      <th>accion_predicha</th>
                      <th>Fecha de Cobranza</th>
                      <th>Intervalo</th>
                      <th>Deudores Registrados</th>
                      <th>Deudores por Acción</th>
                      <th>Valor</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in tablaCombinada" :key="`combinado-${index}`" >
                      <td>{{ index + 1 }}</td>
                      <td>{{ item.id_procesamiento}}</td>
                      <td>{{ item.accion_cobranza}}</td>
                      <td>{{ item.accion_predicha  }}</td>
                      <td>{{ item.fecha_cobranza }}</td>
                      <td>{{ item.intervalo }}</td>
                      <td>{{ item.registro_deudores }}</td>
                      <td>{{ item.deudores_contactar }}</td>
                      <td>{{ item.valor }}</td> 
                    </tr>
                  </tbody>
                  
              </table>
              <div class="pagination">
                        <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1">Anterior</button>
                        <span>Página {{ currentPage }} de {{ totalPages }}</span>
                        <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages">Siguiente</button>
                    </div>
            </div>
          <!-- </div> -->
      </main>
</div>
     
</template>

<script>
import { initializeFilter } from './js/filtro.js';
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
  name: 'Reporte_de_d',
  components: {
    Menu_P,
  },
  data() {
    return {
      accionesCobranza: [],
      tablaCombinada: [],
      resultados: [],
      busqueda: "",
      tipoSeleccionado: "",
      isCollapsed: true,
      currentPage: 1,
      itemsPerPage: 7,
    };
  },
  mounted() {
    initializeFilter();
    this.fetchAccionesCobranza();
    this.fetchResultados();
  },
  computed: {
    resultadosFiltrados() {
      return this.resultados.filter((resultado) => {
        const coincideBusqueda = resultado.documento_cargado.toLowerCase().includes(this.busqueda.toLowerCase());
        const coincideTipo = !this.tipoSeleccionado || resultado.accion_predicha === this.tipoSeleccionado;
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
    },
  },
  methods: {
    async fetchAccionesCobranza() {
      try {
        const response = await axios.get("http://localhost:8000/acciones_cobranza");
        this.accionesCobranza = response.data;
        this.combineData(); // Llama a combineData después de obtener accionesCobranza
      } catch (error) {
        console.error("Error al obtener las acciones de cobranza:", error);
      }
    },
    async fetchResultados() {
      try {
        const response = await axios.get('http://localhost:8000/resultados');
        this.resultados = response.data;
        this.combineData(); // Llama a combineData después de obtener resultados
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    combineData() {
      if (this.resultados.length && this.accionesCobranza.length) {
        // Combina los datos de `resultados` y `accionesCobranza` en `tablaCombinada`
        this.tablaCombinada = this.resultados.map((resultado, index) => {
          const accion = this.accionesCobranza[index] || {};
          return {
            id_procesamiento: resultado.id_procesamiento,
            accion_predicha: resultado.accion_predicha,
            registro_deudores: resultado.registro_deudores,
            deudores_contactar: resultado.deudores_contactar,
            fecha_cobranza: accion.fecha_cobranza || "",
            intervalo: accion.intervalo || "",
            valor: accion.valor || ""
          };
        });
      }
    },
    changePage(page) {
      this.currentPage = page;
    },
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
  },
};
</script>


<style scoped>
  .container {
      display: flex;
      flex-direction: column;
      box-shadow: 8px 8px 8px 8px #bdbdbdbf;
      width: 90%;
      background-color: #ffffff;
      border-radius: 30px;
      justify-content: center;
      margin: auto;
      height: 300vh;
  }
  
  .table-wrapper {
      margin-top: 1rem;
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
      width: 100%;
      border-spacing: 0;
  }
  
  thead {
      background-color: #fff7b3;
  }
  
  th {
      padding: 10px;
      text-align: left;
  }
  
  tbody tr {
      border-bottom: 1px solid #dfdfdf;
  }
  
  tbody td {
      padding: 10px;
      text-align: center;
  }
  
  tbody tr:hover {
      background-color: #f5f5f5;
  }
  
  .pagination {
      display: flex;
      justify-content: center;
      margin-top: 1rem;
  }
  
  .pagination button {
      padding: 5px 10px;
      margin: 0 5px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 3px;
      cursor: pointer;
  }
  
  .pagination button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
  }
  
  .pagination span {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 5px 10px;
      margin: 0 5px;
  }
  </style>