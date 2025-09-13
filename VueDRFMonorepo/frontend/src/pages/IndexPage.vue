<template>
    <q-page padding>
        <q-btn label="Call Backend" @click="callApi"/>
        <div style="margin-top: 12px;">
            <strong v-if="loading">Loading...</strong>
            <div v-if="message">Response: {{ message }}</div>
            <div v-if="error" style="color: red">Error: {{ error }}</div>
        </div>
    </q-page>
</template>
<script setup>
import {ref} from 'vue'
import {api} from 'boot/axios' // our axios instance
const message = ref('')
const error = ref(null)
const loading = ref(false)

async function callApi() {
    loading.value = true
    error.value = null
    try {
// Because baseURL is '/api', this will call '/api/hello/'

        const res = await api.get('/hello/')
        message.value = res.data.message
    } catch (err) {
        console.error(err)
        error.value = err?.response?.data || err.message
    } finally {
        loading.value = false
    }
}
</script>
