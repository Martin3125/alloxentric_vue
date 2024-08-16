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
                <form @submit.prevent="submitForm">
                <div  class="card-body2">
                  
                    <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Sin acciones</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[0].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[0].intervalo" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[0].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Correo electrónico</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[1].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[1].intervalo" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[1].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">SMS</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[2].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[2].intervalo"  type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[2].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Whatsapp</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[3].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[3].intervalo" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[3].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Llamada por bot</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[4].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[4].intervalo" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[4].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item">Llamada directa</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[5].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[5].intervalo" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[5].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
                    
                  </ul>
                  <ul class="list-group list-group-horizontal-sm">
                    <li class="list-group-item" >Acciones judiciales</li>
                    <li class="list-group-item">Fecha:<input v-model="actions[6].fecha_cobranza" type="date" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></li>
                    <li class="list-group-item">Intervalo de Tiempo de éxito: (Días)<input v-model="actions[6].intervalo" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" min="0"></li>
                    <li class="list-group-item">Valor: $<input v-model="actions[6].valor" type="number" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" step="0.01" min="0" placeholder="0.00"></li>
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
  name: 'Cobranza-',
  // Definición del componente
  components: {
    Menu_P,
    
  },

  data() {
    return {
      actions: [
        { accion_cobranza: 'Sin acciones', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { accion_cobranza: 'Correo electrónico', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { accion_cobranza: 'SMS', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { accion_cobranza: 'Whatsapp', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { accion_cobranza: 'Llamada por bot', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { accion_cobranza: 'Llamada directa', fecha_cobranza: '', intervalo: 0, valor: 0.00 },
        { accion_cobranza: 'Acciones judiciales', fecha_cobranza: '', intervalo: 0, valor: 0.00 }
      ]
    };
  },

  methods: {
    async submitForm() {
      try {
        const response = await fetch('http://localhost:8000/api/cobranza', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.actions)
        });

        const data = await response.json();
        if (response.ok) {
          alert('Cobranza actualizada exitosamente');
        } else {
          alert('Error al actualizar cobranza: ' + data.detail);
        }
      } catch (error) {
        console.error('Error:', error);
        alert('Error al enviar datos');
      }
    }
  }
}

</script>
  
<style>

</style>