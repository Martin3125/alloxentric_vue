<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_desempeño.css">
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
                          <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\generar_resultados.html" style="color: #ffffff;">
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
          <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Login.html" style="color: #ffffff;">
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
export default {
  name: 'Reporte_de_desempeño',
  // Definición del componente
}
</script>
  
<style>

</style>