//router.ts
import Vue from 'vue';
import Router from 'vue-router';
import Choose from '../components/Choose.vue';
import Detective from '../components/Detective.vue';
import Mrx from '../components/Mrx.vue';
import Login from '../components/Login.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: Home,
    // },
    {
      path: '/',
      name: 'Login',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Login// () => import(/* webpackChunkName: "about" */ '../components/choose.vue'),
    },
    {
      path: '/choose',
      name: 'choose',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Choose// () => import(/* webpackChunkName: "about" */ '../components/choose.vue'),
    },
    {
      path: '/detective',
      name: 'detective',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Detective// () => import(/* webpackChunkName: "about" */ '../components/choose.vue'),
    },
    {
      path: '/mrx',
      name: 'mrx',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Mrx// () => import(/* webpackChunkName: "about" */ '../components/choose.vue'),
    },
  ],
});