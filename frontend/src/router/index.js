import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListCanchas from '@/components/cancha/ListCanchas'
import ListReservas from '@/components/cancha/ListReservas'
import NewReserva from '@/components/cancha/NewReserva'
import EditReserva from '@/components/cancha/EditReserva'
import DeleteReserva from '@/components/cancha/DeleteReserva'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/canchas',
      name: 'ListCanchas',
      component: ListCanchas
    },
    {
      path: '/reservas',
      name: 'ListReservas',
      component: ListReservas
    },
    {
      path: '/reservas/new',
      name: 'NewReserva',
      component: NewReserva
    },
    {
      path: '/reservas/:reservaId/edit',
      name: 'EditReserva',
      component: EditReserva
    },
    {
      path: '/reservas/:reservaId/delete',
      name: 'DeleteReserva',
      component: DeleteReserva
    },
  ],
  mode: 'history'
})
