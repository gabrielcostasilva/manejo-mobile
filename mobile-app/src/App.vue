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

import { API, graphqlOperation, Hub } from 'aws-amplify'

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

const ListEvents = `query {
  listarTodas {
    id
    name
  }
}`

const updateLocalCache = () => {
  API.graphql(graphqlOperation(ListEvents))
    .then((result) => {
      db.collection('urs')
        .set(result.data.listarTodas)
    })
    .catch((err) => {
      console.error(err)
    })
}
</script>
