from django.contrib import admin

# Register your models here.

from livraria.models import Categoria, Livros, Autor, Editora

admin.site.register(Categoria)
admin.site.register(Livros)
admin.site.register(Autor)
admin.site.register(Editora)
