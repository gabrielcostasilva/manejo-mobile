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
          <ion-label>{{ ur.name }}</ion-label>
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

import { ref } from 'vue'

import Localbase from 'localbase'
const db = new Localbase('manejo')

const urs = ref([])

db.collection('urs')
  .get()
  .then((results) => (urs.value = results))

</script>