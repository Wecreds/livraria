<template>
  <header>
    <router-link :to="{ name: 'home' }">Home</router-link>
    <router-link to="/categorias">Categorias</router-link>
    <router-link to="/livros">Livros</router-link>
    <router-link to="/editoras">Editoras</router-link>
    <router-link to="/autores">Autores</router-link>
  
  </header>
  <main>
    <RouterView />
  </main>
</template>
