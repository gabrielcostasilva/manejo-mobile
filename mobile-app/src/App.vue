<template>
  <ion-app>
    <authenticator>
      <ion-router-outlet />
    </authenticator>
  </ion-app>
</template>

<script setup>
import { IonApp, IonRouterOutlet } from '@ionic/vue'
import { Authenticator } from '@aws-amplify/ui-vue'

import { API, graphqlOperation, Hub, Auth } from 'aws-amplify'

import Localbase from 'localbase'

const listener = (data) => {
  switch (data.payload.event) {
    case 'signIn':
    case 'autoSignIn':
      console.log('user signed in')
      updateLocalCache()
      break

    case 'signOut':
      console.log('user signed out')
      break
  }
}

Hub.listen('auth', listener)

const db = new Localbase('manejo')

let currentAuthenticatedUser = null

const ListEvents = `query listarTodasPorEmail($email: String!) {
  listarTodas(user_email: $email) {
    id
    name
  }
}`



const updateLocalCache = async () => {
  currentAuthenticatedUser = await Auth.currentAuthenticatedUser()

  API.graphql(graphqlOperation(ListEvents, { email: currentAuthenticatedUser.username }))
    .then((result) => {
      db.collection('urs')
        .set(result.data.listarTodas)
    })
    .catch((err) => {
      console.error(err)
    })
}
</script>
