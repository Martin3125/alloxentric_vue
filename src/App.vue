<template>
  <div id="app">
    <Reporte_ultima_carga />
    <router-view/>
  </div>
  
</template>

<script>
// import Inicio from './components/Inicio-.vue' // Importa el componente

import Reporte_ultima_carga from './components/Reporte_de_la_ultima_carga.vue'
// Importa Bootstrap JS
import 'bootstrap/dist/js/bootstrap.bundle.min.js';



export default {
  name: 'App',
  components: {
    Reporte_ultima_carga,// Registra el componente
    
  }
}
</script>
<style>

</style>