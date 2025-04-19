<template>
    <div>
        <h1>{{ msg }}</h1>
        <p>Bem-vindo à nossa empresa! Nós nos dedicamos a oferecer as melhores soluções para nossos clientes.</p>
    </div>
</template>

<script>
    export default {
    name: 'About',
    data() {
        return {
        msg: 'XPTO'
        }
    }
    }
</script>

<style scoped>
    p {
        font-size: 16px;
        color: #333;
        line-height: 1.5;
    }
</style>