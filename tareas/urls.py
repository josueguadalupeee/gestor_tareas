from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista, name="lista"),
    path("tarea/<int:pk>/alternar/", views.alternar, name="alternar"),
    path("tarea/<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]
