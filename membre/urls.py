from django.urls import path
from . import views  # Assurez-vous que vous avez bien des vues définies dans views.py

urlpatterns = [
    path('', views.liste_medias, name='liste_medias'),  # Par exemple, une vue pour la page d'accueil
]
