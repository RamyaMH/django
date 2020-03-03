<template>
  <v-card>
    <h4 v-if="user_groups.includes('Admin')">Hello {{username}}, you are Admin!</h4>
    <h4 v-if="user_groups.includes('CP')">Hello {{username}}, you are CP!</h4>
    <h4 v-if="user_groups.includes('Reviewer')">Hello {{username}}, you are Reviewer!</h4>
    <h4 v-if="user_groups.includes('Author')">Hello {{username}}, you are an Author!</h4>
    <h1>{{ msg }}</h1>
    <v-card-title>
      <v-text-field
        v-model='search'
        append-icon='search'
        label='Search'
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers='headers'
      :items='employeeList'
      :search='search'
    ></v-data-table>
    <v-button type='submit' v-on:click="signOut()" class='btn btn-block btn-primary'>Sign Out</v-button>
  </v-card>
</template>

<script>
export default {
  name: 'EmployeeList',
  data () {
    return {
      search: '',
      employeeList: [],
      user_groups: [],
      user_id: '',
      username: '',
      msg: 'Employees list is displayed here',
      headers: [
        {
          text: 'Full Name',
          align: 'left',
          filterable: false,
          value: 'full_name'
        },
        { text: 'Mobile', value: 'mobile' },
        { text: 'Position', value: 'pos' }
      ]
    }
  },
  mounted () {
    this.getAllEmployeeList()
    this.getUserData()
  },
  methods: {
    getAllEmployeeList: function () {
      const baseURI = 'http://localhost:8000/employee/all/'
      this.axios.get(baseURI)
        .then(response => {
          this.employeeList = response.data
          console.log(this.employeeList)
          for (var e in this.employeeList) {
            console.log(this.employeeList[e].position.title)
            this.employeeList[e].pos = this.employeeList[e].position.title
          }
        })
        .catch((err) => {
          this.loading = false
          console.log(err)
        })
    },
    signOut: function () {
      const baseURI = 'http://localhost:8000/auth/token/logout'
      this.axios.post(baseURI)
        .then(response => {
          sessionStorage.removeItem('authToken')
          sessionStorage.removeItem('username')
          this.axios.defaults.headers.common = {'Authorization': `Token ${response.data.auth_token}`}
          this.$router.push('/')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUserData: function () {
      const URI = 'http://localhost:8000/employee/user/'
      this.axios.get(URI)
        .then(response => {
          this.user_groups = response.data.user_groups
          this.user_id = response.data.id
          this.username = response.data.username
          sessionStorage.setItem('user_id', response.data.id)
          sessionStorage.setItem('user_groups', response.data.user_groups)
          alert(response.data.user_groups)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>
</style>
