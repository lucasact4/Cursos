<template>
  <div>
    <p v-if="esta_trabalhando">Estou trabalhando no momento.</p>
    <p v-else>Estou em busca de novas oportunidades.</p>
    <p>Utilizo as seguintes tecnologias:</p>
    <ul>
      <li>JavaScript</li>
      <li>PHP</li>
      <li>Python</li>
    </ul>
    <div>

      <button @click="showEmail">{{ textoBotao }}</button>
    </div>
    <p v-show="mostrar_email">Mande uma mensagem para: {{ email }}</p>
    <p class="teste">Para acessar meu portfólio basta <a v-bind:href="meu_link" target="_blank">clicar aqui</a></p>
    <Picture />
  </div>
</template>
<script>
  import Picture from './Picture.vue'
  export default {
    name: 'Info',
    components: {
      Picture
    },
    created() {
      this.showEmail()
    },
    data() {
      return {
        esta_trabalhando: true,
        mostrar_email: true,
        email: 'funcraftact4@outlook.com',
        meu_link: 'https://google.com',
        textoBotao: 'Mostrar e-mail'
      }
    },
    methods: {
      showEmail() {
        this.mostrar_email = !this.mostrar_email
        this.stateEmail()
      },
      stateEmail() {
        if(!this.mostrar_email) {
          this.textoBotao = 'Mostrar e-mail'
        } else {
          this.textoBotao = 'Esconder e-mail'
        }
      }
    }
  }
</script>

<style>
  .paragrafo-pai {
    color: red;
  }
</style>