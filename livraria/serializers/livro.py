from rest_framework.serializers import ModelSerializer

from livraria.models import Livros

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
    )
        capa = ImageSerializer(required=False, read_only=True)
    depth = 1
  
    
class LivrosDetailSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)

class LivrosListSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = ["id", "titulo", "preco", "autores", "capa"]
        depth = 1