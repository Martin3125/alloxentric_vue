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
  <Menu_P  />
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
import Menu_P from './Menu-.vue';
export default {
  name: 'Cobranza-',
  // Definición del componente
  components: {
    Menu_P,
    
  }
}
</script>
  
<style>

</style>