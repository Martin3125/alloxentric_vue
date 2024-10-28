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
const app = createApp(App);
createApp(App)
  .use(router)
  .mount('#app')
// createApp(Menu_principal).mount('#menu')



// const keycloak = Keycloak({
//   url: 'http://localhost:8080/auth', // Update to your Keycloak URL
//   realm: 'devnation',
//   clientId: 'vue-app',
// });

keycloak.init({ onLoad: 'login-required' }).then(authenticated => {
  if (authenticated) {
      console.log('Authenticated');
      app.mount('#app');
  } else {
      console.log('Not authenticated');
  }
}).catch(error => {
  console.error('Failed to initialize Keycloak', error);
});