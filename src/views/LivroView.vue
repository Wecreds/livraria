<script>
import LivrosApi from "../api/livros";
const livrosApi = new LivrosApi();

import CategoriasApi from "@/api/categorias";
const categoriasApi = new CategoriasApi();

import EditorasApi from "@/api/editora";
const editorasApi = new EditorasApi();

import AutorApi from "@/api/autor";
const autorApi = new AutorApi();
import LivroAutores from "../components/LivroAutores.vue";

export default {
  data() {
    return {
      livros: [],
      livro: {},
      categorias: [],
      editoras: [],
      autores: [],
    };
  },
  async created() {
    this.livros = await livrosApi.buscarTodosOsLivros();
    this.categorias = await categoriasApi.buscarTodasAsCategorias();
    this.editoras = await editorasApi.buscarTodosOsEditoras();
    this.autores = await autorApi.buscarTodosOsAutores();
  },
  methods: {
    async salvar() {
      if (this.livros.id) {
        await livrosApi.atualizarLivro(this.livro);
      } else {
        await livrosApi.adicionarLivro(this.livro);
      }
      this.livro = {};
      this.livros = await livrosApi.buscarTodosOsLivros();
    },
    editar(livro) {
      Object.assign(this.livro, livro);
    },
    async excluir(livro) {
      await livrosApi.excluirLivro(livro.id);
      this.livros = await livrosApi.buscarTodosOsLivros();
    },
  },
  components: { LivroAutores },
};
</script>

<template>
  <h1>Livros</h1>
  <hr />
  <div class="form">
    <input type="text" v-model="livro.titulo" placeholder="Titulo" />
    <input type="number" v-model="livro.preco" placeholder="Preço" />
    <input
      type="text"
      maxlength="32"
      v-model="livro.isbn"
      placeholder="ISBN (Opcional)"
    />
    <input type="number" v-model="livro.quantidade" placeholder="Quantidade" />
    Categoria:
    <select v-model="livro.categoria">
      <option
        v-for="categoria in categorias"
        :key="categoria.id"
        :value="categoria.id"
      >
        {{ categoria.descricao }}
      </option>
    </select>
    Editora:
    <select v-model="livro.editora">
      <option v-for="editora in editoras" :key="editora.id" :value="editora.id">
        {{ editora.nome }}
      </option>
    </select>
    <br />
    Autores:
    <select multiple v-model="livro.autores">
      <option v-for="autor in autores" :key="autor.id" :value="autor.id">
        {{ autor.nome }}
      </option>
    </select>
    <button @click="salvar">Salvar</button>
  </div>
  <hr />
  <ul>
    <li v-for="livro in livros" :key="livro.id">
      <span @click="editar(livro)">
        ({{ livro.id }}) - {{ livro.titulo }} - R${{ livro.preco }} -
        <LivroAutores :autores="livro.autores" />
      </span>
      <button @click="excluir(livro)">X</button>
    </li>
  </ul>
</template>
