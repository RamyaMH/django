<template>
<v-flex xs4 class="grey lighten-4">
<v-card>
    <v-tabs
      background-color="white"
      color="deep-purple accent-4"
      right
    >
      <v-tab>Sign in</v-tab>
      <v-tab>Register</v-tab>

      <v-tab-item>
        <v-container fluid>
            <v-text-field prepend-icon="person" name="Username" label="Username" v-model="username"></v-text-field>
            <v-text-field prepend-icon="lock" name="Password" label="Password" type="password" v-model="password"></v-text-field>
            <v-card-actions>
              <v-btn primary large block type='submit' @click='signIn()'>Login</v-btn>
            </v-card-actions>
        </v-container>
      </v-tab-item>
      <v-tab-item>
        <v-container fluid>
            <v-text-field prepend-icon="person" name="Username" label="Username" v-model="username"></v-text-field>
            <v-text-field  prepend-icon="email"  name="email" label="E-mail" v-model="email"></v-text-field>
            <v-text-field prepend-icon="lock" name="Password" label="Password" type="password" v-model="password"></v-text-field>
            <v-text-field prepend-icon="lock" name="Password2" label="Re-type Password" type="password" v-model="password2"></v-text-field>
            <v-card-actions>
              <v-btn primary large block type='submit' @click='signUp()'>Register</v-btn>
            </v-card-actions>
        </v-container>
      </v-tab-item>
    </v-tabs>
  </v-card>
</v-flex>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      username: '',
      password: '',
      password2: ''
    }
  },
  methods: {
    signUp () {
      const credentials = { username: this.username, password: this.password, re_password: this.password2, email: this.email }
      this.axios.post('http://localhost:8000/auth/users/', credentials)
        .then(response => {
          alert(
            'Your account has been created. You will be signed in automatically'
          )
          this.signIn()
        }).fail(response => {
          alert(response.responseText)
        })
    },
    signIn: function () {
      console.log('in signin')
      const credentials = { username: this.username, password: this.password }
      const baseURI = 'http://localhost:8000/auth/token/login'
      this.axios.post(baseURI, credentials)
        .then(response => {
          sessionStorage.setItem('authToken', response.data.auth_token)
          sessionStorage.setItem('username', this.username)
          this.axios.defaults.headers.common = {'Authorization': `Token ${response.data.auth_token}`}
          this.$router.push('/list')
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>

</style>
