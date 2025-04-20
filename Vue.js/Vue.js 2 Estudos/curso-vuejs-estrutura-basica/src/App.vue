<template>
  <div id="app">
    <md-card>
      <md-card-header>
        <div class="md-title">
          Material Design Com Vue.js 2
        </div>
        <div class="md-subhead">
          Com Clayton do http://medium.com/codigorefinado e também no Youtube :D
        </div>
      </md-card-header>
      <md-card-content>
        <md-button class="md-raised md-primary" @click="table()">
          Tabela
        </md-button>
        <md-button class="md-raised md-primary" v-on:click="limpar()">
          Limpar
        </md-button>
      </md-card-content>
      <md-table class="width-custom">
        <md-table-header>
          <md-table-row>
            <md-table-head>Primeiro nome</md-table-head>
            <md-table-head>Sobrenome</md-table-head>
            <md-table-head>E-mail</md-table-head>
          </md-table-row>
        </md-table-header>

        <md-table-body>
          <md-table-row v-for="(contato, index) in contatos" :key="index">
            <md-table-cell>{{ contato.nome }}</md-table-cell>
            <md-table-cell>{{ contato.sobrenome }}</md-table-cell>
            <md-table-cell>{{ contato.email }}</md-table-cell>
          </md-table-row>
        </md-table-body>
      </md-table>
    </md-card>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      contatos: [
        {     
          nome: 'Clayton',
          sobrenome: 'Passos',
          email: 'clayton.passos@gmail.com'
        },
        {     
          nome: 'Daniela',
          sobrenome: 'Passos',
          email: 'daniela.passos@gmail.com'
        },
      ]
    }
  },
  methods: {
    table: function () {
      this.contatos.push({
        nome: 'Sebastian',
        sobrenome: 'Seilaoq',
        email: 'seilaoq@gmail.com'
      });
      this.contatos.push({
        nome: 'Sebastian2',
        sobrenome: 'Seilaoq2',
        email: 'seilaoq2@gmail.com'
      });
      this.contatos.push({
        nome: 'Sebastian3',
        sobrenome: 'Seilaoq3',
        email: 'seilaoq3@gmail.com'
      });
    },
    limpar: function () {
      this.contatos.splice(0, this.contatos.length);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.width-custom {
  margin: auto;
  width: 500px;
}
</style>
