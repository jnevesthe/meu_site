from django.urls import path
from .views import Index, Sobre
from django.http import FileResponse
import os

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    
    # Rota para ads.txt
    path("ads.txt", lambda request: FileResponse(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "ads.txt"), "rb"))),
]
