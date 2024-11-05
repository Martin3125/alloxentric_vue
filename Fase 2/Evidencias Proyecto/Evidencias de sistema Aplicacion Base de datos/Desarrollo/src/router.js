// src/router.js
// import Vue from 'vue';
import { createRouter, createWebHistory } from 'vue-router'
import Inicio from './components/Inicio-.vue'
// import Login from './components/Login-.vue'
// import Registro from './components/Registro-.vue'
import Cobranza from './components/Cobranza-.vue'
import Cargar_resultados_periodo_anterior from './components/cargar_resultados_periodo_anterior.vue'
import generar_resultados from './components/generar_resultados.vue'
import resultados from './components/resultados-.vue'
import res_periodo_anterior from './components/res_periodo_anterior.vue'
import Reporte_de_desempeño from './components/Reporte_de_desempeño.vue'
import Reporte_de_la_ultima_carga from './components/Reporte_de_la_ultima_carga.vue'
import Settings from './components/Settings.vue'
import Nuevo_Procesamiento from './components/Nuevo_Procesamiento-.vue'


const routes = [
  // { path: '/', component: Login },
  // { path: '/Registro', component: Registro },
  { path: '/', component: Inicio},
  { path: '/cobranza', component: Cobranza },
  { path: '/cargar_resultados', component: Cargar_resultados_periodo_anterior },
  { path: '/generar_resultados', component: generar_resultados },
  { path: '/Nuevo_Procesamiento', component: Nuevo_Procesamiento },
  { path: '/Reporte_de_d', component: Reporte_de_desempeño },
  { path: '/Reporte_de_la_ultima_carga', component: Reporte_de_la_ultima_carga },
  { path: '/resultados', component: resultados },
  { path: '/res_periodo_anterior', component: res_periodo_anterior },
  { path: '/settings', component: Settings },
  

]

const router = createRouter({
  history: createWebHistory(),
  routes
})


export default router
