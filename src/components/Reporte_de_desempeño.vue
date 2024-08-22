<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_desempeño.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <header>
        <div id="logo_header">
            <img src="C:\Users\Equipo PC\Desktop\Alloxentric\2.png" alt="logo">
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
                        <tr>
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
                      </tr>
                    </thead>
                    <tbody>
                        <!-- Filas de datos irán aquí -->
                    </tbody>
                </table>

                </div>
            </div>
        </div>
    </main>
</div>
</template>
<script>
import {initializeFilter} from './js/filtro.js';
import Menu_P from './Menu-.vue';

export default {
  name: 'Reporte_de_d',// Definición del componente
  mounted() {
    initializeFilter();
  },
  components: {
    Menu_P,

    
  }
}
</script>
  
<style>

</style>