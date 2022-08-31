from django.forms import ModelForm
from .models import Camisas, Short, Calcados

class CamisasForm(ModelForm):
    class Meta:
           model = Camisas
           fields = ['tamanho', 'marca', 'tipo', 'nome', 'ano', 'personalizacao', 'foto']

class ShortForm(ModelForm):
    class Meta:
           model = Short
           fields = ['modelo', 'tamanho','marca','tipo','foto']

class CForm(ModelForm):
    class Meta:
           model = Calcados
           fields = ['modelo', 'tamanho','marca','marca','foto']