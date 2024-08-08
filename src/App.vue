<template>
  <div id="app">
    <Login />
    <router-view/>
  </div>
  
</template>

<script>
// import Inicio from './components/Inicio-.vue' // Importa el componente

import Login from './components/Login-.vue'



export default {
  name: 'App',
  components: {
    Login,// Registra el componente
    
  }
}
</script>
<style>

</style>