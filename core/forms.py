from pyexpat import model
from django.forms import ModelForm
from .models import Camisas, Short, Calcados, Acessorios

class CamisasForm(ModelForm):
    class Meta:
        model = Camisas
        fields = ['tamanho', 'marca', 'tipo', 'nome', 'ano', 'personalizacao', 'foto', 'quantidade']

class ShortForm(ModelForm):
    class Meta:
        model = Short
        fields = ['modelo', 'tamanho','marca','tipo','foto' ,'quantidade']

class CalcadosForm(ModelForm):
    class Meta:
        model = Calcados
        fields = ['modelo', 'tamanho','marca','tipo','foto', 'quantidade']

class AcessoriosForm(ModelForm):
    class Meta:
        model = Acessorios
        fields = ['nome','tipo','marca','esporte','foto','quantidade']