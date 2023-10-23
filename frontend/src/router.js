import * as Vue from 'vue'
import * as VueRouter from 'vue-router'

import Post from '@/components/Post'
import Author from '@/components/Author'
import PostsByTag from '@/components/PostsByTag'
import AllPosts from '@/components/AllPosts'
import App from '@/App'
// Vue.use(VueRouter)

const routes = [
  { path: '/author/:username', component: Author },
  { path: '/post/:slug', component: Post },
  { path: '/tag/:tag', component: PostsByTag },
  { path: '/', component: AllPosts },
]

export const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),
  routes,
})
// export default router
Vue.createApp(App).use(router).mount('#app')