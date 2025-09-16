<template>
    <q-layout view="lHh Lpr lFf">
        <!-- Header and Drawer only show if not on login -->
        <q-header v-if="showHeaderDrawer" elevated>
            <q-toolbar>
                <q-btn
                    flat
                    dense
                    round
                    icon="menu"
                    aria-label="Menu"
                    @click="toggleLeftDrawer"
                />

                <q-toolbar-title>Quasar App</q-toolbar-title>

                <div>Quasar v{{ $q.version }}</div>
            </q-toolbar>
        </q-header>

        <q-drawer
            v-if="showHeaderDrawer"
            v-model="leftDrawerOpen"
            show-if-above
            bordered
        >
            <q-list>
                <q-item-label header>Essential Links</q-item-label>
                <EssentialLink
                    v-for="link in essentialLinks"
                    :key="link.title"
                    v-bind="link"
                />
            </q-list>
        </q-drawer>

        <q-page-container>
            <router-view/>
        </q-page-container>
    </q-layout>
</template>

<script>
import {defineComponent, ref, computed} from 'vue'
import {useRoute} from 'vue-router'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
    {title: 'Docs', caption: 'quasar.dev', icon: 'school', link: 'https://quasar.dev'},
    {title: 'Github', caption: 'github.com/quasarframework', icon: 'code', link: 'https://github.com/quasarframework'},
    {title: 'Discord Chat Channel', caption: 'chat.quasar.dev', icon: 'chat', link: 'https://chat.quasar.dev'},
    {title: 'Forum', caption: 'forum.quasar.dev', icon: 'record_voice_over', link: 'https://forum.quasar.dev'},
    {title: 'Twitter', caption: '@quasarframework', icon: 'rss_feed', link: 'https://twitter.quasar.dev'},
    {title: 'Facebook', caption: '@QuasarFramework', icon: 'public', link: 'https://facebook.quasar.dev'},
    {
        title: 'Quasar Awesome',
        caption: 'Community Quasar projects',
        icon: 'favorite',
        link: 'https://awesome.quasar.dev'
    }
]

export default defineComponent({
    name: 'MainLayout',
    components: {EssentialLink},

    setup() {
        const route = useRoute()
        const leftDrawerOpen = ref(false)

        // Hide header/drawer on login page
        const showHeaderDrawer = computed(() => route.path !== '/')

        const toggleLeftDrawer = () => {
            leftDrawerOpen.value = !leftDrawerOpen.value
        }

        return {
            essentialLinks: linksList,
            leftDrawerOpen,
            toggleLeftDrawer,
            showHeaderDrawer
        }
    }
})
</script>
