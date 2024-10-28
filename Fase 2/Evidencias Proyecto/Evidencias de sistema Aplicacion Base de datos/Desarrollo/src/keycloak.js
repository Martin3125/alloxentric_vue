import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
    url: 'http://localhost:8080/auth',
    realm: 'Alloxentric', // Reemplaza con el nombre de tu realm
    clientId: 'vue-app', // El ID de cliente que configuraste en Keycloak
});

export default keycloak;
