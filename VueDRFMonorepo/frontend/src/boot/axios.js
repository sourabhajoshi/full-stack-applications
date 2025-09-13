import {boot} from 'quasar/wrappers'
import axios from 'axios'

const api = axios.create({baseURL: '/api'})

export default boot(({app}) => {
    // make it available in Vue components as this.$api (Options API)
    app.config.globalProperties.$api = api
})

export {api}
