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
</script>
