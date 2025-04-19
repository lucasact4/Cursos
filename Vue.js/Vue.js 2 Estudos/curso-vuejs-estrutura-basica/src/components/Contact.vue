<template>
    <p>
        Endereço: {{ msg }}
    </p>
</template>

<script>
    export default {
        name: 'Contact',
        data() {
            return {
                msg: 'Rua dos Bobos, 0 - Bairro: Nenhum - Cidade: Nenhuma - Estado: Nenhum - CEP: 00000-000'
            }
        }
    }
</script>

<style>

</style>