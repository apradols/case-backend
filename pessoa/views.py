from rest_framework import viewsets
from pessoa.models import Pessoa
from pessoa.serializer import PessoaSerializer

class PessoaViewsSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
