from django.urls import path 
from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete

urlpatterns=[
    
    path('cadastro/', CampoCreate.as_view(), name='cadastro'),
    path('cadastro/atividade', AtividadeCreate.as_view(), name='atividade'),
    
    path('editar/cadastro/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),
    
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
]