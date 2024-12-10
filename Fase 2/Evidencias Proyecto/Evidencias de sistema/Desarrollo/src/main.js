import { createApp } from 'vue'
import App from './App.vue'
import router from './router'    // Importa el router
import '@/assets/Menu.css' // Importa el CSS aquí
import keycloak from './keycloak'


// import Inicio from './components/Inicio-.vue'
// import Cobranza from './components/Cobranza-.vue'
// import Menu_principal from './components/menu_principal.vue'


// createApp(App).mount('#app')
// createApp(Inicio).mount('#Inicio')
// createApp(Cobranza).use(router)
// const app = createApp(App);
createApp(App)
  .use(router)
  .mount('#app')
// createApp(Menu_principal).mount('#menu')



// const keycloak = Keycloak({
//   url: '', // Update to your Keycloak URL
//   realm: 'devnation',
//   clientId: 'vue-app',
// });

// Inicializa Keycloak y luego monta la aplicación Vue
// keycloak
//   .init({ onLoad: 'login-required', pkceMethod: 'S256' })
//   .then(authenticated => {
//     if (!authenticated) {
//       console.warn('No autenticado. Redireccionando al login de Keycloak.');
//       return keycloak.login();
//     }

//     console.log("Token de acceso:", keycloak.token);

//     const app = createApp(App);
//     app.use(router);
//     app.provide('$keycloak', keycloak);
//     app.mount('#app');
//   })
//   .catch(err => {
//     console.error('Error al inicializar Keycloak:', err);
//     alert('Error en la autenticación con Keycloak. Detalles: ' + err);
//   });



// const Keycloak = new Keycloak({
//   url: 'http://localhost:8080', // URL base de tu Keycloak
//   realm: 'Alloxentric',
//   clientId: 'vue-app',
// });


keycloak.init({ onLoad: 'login-required' })
  .then(authenticated => {
    if (!authenticated) {
      console.warn('No autenticado. Redireccionando al login de Keycloak.');
      return keycloak.login();
    }

    console.log("Token de acceso:", keycloak.token);  // Imprimir el token
    // Crea y monta la aplicación Vue después de inicializar Keycloak
    const app = createApp(App);
    app.use(router);
    app.mount('#app');
  })
  .catch(err => {
    console.error('Error al inicializar Keycloak:', err);
  });
