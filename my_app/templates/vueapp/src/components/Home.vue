<template>
  <v-card id="id1" class="mx-auto" max-width="400">
    <h1>{{ msg }}</h1>
    <router-link :to="{ name: 'EmployeeList'}">list</router-link>
    <router-link :to="{ name: 'UserAuth'}">auth</router-link>
  </v-card>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Welcome to Home page'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#id1 {
  height: 100%;
}
</style>
