<template>
  <div>
    <Reutilizacao />
    <h1>Olá Vue</h1>
    <Reutilizacao />
    <p>Meu nome é {{ nome }} e trabalho como {{ profissao }}</p>
    <Reutilizacao />
    <MultiplosEventos />
    <Reutilizacao />
  </div>
</template>

<script>
  import MultiplosEventos from './MultiplosEventos.vue'
  import Reutilizacao from './Reutilizacao.vue';

  export default {
    name: 'PrimeiroComponente',
    components: {
      MultiplosEventos,
      Reutilizacao
    },
    data() {
      return {
        nome: "Matheus",
        profissao: "Programador"
      }
    }
  }
</script>