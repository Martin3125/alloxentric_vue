// import Keycloak from 'keycloak-js';

// const keycloak = new Keycloak({
//   url: 'http://localhost:8080/admin/Alloxentric/console/', // Cambia esto a la URL de tu servidor Keycloak
//   realm: 'Alloxentric', // Tu realm en Keycloak
//   clientId: 'vue-app', // Tu Client ID
// });

// // Inicializa Keycloak
// // En tu componente

// // keycloak.init({ onLoad: 'login-required' })
// //     .then(authenticated => {
// //         if (authenticated) {
// //             console.log('Usuario autenticado');
// //         } else {
// //             console.warn('Usuario no autenticado');
// //         }
// //     })
// //     .catch(err => {
// //         console.error('Error al inicializar Keycloak:', err);
// //     });


// export default keycloak;

import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080', // URL base de tu Keycloak
  realm: 'Alloxentric',
  clientId: 'vue-app',
});

export default keycloak;
