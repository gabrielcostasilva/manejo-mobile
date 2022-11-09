<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Minhas URs</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <ion-list>
        <ion-item v-for="ur in urs" :key="ur.id">
          <ion-label>{{ ur.nome }}</ion-label>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script setup>
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonList,
  IonItem,
  IonLabel,
} from '@ionic/vue'

import { API, graphqlOperation } from 'aws-amplify'
import { ref } from 'vue'

const ListEvents = `query {
  listarTodas {
    id
    nome
  }
}`

const urs = ref([])

API.graphql(graphqlOperation(ListEvents))
  .then((result) => urs.value = result.data.listarTodas)
  .catch((err) => console.err('oops', err))
</script>
