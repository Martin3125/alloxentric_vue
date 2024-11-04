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
        
          <div class="container">
            
            <!-- <div class="card-body" >
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
                <div v-if="successMessage" class="alert alert-success mt-3">{{ successMessage }}</div>
            </div> -->

            <div class="card-body">
              <h5 class="card-title3">Acciones de Cobranza</h5>
              <form @submit.prevent="registrarCobranza">
                  <div class="card-body2">
                      <table class="table">
                          <thead>
                              <tr>
                                  <th>Acción</th>
                                  <th>Fecha</th>
                                  <th>Intervalo de Tiempo (Días)</th>
                                  <th>Valor ($)</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr v-for="(action, index) in actions" :key="index">
                                  <td>{{ action.accion_cobranza }}</td>
                                  <td>
                                      <input v-model="action.fecha_cobranza" type="date" class="form-control">
                                  </td>
                                  <td>
                                      <input v-model="action.intervalo" type="number" class="form-control" min="0">
                                  </td>
                                  <td>
                                      <input v-model="action.valor" type="number" class="form-control" step="0.01" min="0" placeholder="0.00">
                                  </td>
                              </tr>
                          </tbody>
                      </table>
                  </div>
                  <button id="guardar" type="submit" class="btn btn-primary">Guardar</button>
              </form>
              <div v-if="successMessage" class="alert alert-success mt-3">{{ successMessage }}</div>
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
      successMessage: '',  // Mensaje de éxito
      showToast: false,    // Controlar la visibilidad del toast
    };
  },
  mounted() {
    this.cargarDatos();
  },
  methods: {
    guardarDatos() {
      localStorage.setItem('actions', JSON.stringify(this.actions));
    },
    cargarDatos() {
      const storedActions = localStorage.getItem('actions');
      if (storedActions) {
        this.actions = JSON.parse(storedActions);
      }
    },
    async registrarCobranza() {
      this.showToast = true; // Mostrar el mensaje 
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
          this.successMessage = 'Acciones de cobranza guardadas correctamente!'; // Mensaje de éxito
          // this.$router.push('/cobranza'); // Aquí puedes redirigir al usuario o limpiar el formulario
        }
      } catch (error) {
        console.error('Error en la solicitud:', error);
        this.successMessage = 'Error al guardar las acciones de cobranza.';
       } finally {
        this.showToast = false; // Ocultar el mensaje de procesamiento después de completar la solicitud
      }
    },
    toggleSidebar() {
        this.isCollapsed = !this.isCollapsed;
      },
  }
};
</script>

<style>
/* Estilos generales */
body {
  font-family: 'Nunito', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa; /* Color de fondo para un mejor contraste */
}

/* Estilos para el encabezado */
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 20px;
  background-color: #343a40; /* Color de fondo del encabezado */
  color: white; /* Color del texto */
}

/* Estilos del logo y botón */
#logo_header {
  display: flex;
  align-items: center;
}

#logo_header img {
  height: 50px; /* Tamaño del logo */
  margin-right: 10px; /* Espaciado entre logo y título */
}

/* Estilos del campo de búsqueda */
.input_search {
  display: flex;
  align-items: center;
  flex-grow: 1; /* Permitir que el campo de búsqueda use el espacio disponible */
  margin: 0 20px; /* Espaciado horizontal */
}

.input_search input {
  flex-grow: 1; /* El input ocupa todo el espacio disponible */
  padding: 8px; /* Espaciado interno */
}

/* Estilos del menú */
#menu {
  margin-left: auto; /* Separar el menú del resto */
}

/* Estilos generales del contenedor principal */
#general {
  display: flex;
  height: calc(100vh - 60px); /* Restar el alto del encabezado */
}

/* Estilos para el menú */
Menu_P {
  flex: 0 0 200px; /* Fijo en 200px de ancho */
}

/* Estilos del main */
main {
  flex: 1; /* Ocupa el espacio restante */
  padding: 20px; /* Espaciado interno */
}

/* Estilos del contenedor de tarjetas */
.container {
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 1200px; /* Limitar el ancho máximo */
  height: 90%;
  background-color: #ffffff;
  border-radius: 20px;
  margin: auto; /* Centrar horizontalmente */
  padding: 20px; /* Espaciado interno */
  overflow: hidden; /* Evitar que se desborde el contenido */
}

/* Estilos de la lista de acciones */
.card-body2 {
  margin: 10px 0;
}

.list-group {
  display: flex;
  flex-wrap: wrap; /* Permitir que los elementos se ajusten a varias líneas */
  list-style-type: none;
  padding: 0;
}

.list-group-item {
  flex: 1 1 calc(30% - 10px); /* Ocupa un 30% menos espacio entre elementos */
  margin: 5px; /* Espaciado entre elementos */
}

/* Estilos para el botón guardar */
#guardar {
  margin-top: 20px; /* Espaciado superior */
}

/* Estilos para mensajes de alerta */
.alert {
  margin-top: 1rem;
}

.table {
    width: 100%; /* Hacer que la tabla ocupe el 100% del contenedor */
    margin-top: 20px; /* Espaciado superior */
    border-collapse: collapse; /* Colapsar bordes para un aspecto más limpio */
}

.table th, .table td {
    padding: 10px; /* Espaciado interno */
    text-align: left; /* Alinear el texto a la izquierda */
    border-bottom: 1px solid #ddd; /* Línea debajo de cada fila */
}

.table th {
    background-color: #f1f1f1; /* Color de fondo para el encabezado */
}

.form-control {
    width: 100%; /* Hacer que los inputs ocupen el 100% del espacio de la celda */
}


/* Media Queries para Responsividad */
@media (max-width: 768px) {
  .list-group-item {
    flex: 1 1 100%; /* Ocupa el 100% en pantallas pequeñas */
  }

  #logo_header img {
    height: 40px; /* Reducción del tamaño del logo */
  }
}

@media (max-width: 480px) {
  header {
    flex-direction: column; /* Cambia a disposición vertical en pantallas muy pequeñas */
    align-items: flex-start; /* Alinear al inicio */
  }

  .input_search {
    margin: 10px 0; /* Espaciado vertical */
  }
}

</style>