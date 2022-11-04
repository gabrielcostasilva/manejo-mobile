import { createRouter, createWebHistory } from '@ionic/vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/main/Home.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
