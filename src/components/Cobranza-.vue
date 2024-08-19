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
      ]
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
    }
  }
};
</script>




<style>

</style>