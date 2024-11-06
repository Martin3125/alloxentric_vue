<template>
    <link rel="stylesheet" href="src/assets/res_periodo_anterior.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
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
        <div class="input_search">
            <input v-model="busqueda" type="search" placeholder="Buscar" />
            <i class="bi bi-search" id="search"></i>
        </div>
        <div class="card-body">
            <h5 class="card-title2">Usuario: {{ usuarioLogueado }}</h5>
        </div>
    </header>
    

</body>
<div class="main">
    <Menu_P v-if="!isCollapsed"/>
    <main id="cards">
        <div class="general">

            <div class="container">
                <div class="titulos">
                    <div class="btn_volver">
                        <a class="btn btn-primary" href="/cargar_resultados" style="width: 100%;">VOLVER</a>
                    </div>

                    <div class="text_resultados">
                        <h1 style="text-align: left;">Resultados del período anterior </h1>
                    </div>

                </div>
                <!-- Filtro de Procesamiento -->
                <div class="filtro-procesamiento">
                    <label for="filtroAccion">Filtrar por Acción de Cobranza: </label>
                    <select v-model="tipoSeleccionado" id="filtroAccion">
                        <option value="">Todos</option>
                        <option value="O876">O876</option>
                        <option v-for="accion in acciones" :key="accion.Id_accion" :value="accion.nombre">{{ accion.nombre }}</option>
                    </select>
                </div>
                
                <div class="tbl_resultados">
                    <!-- Tabla de resultados -->
                    <table>
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>ID Procesamiento</th>
                                <th>Documento Cargado</th>
                                <th>Fecha de Carga</th>
                                <th>Deudores registrados</th>
                                <th>Acciones de Cobranza</th>
                                <th>Deudores por acción</th>
                                <!-- <th>Precio</th>
                                <th>Valor Multiplicado</th>  -->
                                <th>Operaciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(resultado, index) in paginatedResultados" :key="resultado.id_procesamiento">
                                <td>{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                                <td>{{ resultado.id_procesamiento }}</td>
                                <td>{{ resultado.documento_cargado }}</td>
                                <td>{{ resultado.fecha_carga }}</td>
                                <td>{{ resultado.registro_deudores }}</td>
                                <td>{{ resultado.accion_predicha}}</td> <!-- Campo corregido si es necesario -->
                                <td>{{ resultado.deudores_contactar }}</td>
                                <!-- <td>{{ resultado.precio }}</td>  -->
                                <!-- <td>{{ resultado.valor_multiplicado }}</td>   -->
                                
                                <td>
                                    <i class="bi bi-pencil-square" @click="editarResultado(resultado)"></i>
                                    <i class="bi bi-trash" @click="eliminarResultado(resultado.id_procesamiento)"></i>
                                </td>
                            </tr>
                        </tbody>
                    </table>
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
  name: 'res_periodo_anterior', // Definición del componente
  mounted() {
    this.fetchResultados();
    this.cargarAcciones();
  },
  components: {
    Menu_P,
  },
  data() {
    return {
      busqueda: "",
      tipoSeleccionado: "",
      resultados: [],
      acciones: [], // Lista de acciones de cobranza
      currentPage: 1,
      itemsPerPage: 7,
      isCollapsed: true,
    };
  },
  computed: {
    // Filtrar resultados por búsqueda y tipo de acción seleccionada
    resultadosFiltrados() {
        return this.resultados.filter((resultado) => {
            const coincideBusqueda = resultado.documento_cargado.toLowerCase().includes(this.busqueda.toLowerCase());
            const coincideTipo = !this.tipoSeleccionado || resultado.id_procesamiento === this.tipoSeleccionado;
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
    async cargarAcciones() {
      try {
        const response = await axios.get('http://localhost:8000/api/acciones');
        this.acciones = response.data; // Asignar los datos a la propiedad acciones
      } catch (error) {
        console.error('Error al cargar acciones de cobranza:', error);
      }
    },
    accionPorId(idAccion) {
      return this.acciones.find(accion => accion.Id_accion === idAccion);
    },
    calcularValorMultiplicado(deudoresContactar, valor) {
      return deudoresContactar * valor; // Multiplicación del valor por los deudores a contactar
    }
  }
};
</script>

<style>

</style>