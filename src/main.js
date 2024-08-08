// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Inicio from './components/Inicio-.vue'
import Cobranza from './components/Cobranza-.vue'
import router from './router'    // Importa el router
// import Menu_principal from './components/menu_principal.vue'

createApp(App).mount('#app')
createApp(Inicio).mount('#Inicio')
createApp(Cobranza).use(router)
// createApp(Menu_principal).mount('#menu')


