import { createApp} from 'vue'
import { createProvider } from 'vue-cli-plugin-apollo'
import App from './App.vue'

import { router } from '@/router'


// createApp(App).mount('#app')

// new Vue({
//   router,
//   render: (h) => h(App),
// })
const apolloProvider = createProvider({
  httpEndpoint: 'http://localhost:8000/graphql',
  wsEndpoint: null,
})
const app = createApp(App).use(router).use(apolloProvider)
app.mount('#app')