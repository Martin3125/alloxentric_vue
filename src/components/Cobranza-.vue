<template>
  <link rel="stylesheet" href="src\assets\Cobranza.css">
    <body>
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
                <h5 class="card-title1">Cobranza</h5>
            </div>
            <div class="card-body" id="usuario">
                <h5 class="card-title2">Usuario</h5>
            </div>
        </div>
        <div  id="card"  class="card">
            <div class="card-body" >
                <h5 class="card-title3">Acciones de Cobranza</h5>
                <div  class="card-body2">
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Sin acciones</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Correo electrónico</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">SMS</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Whatsapp</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Llamada por bot</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Llamada directa</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Acciones judiciales</li>
                    <li class="list-group-item">Fecha:<input type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                  </ul>
                </div>
                <button id="guardar" type="button" class="btn btn-primary">Guardar</button>

            </div>
        </div>
    </main>
</div>
</body>
</template>
<script>
export default {
  name: 'Cobranza-',
  // Definición del componente
}
</script>
  
<style>

</style>