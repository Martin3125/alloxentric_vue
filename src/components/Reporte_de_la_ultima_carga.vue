<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_la_ultima_carga.css">
    <header>
        <div id="logo_header">
            <img src="C:\Users\Equipo PC\Desktop\Alloxentric\2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>

        <div id="menu">
        </div>
    </header>
<div id="general">
    <div id="MenuPrincipal">
        <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" href="C:\Users\Equipo PC\Desktop\Alloxentric\inicio.html" style="color: #ffffff;">
                <svg class="bi"><use xlink:href="#house-fill"></use></svg>
                Inicio
              </a>
            </li>
            <!-- <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\documentos.html" style="color: #ffffff;">
                <svg class="bi"><use xlink:href="#file-earmark"></use></svg>
                Documentos
              </a>
            </li> -->
            <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cobranza.html" style="color: #ffffff;">
                <svg class="bi"><use xlink:href="#cart"></use></svg>
                Cobranza
              </a>
            </li>
            <li class="nav-item">
              <div class="accordion accordion-flush" id="accordionFlushExample" >
                <div class="accordion-item" style="background-color: #06B7B2; color: #ffffff;"  >
                  <h2 class="accordion-header" id="procesamiento">
                    <button class="accordion-button collapsed" style="background-color: #06B7B2; margin-left: 6%; width: 93%; color: #ffffff;" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne" >
                      Procesamiento
                    </button>
                  </h2>
                  <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                    <div class="accordion-body" >
                      <ul class="list-group">
                        <li class="nav-item">
                          <a color="#06B7B2" class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cargar resultados del periodo anterior.html" style="color: #ffffff;">
                            <svg class="bi"><use xlink:href="#cart"></use></svg>
                            Cargar resultados del periodo anterior
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                    <div class="accordion-body">
                      <ul class="list-group">
                        <li class="nav-item">
                          <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Allexontric\Cargar resultados del periodo anterior.html" style="color: #ffffff;">
                            <svg class="bi"><use xlink:href="#cart"></use></svg>
                            Generar resultados del periodo
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="accordion-item" style="background-color: #06B7B2; color: #ffffff;">
                  <h2 class="accordion-header">
                    <button class="accordion-button collapsed" style="background-color: #06B7B2; color: #ffffff;  margin-left: 6%; width: 93%;" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                      Informes
                    </button>
                  </h2>
                  <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                    <div class="accordion-body">
                      <ul class="list-group">
                        <li class="nav-item">
                          <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Reporte de la ultima carga.html" style="color: #ffffff;">
                            <svg class="bi"><use xlink:href="#cart"></use></svg>
                            Reporte de la ultima carga
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                    <div class="accordion-body">
                      <ul class="list-group">
                        <li class="nav-item">
                          <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Reporte de desempeño.html" style="color: #ffffff;">
                            <svg class="bi"><use xlink:href="#cart"></use></svg>
                            Reporte de desempeño
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </li> 
          </ul>
          
          <hr class="my-3">
    
      <ul class="nav flex-column mb-auto">
        <li class="nav-item">
          <a class="nav-link d-flex align-items-center gap-2" href="#" style="color: #ffffff;">
            <svg class="bi"><use xlink:href="#gear-wide-connected"></use></svg>
            Settings
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link d-flex align-items-center gap-2" href="#" style="color: #ffffff;">
            <svg class="bi"><use xlink:href="#door-closed"></use></svg>
            Sign out
          </a>
        </li>
      </ul>
    </div>
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
            <div class="card-body" >
                <h5 class="card-title3">Reporte de la ultima carga</h5>
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
                          <label>
                              <input type="checkbox" name="action" value="correo">
                              Correo electrónico
                          </label>
                          <label>
                              <input type="checkbox" name="action" value="sms">
                              SMS
                          </label>
                          <label>
                              <input type="checkbox" name="action" value="whatsapp">
                              Whatsapp
                          </label>
                          <label>
                            <input type="checkbox" name="action" value="llamada">
                            Llamada por bot
                        </label>
                          <label>
                              <input type="checkbox" name="action" value="llamada">
                              Llamada directa
                          </label>
                          <label>
                              <input type="checkbox" name="action" value="acciones_judiciales">
                              Acciones judiciales
                          </label>
                          <label>
                              <input type="checkbox" name="action" value="sin_acciones">
                              Sin acciones
                          </label>
                          <button type="submit">Filtrar</button>
                      </form>
                  </div>
                  <table id="documentTable">
                    <thead>
                        <tr>
                            <th style="border: 1px solid black;">ID</th>
                            <th style="border: 1px solid black;">Nombre del documento</th>
                            <th style="border: 1px solid black;">Fecha</th>
                            <th style="border: 1px solid black;">Registro de gente</th>
                            <th style="border: 1px solid black;">Tipo de acción</th>
                            <th style="border: 1px solid black;">Cantidad de gente a contactar</th>
                            <th style="border: 1px solid black;">Descargar</th>
                        </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th style="border-right: 1px solid black; border-left: 1px solid black;"></th>
                        <td style="border: 1px solid black;">Documento 1</td>
                        <td style="border: 1px solid black;">28/07/2024</td>
                        <td style="text-align: center; border: 1px solid black;">300</td>
                        <td style="border: 1px solid black;">Correo electrónico</td>
                        <td style="text-align: center;border: 1px solid black;">100</td>
                        <td style="border: 1px solid black;"><a type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Descargar</a></td>
                      </tr>
                      <tr>
                        <th scope="row" style="border-right: 1px solid black; border-left: 1px solid black;">A001</th>
                        <td style="border: 1px solid black;">Documento 2</td>
                        <td style="border: 1px solid black;">28/07/2024</td>
                        <td style="text-align: center; border: 1px solid black;">300</td>
                        <td style="border: 1px solid black;">Whatsapp</td>
                        <td style="text-align: center; border: 1px solid black;">50</td>
                        <td style="border: 1px solid black;"><a type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Descargar</a></td>
                      </tr>
                      <tr>
                        <th scope="row" style="border: 1px solid black;"></th>
                        <td style="border: 1px solid black;">Documento 3</td>
                        <td style="border: 1px solid black;">28/07/2024</td>
                        <td style="text-align: center; border: 1px solid black;">300</td>
                        <td style="border: 1px solid black;">Llamada por bot</td>
                        <td style="text-align: center; border: 1px solid black;">150</td>
                        <td style="border: 1px solid black;"><a type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Descargar</a></td>
                      </tr>
                    </tbody>
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

export default {
  name: 'Reporte_ultima_carga',// Definición del componente
  mounted() {
    initializeFilter();
  }
  
}
</script>
  
<style>

</style>