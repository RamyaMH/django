<template>
  <v-app id="app">
    <v-app-bar
      app
      absolute
      color="teal lighten-3"
      dark
      hide-on-scroll
      prominent
      scroll-target=""
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <template v-slot:extension>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider color="yellow"></v-tabs-slider>

          <v-tab v-for="item in items" :key="item">{{ item }}</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-content>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
   <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer absolute class="font-weight-medium">
      <v-col class="text-center" cols="12">&copy; {{ new Date().getFullYear() }}</v-col>
    </v-footer>
  </v-app>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      tab: null,
      items: ['Home', 'Videos', 'About', 'Contact Us']
    }
  }
}
</script>

<style>
</style>
