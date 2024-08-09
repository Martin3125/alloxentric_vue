<template>
   <link rel="stylesheet" href="src\assets\Inicio.css">
  <div>
    <header>
        <div id="logo_header">
          <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\2.png" alt="logo" />
          <h2>Alloxentric</h2>
        </div>
        <div id="menu"></div>
    </header>
    <div class="my-component">
        <div id="general">
            <div id="MenuPrincipal">
                <ul class="nav flex-column">
                    <li class="nav-item">
                    <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" href="C:\Users\Equipo PC\Desktop\Alloxentric\inicio.html" style="color: #ffffff;">
                        <svg class="bi"><use xlink:href="#house-fill"></use></svg>
                        Inicio
                    </a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link d-flex align-items-center gap-2" href="/cobranza" style="color: #ffffff;">
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
                      <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Buscar">
                  </div>
                  <div class="card-body" id="usuario">
                      <h5 class="card-title2">Usuario</h5>
                  </div>
              </div>
              <div id="bodycard">
                  <div  id="card"  class="card">
                    <div class="card-body" >
                        <h5 class="card-title3">Últimos documentos subidos</h5>
                          <table id="documentTable">
                            <thead>
                                <tr>
                                    <th>Documentos</th>
                                    <th>Fechas</th>
                                </tr>
                                <tr>
                                  <th>Documento 1 .csv</th>
                                  <th>24/06/2024</th>
                                </tr>
                                <tr>
                                  <th>Documento 2 .xlsx</th>
                                  <th>24/06/2024</th>
                                </tr>
                                <tr>
                                  <th>Documento 3 .csv</th>
                                  <th>24/06/2024</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Filas de datos irán aquí -->
                            </tbody>
                        </table>
                    </div>
                </div>
                <div  id="card2"  class="card2">
                  <div class="card-body" >
                      <h5 class="card-title3">Procesamientos programados</h5>
                        <table id="documentTable">
                          <thead>
                              <tr>
                                  <th>Nombre del procesamiento</th>
                                  <th>Fechas</th>
                                  <th>Hora</th>
                                  <th>Cancelar</th>

                              </tr>
                              <tr>
                                <th>Proceso 1 </th>
                                <th>24/06/2024</th>
                                <th>12:50</th>
                                <th><button type="download" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Cancelar</button></th>
                              </tr>
                              <tr>
                                <th>Proceso 2 </th>
                                <th>24/06/2024</th>
                                <th>14:30</th>
                                <th><button type="download" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Cancelar</button></th>
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
    </div>
  </div>
</template>
<script>
export default {
  name: 'Inicio-',
  // Definición del componente
}
</script>
  
<style>
    
</style>