<template>
  <link rel="stylesheet" href="src\assets\Cobranza.css">
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
        <div class="input_search" >
          <input v-model="busqueda" type="search" placeholder="Buscar" />
          <i class="bi bi-search" id="search"></i>
        </div>
        <div class="card-body">
          <h5 class="card-title2">Usuario{{ usuarioLogueado }}</h5>
        </div>
        <div id="menu">
        </div>
    </header>
<div id="general">
  <Menu_P v-if="!isCollapsed"/>
    <main id="cards">
        <!-- <div id="arriba">
            <div class="card-body"  id="Titulo" >
                <h5 class="card-title1">Cobranza</h5>
            </div>
            <div class="card-body" id="usuario">
                <h5 class="card-title2">Usuario</h5>
            </div>
        </div> -->
        <div  id="card"  class="card">
            <div class="card-body" >
                <h5 class="card-title3">Acciones de Cobranza</h5>
                <form @submit.prevent="registrarCobranza">
                  <div class="card-body2">
                    <ul v-for="(action, index) in actions" :key="index" class="list-group list-group-horizontal-sm">
                      <li class="list-group-item">{{ action.accion_cobranza }}</li>
                      <li class="list-group-item">Fecha: <input v-model="action.fecha_cobranza" type="date" class="form-control"></li>
                      <li class="list-group-item">Intervalo de Tiempo de éxito: (Días) <input v-model="action.intervalo" type="number" class="form-control" min="0"></li>
                      <li class="list-group-item">Valor: $ <input v-model="action.valor" type="number" class="form-control" step="0.01" min="0" placeholder="0.00"></li>
                    </ul>
                  </div>
                  <button id="guardar" type="submit" class="btn btn-primary">Guardar</button>
                </form>
            </div>
        </div>
    </main>
</div>
</body>
</template>
<script>
import Menu_P from './Menu-.vue';
export default {
  name: 'Cobranza-', // Definición del componente
  components: {
    Menu_P,
  },
  data() {
    return {
      actions: [
        { Id_accion: null, accion_cobranza: 'Sin acciones', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { Id_accion: null, accion_cobranza: 'Correo electrónico', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { Id_accion: null, accion_cobranza: 'SMS', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { Id_accion: null, accion_cobranza: 'Whatsapp', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { Id_accion: null, accion_cobranza: 'Llamada por bot', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { Id_accion: null, accion_cobranza: 'Llamada directa', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { Id_accion: null, accion_cobranza: 'Acciones judiciales', fecha_cobranza: '', intervalo: 0, valor: 0.00 }
      ],
      isCollapsed: true,
    };
  },
  methods: {
    async registrarCobranza() {
      try {
        const respuesta = await fetch('http://127.0.0.1:8000/api/acciones', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.actions)
        });

        if (!respuesta.ok) {
          const errorData = await respuesta.json();
          console.error('Error en la respuesta:', errorData);
          this.errorMessage = errorData.detail || 'Error en el registro';
        } else {
          const data = await respuesta.json();
          console.log(data);
          this.$router.push('/Inicio'); // Aquí puedes redirigir al usuario o limpiar el formulario
        }
      } catch (error) {
        console.error('Error en la solicitud:', error);
      }
    },
    toggleSidebar() {
        this.isCollapsed = !this.isCollapsed;
      },
  }
};
</script>




<style>

</style>