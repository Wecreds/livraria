from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Autor, Livros



class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"
        depth = 1

class LivrosDetailSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"
        depth = 1

class LivrosListSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = ["id", "titulo", "preco", "autores"]
        depth = 1