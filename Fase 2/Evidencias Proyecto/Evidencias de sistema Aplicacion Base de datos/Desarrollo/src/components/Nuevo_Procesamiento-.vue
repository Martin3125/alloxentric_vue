<template>
    <link rel="stylesheet" href="src/assets/Inicio.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
    <header>
      <div id="logo_header">
        <button class="toggle-btn" @click="toggleSidebar">
          <span class="icon" v-if="isCollapsed">☰</span>
          <span class="icon" v-else>✖</span>
        </button>
        <img src="@/assets/2.png" alt="logo" />
        <h2>Alloxentric</h2>
      </div>
      <div class="input_search">
        <input v-model="busqueda" type="search" placeholder="Buscar" />
        <i class="bi bi-search" id="search"></i>
      </div>
      <div class="card-body">
        <h5 class="card-title2">Usuario: {{ usuarioLogueado }}</h5>
      </div>
      <div id="menu"></div>
    </header>
  
    <div class="my-component">
      <div id="general">
        <Menu_P v-if="!isCollapsed" />
        <main id="cards">
            <h3>Retroalimentación de Acciones</h3>
                <form @submit.prevent="enviarRetroalimentacion">
                <div>
                    <label for="deudor">Seleccionar Deudor:</label>
                    <select v-model="deudorSeleccionado" id="deudor">
                    <option v-for="deudor in deudores" :key="deudor.nombre" :value="deudor.nombre">
                        {{ deudor.nombre }}
                    </option>
                    </select>
                </div>
                <div>
                    <label for="tipoAccion">Tipo de Acción:</label>
                    <input v-model="tipoAccion" type="text" id="tipoAccion" placeholder="ej: Correo electronico" required />
                </div>
                <div>
                    <label for="resultado">Resultado:</label>
                    <input v-model="resultadoAccion" type="text" id="resultado" placeholder="ej: Pago completado" required />
                </div>
                <button type="submit">Enviar Retroalimentación</button>
                </form>
                
                <table>
                <thead>
                    <tr>
                    <th>Deudor</th>
                    <th>Acción</th>
                    <th>Resultado</th>
                    <th>Fecha</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="deudor in deudores" :key="deudor.nombre">
                        <td>{{ deudor.nombre }}</td>
                    </tr>
                </tbody>
                </table>
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import Menu_P from './Menu-.vue';
  
  export default {
    name: 'Nuevo_Procesamiento-',
    components: { Menu_P },
    data() {
      return {
        busqueda: "",
        isCollapsed: true,
        usuarioLogueado: "",
        nuevoDeudor: "",         // Nuevo campo para ingresar deudores
        nuevaAccion: "",         // Nuevo campo para seleccionar acción
        resultados: [],          // Resultados procesados
      };
    },
    methods: {
      toggleSidebar() {
        this.isCollapsed = !this.isCollapsed;
      },
      logout() {
        this.$keycloak.logout();
      },
      async enviarDatos() {
        const datos = {
          deudores: this.nuevoDeudor.split(',').map(deudor => deudor.trim()), // Procesar la entrada
          accion_predicha: this.nuevaAccion,
        };
  
        try {
          const response = await fetch('/api/procesar_datos', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(datos),
          });
  
          if (response.ok) {
            this.resultados = await response.json(); // Obtener nuevos resultados procesados
            this.nuevoDeudor = ""; // Limpiar el campo
            this.nuevaAccion = ""; // Limpiar el campo
          } else {
            console.error('Error al enviar los datos:', response.statusText);
          }
        } catch (error) {
          console.error('Error al procesar los datos:', error);
        }
      },
      async fetchResultados() {
        // Aquí puedes implementar la lógica para obtener los resultados iniciales
      }
    },
    mounted() {
      if (this.$keycloak && this.$keycloak.authenticated) {
        this.usuarioLogueado = this.$keycloak.tokenParsed.preferred_username || "Usuario desconocido";
      }
      this.fetchResultados(); // Llama a la función para obtener los resultados iniciales
    },
  };
  </script>
  
  <style>
  /* Estilos personalizados */
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 8px;
    border: 1px solid #ccc;
    text-align: left;
  }
  th {
    background-color: #f2f2f2;
  }
  form {
    margin-bottom: 20px;
  }
  </style>
  