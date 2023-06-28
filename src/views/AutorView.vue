<script>
import AutorApi from "@/api/autor";
const autorApi = new AutorApi();
export default {
  data() {
    return {
      autores: [],
      autor: {},
    };
  },
  async created() {
    this.autores = await autorApi.buscarTodosOsAutores();
  },
  methods: {
    async salvar() {
      if (this.autor.id) {
        await autorApi.atualizarAutor(this.autor);
      } else {
        await autorApi.adicionarAutor(this.autor);
      }
      this.autor = {};
      this.autores = await autorApi.buscarTodosOsAutores();
    },
    editar(autor) {
      Object.assign(this.autor, autor);
    },
    async excluir(autor) {
      await autorApi.excluirAutor(autor.id);
      this.autores = await autorApi.buscarTodosOsAutores();
    },
  },
};
</script>

<template>
  <h1>Autores</h1>
  <hr />
  <div class="form">
    <input type="text" v-model="autor.nome" placeholder="Nome" />
    <input type="email" v-model="autor.email" placeholder="Email" />
    <button @click="salvar">Salvar</button>
  </div>
  <hr />
  <ul>
    <li v-for="autor in autores" :key="autor.id">
      <span @click="editar(autor)"
        >({{ autor.id }}) - {{ autor.nome }} - {{ autor.email }}</span
      >
      <button @click="excluir(autor)">X</button>
    </li>
  </ul>
</template>
