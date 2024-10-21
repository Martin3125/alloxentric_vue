<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_desempeño.css">
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
            <div class="card-body" id="usuario">
                <h5 class="card-title2">Usuario</h5>
            </div>
        </div>
        <div  id="card"  class="card">
            <div class="card-body" >
                <h5 class="card-title3">Reportes desempeño</h5>
                <div  class="card-body2">
                  <div id="buscar-filtro">
                    <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Buscar">
                    <div class="filter-toggle-container">
                      <button id="toggleFilterButton">Mostrar Filtro</button>
                    </div>
                  </div>
                  <!-- <div id="buscar-filtro">
                    <input type="text" v-model="deudor_ids" class="form-control" placeholder="Buscar IDs de deudores separados por coma">
                    <div class="filter-toggle-container">
                      <button @click="getReporteDesempeno">Buscar</button>
                    </div>
                  </div> -->

                  <div class="filter-container" id="filterContainer">
                      <h2>Filtrar por tipo de acción</h2>
                      <form id="filterForm">
                          <!-- Campos de fecha -->
                          <label>
                              Fecha de envío: <input type="text" class="fecha_envio" name="fecha_envio" placeholder="DD/MM/YYYY">
                          </label><br>
                          <label>
                              Fecha de pago estimada: <input type="text" class="fecha_pago_estimado" name="fecha_pago_estimado" placeholder="DD/MM/YYYY">
                          </label><br>
                          <label>
                              Fecha real del pago: <input type="text" class="fecha_pago_real" name="fecha_pago_real" placeholder="DD/MM/YYYY">
                          </label><br>
                          <button type="submit">Filtrar</button>
                      </form>
                  </div>
                  <table id="documentTable">
                    <thead>
                        <tr>
                            <th>ID del Deudor</th>
                            <th>Nombre del Deudor</th>
                            <th>Cobranza</th>
                            <th>Fecha de envio</th>
                            <th>Intervalo</th>
                            <th>Fecha de  pago estimada</th>
                            <th>Demora</th>
                            <th>Fecha real del pago</th>
                            <th>Lo que debe pagar</th>
                            <th>Valor real a pagar</th>
                        </tr>
                        <!-- <tr>
                          <th>254</th>
                          <th>Bruno Díaz</th>
                          <th>Correo electronico</th>
                          <th>03/07/2024</th>
                          <th>2 Días</th>
                          <th>05/07/2024</th>
                          <th>4 Días</th>
                          <th>07/07/2024</th>
                          <th>$500000</th>
                          <th>$300000</th>
                      </tr> -->
                    </thead>
                    
                    <tbody>
                      <tr v-for="reporte in reportes" :key="reporte.ID_deudor">
                        <td>{{ reporte.ID_deudor }}</td>
                        <td>{{ reporte.nombre_deudor }}</td>
                        <td>{{ reporte.accion }}</td>
                        <td>{{ reporte.fecha_envio }}</td>
                        <td>{{ reporte.intervalo }}</td>
                        <td>{{ reporte.fecha_estimada }}</td>
                        <td>{{ reporte.demora }}</td>
                        <td>{{ reporte.fecha_real }}</td>
                        <td>{{ reporte.debe_pagar }}</td>
                        <td>{{ reporte.valor_pagar }}</td>
                      </tr>
                    </tbody>
                </table>

                </div>
            </div>
        </div>
    </main>
</div>
</template>


<!-- <script>
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
      reportes: [],  // Inicializa la lista de reportes como un array vacío
    };
  },
  mounted() {
    initializeFilter();
    this.getReporteDesempeno();  // Ejemplo con ID deudor 254, puedes modificarlo para ser dinámico
  },
  methods: {
    async getReporteDesempeno(deudor_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/reportes/${deudor_id}`);
        console.log(response.data);  // Verifica el formato de los datos en la consola
        // Agrega el reporte a la lista, en caso de que sea un solo objeto
        if (Array.isArray(response.data)) {
          this.reportes = response.data;
        } else {
          this.reportes = [response.data];  // Convierte el objeto en un array
        }
      } catch (error) {
        console.error("Error al obtener el reporte de desempeño:", error);
      }
    }
  },
  
}


</script> -->
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
      reportes: [],  // Inicializa la lista de reportes como un array vacío
      deudor_ids: [],  // Aquí se almacenarán los IDs de los deudores
    };
  },
  mounted() {
    initializeFilter();
    this.getAllDeudores();  // Cargar todos los IDs de los deudores al montar el componente
  },
  methods: {
    async getAllDeudores() {
      try {
        // Solicitar todos los IDs de los deudores
        const response = await axios.get('http://127.0.0.1:8000/api/deudores_ids');
        this.deudor_ids = response.data;
        // Ahora obtener los reportes para cada deudor
        this.getReportesParaTodosLosDeudores();
      } catch (error) {
        console.error("Error al obtener los IDs de los deudores:", error);
      }
    },
    
    async getReportesParaTodosLosDeudores() {
      for (const deudor_id of this.deudor_ids) {
        await this.getReporteDesempeno(deudor_id);  // Llama a la función para cada deudor
      }
    },

    async getReporteDesempeno(deudor_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/reportes/${deudor_id}`);
        console.log(response.data);  // Verifica el formato de los datos en la consola
        // Si la respuesta es un array, agrega los reportes
        if (Array.isArray(response.data)) {
          this.reportes.push(...response.data);  // Agrega todos los reportes al array
        } else {
          this.reportes.push(response.data);  // Si es un objeto, agrégalo directamente
        }
      } catch (error) {
        console.error("Error al obtener el reporte de desempeño para el deudor:", deudor_id, error);
      }
    }
  },
}
</script>


<style>

</style>