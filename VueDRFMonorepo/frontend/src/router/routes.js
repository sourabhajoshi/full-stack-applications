import LogInPage from 'pages/LogInPage.vue'
import RegisterPage from "pages/RegisterPage.vue";

const routes = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [
            {path: '', name: 'login', component: LogInPage},
            {path: 'register', component: RegisterPage}
        ]
    },
    {
        path: '/register',
        component: () => import('layouts/MainLayout.vue'),
        children: [
            {path: '', name: 'login', component: LogInPage},
        ]
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: '/:catchAll(.*)*',
        component: () => import('pages/ErrorNotFound.vue')
    }
]

export default routes
