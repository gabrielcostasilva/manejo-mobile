<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Minhas URs</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <ion-list>
        <ion-item v-for="ur in urs" :key="ur">
          <ion-label>{{ ur }}</ion-label>
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
  IonLabel
} from '@ionic/vue'

const urs = [
  'Pokémon Yellow',
  'Mega Man X',
  'The Legend of Zelda',
  'Pac-Man',
  'Super Mario World',
]
</script>
