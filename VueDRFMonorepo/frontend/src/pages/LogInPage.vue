<template>
    <q-page class="row justify-center items-center window-height">
        <q-card class="q-pa-xl" style="width: 350px">
            <q-card-section class="text-h6">Login</q-card-section>

            <q-card-section>
                <q-form @submit.prevent="login">
                    <q-input
                        v-model="email"
                        type="email"
                        label="Email"
                        dense
                        outlined
                        required
                        class="q-mb-md"
                    />

                    <q-input
                        v-model="password"
                        type="password"
                        label="Password"
                        dense
                        outlined
                        required
                        class="q-mb-md"
                    />

                    <q-btn type="submit" label="Login" color="primary" class="full-width q-mb-sm"/>

                    <div class="text-center">
                        <q-btn
                            flat
                            label="Register"
                            color="secondary"
                            @click="goToRegister"
                            class="q-mt-sm"
                        />
                    </div>
                </q-form>
            </q-card-section>
        </q-card>
    </q-page>
</template>

<script setup>
import {ref} from 'vue';
import {useRouter} from 'vue-router';

const email = ref('');
const password = ref('');
const router = useRouter();

const ADMIN_EMAIL = import.meta.env.VITE_DUMMY_USER
const ADMIN_PASSWORD = import.meta.env.VITE_DUMMY_PASSWORD

function login() {
    if(email.value === ADMIN_EMAIL && password.value === ADMIN_PASSWORD){
        router.push('/dashboard')
    }else{
        alert("Please check your email or password")
    }
}

function goToRegister() {
    router.push('/register');
}
</script>

<style scoped>
/* optional styling */
</style>
