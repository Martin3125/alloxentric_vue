<template>
  <link rel="stylesheet" href="src/assets/Reporte_de_desempeno.css">
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
      <div class="container">
        <div class="table_header">
          <h2>Reporte de Desempeño</h2>
        </div>
        
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>ID Procesamiento</th>
              <th>Acción Cobranza</th>
              <th>Registro Deudores</th>
              <th>Deudores a Contactar</th>
              <th>Fecha Cobranza</th>
              <th>Intervalo (Días)</th>
              <th>Costo total ($)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(resultado, index) in paginatedResultadosCombinados" :key="resultado.id_procesamiento">
              <td>{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
              <td>{{ resultado.id_procesamiento }}</td>
              <td>{{ resultado.accion_predicha }}</td>
              <td>{{ resultado.registro_deudores }}</td>
              <td>{{ resultado.deudores_contactar }}</td>
              <td>{{ resultado.fecha_cobranza || 'N/A' }}</td>
              <td>{{ resultado.intervalo || 0 }}</td>
              <td>{{ resultado.valor || 0 }}</td>
            </tr>
          </tbody>
        </table>
        
        <div class="table_footer">
          <div class="pagination">
            <button @click="changePage(1)" :disabled="currentPage === 1">Primera</button>
            <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1">Anterior</button>
            <span>Página {{ currentPage }} de {{ totalPages }}</span>
            <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">Siguiente</button>
            <button @click="changePage(totalPages)" :disabled="currentPage === totalPages">Última</button>
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
  name: 'Reporte_de_d',
  components: {
    Menu_P,
  },
  data() {
    return {
      busqueda: "",
      resultadosCombinados: [],
      currentPage: 1,
      itemsPerPage: 7,
      isCollapsed: true,
      usuarioLogueado: ''  // Ajusta según tu lógica para obtener el usuario logueado
    };
  },
  computed: {
    resultadosFiltrados() {
      return this.resultadosCombinados.filter((resultado) => {
        return resultado.accion_predicha.toLowerCase().includes(this.busqueda.toLowerCase());
      });
    },
    paginatedResultadosCombinados() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.resultadosFiltrados.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.resultadosFiltrados.length / this.itemsPerPage);
    }
  },
  methods: {
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
    async fetchData() {
      try {
        // Obtener los resultados
        const responseResultados = await axios.get('http://localhost:8000/resultados');
        const resultados = responseResultados.data;

        // Obtener las acciones de cobranza
        const responseAcciones = await axios.get('http://localhost:8000/api/acciones');
        const accionesCobranza = responseAcciones.data;

        // Crear un diccionario para acceder fácilmente a las acciones de cobranza
        const accionesDict = {};
        accionesCobranza.forEach(accion => {
          accionesDict[accion.accion_cobranza] = accion;
        });

        // Combinar los datos y calcular el valor
        this.resultadosCombinados = resultados.map(resultado => {
          const accion = accionesDict[resultado.accion_predicha];
          
          // Si encontramos la acción correspondiente, calculamos el valor
          const valor = accion ? accion.valor * resultado.deudores_contactar : 0;

          return {
            ...resultado,
            ...accion,
            valor // Agregar el valor calculado
          };
        });
      } catch (error) {
        console.error("Error al obtener los datos:", error);
      }
    },
    changePage(page) {
      this.currentPage = page;
    }
  },
  mounted() {
    this.fetchData();
  }
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
      background-color: #06B7B2;
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