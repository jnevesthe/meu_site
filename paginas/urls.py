from django.urls import path
from .views import Index, Sobre

urlpatterns=[
    
    path("", Index.as_view(), name="index"),
    path("sobre/", Sobre.as_view(), name="sobre"),
]