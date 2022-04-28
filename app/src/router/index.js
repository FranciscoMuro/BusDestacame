import { createRouter, createWebHashHistory } from 'vue-router'
import AutobusView from '../views/AutobusView.vue'
import ChoferesView from '../views/ChoferesView.vue'
import PasajerosView from '../views/PasajerosView.vue'
import TrayectosView from '../views/TrayectosView.vue'

const routes = [
  {
    path: '/',
    name: 'autobuses',
    component: AutobusView
  },
  {
    path: '/pasajeros',
    name: 'pasajeros',
    component: PasajerosView
  },
  {
    path: '/trayectos',
    name: 'trayectos',
    component: TrayectosView
  },
  {
    path: '/choferes',
    name: 'choferes',
    component: ChoferesView
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
