import { createRouter, createWebHistory } from 'vue-router'
import AddMovieFormView from '../views/AddMovieFormView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/movies/create',
      name: 'add-movie',
      component: AddMovieFormView
    },
   
  ]
})

export default router
