import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { IonicVue } from '@ionic/vue'

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css'

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css'
import '@ionic/vue/css/structure.css'
import '@ionic/vue/css/typography.css'

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css'
import '@ionic/vue/css/float-elements.css'
import '@ionic/vue/css/text-alignment.css'
import '@ionic/vue/css/text-transformation.css'
import '@ionic/vue/css/flex-utils.css'
import '@ionic/vue/css/display.css'

import '@aws-amplify/ui-vue/styles.css'
import { Amplify, Auth, API } from 'aws-amplify'
import './registerServiceWorker'

Amplify.configure({
  Auth: {
    region: process.env.VUE_APP_REGION,
    userPoolId: process.env.VUE_APP_USER_POOL_ID,
    userPoolWebClientId: process.env.VUE_APP_USER_POOL_WEB_CLIENT_ID,
  },
  API: {
    aws_appsync_graphqlEndpoint:
      process.env.VUE_APP_AWS_APPSYNC_GRAPHQL_ENDPOINT,
    aws_appsync_region: process.env.VUE_APP_AWS_APPSYNC_REGION,
    aws_appsync_authenticationType:
      process.env.VUE_APP_AWS_APPSYNC_AUTHENTICATION_TYPE
  },
})

const app = createApp(App).use(IonicVue).use(router)

router.isReady().then(() => {
  app.mount('#app')
})
