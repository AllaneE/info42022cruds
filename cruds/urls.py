"""cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import short_listar,camisas_listar,calcados_listar,acessorios_listar
from core.views import acessorios_cadastrar,camisas_cadastrar,calcados_cadastrar, short_cadastrar
from core.views import short_editar, camisas_editar,calcados_editar,acessorios_editar
from core.views import short_remover,camisas_remover,calcados_remover,acessorios_remover, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),

   
    #url de camisas
    path('camisas/', camisas_listar, name= 'listar_camisas'),
    path('camisa_cadastro/', camisas_cadastrar, name='camisa_cadastro'),
    path('camisa_editar/<int:id>/',camisas_editar, name='camisa_editar'),
    path('camisa_remover/<int:id>/', camisas_remover, name= 'camisa_remover'),


    #url de calcados
    path('calcados/', calcados_listar, name= 'listar_calcados'),
    path('calcados_cadastro/', calcados_cadastrar, name='calcado_cadastro'),
    path('calcados_editar/<int:id>/', calcados_editar, name='calcado_editar'),
    path('calcados_remover/<int:id>/', calcados_remover, name= 'calcado_remover'),


    #url de shorts
    path('short/', short_listar, name= 'listar_shorts'),
    path('short_cadastro/', short_cadastrar, name='short_cadastro'),
    path('short_editar/<int:id>/',short_editar, name='short_editar'),
    path('short_remover/<int:id>/', short_remover, name= 'short_remover'),


    #url de acessorios
    path('acessorios/', acessorios_listar, name= 'listar_acessorios'),
    path('acessorios_cadastro/', acessorios_cadastrar, name='acessorio_cadastro'),
    path('acessorios_editar/<int:id>/', acessorios_editar, name='acessorio_editar'),
    path('acessorios_remover/<int:id>/', acessorios_remover, name= 'acessorio_remover'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
