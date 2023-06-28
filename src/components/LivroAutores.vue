<script setup>

const props = defineProps(["autores"])

</script>

<template>
    <div>
        <p v-for="autor, index in props.autores" :key="index">
            {{ autor.nome }}
        </p>
    </div>
</template>