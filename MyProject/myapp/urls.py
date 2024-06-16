from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("home/", index, name="index"),
    path("nbook", spa, name="pagina"),
    path("itens/cadastrar/", create, name="criar_item"),
    path("itens/editar/<int:id>", edit, name="editar_item"),
    path("itens/atualizar/<int:id>", update, name="atualizar_item"),
    path("itens/visualizar/<int:id>", read, name="visualizar_item"),
    path("itens/deletar/<int:id>", delete, name="deletar_item"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
