from django.urls import path
from.views import liste_membres, ajouter_membre, liste_medias, ajouter_media, ajouter_emprunt,liste_emprunts, rendre_emprunt


urlpatterns = [
    path('', liste_medias, name='liste_medias'),
    path('membres/', liste_membres, name='liste_membres'),
    path('membre/ajouter/', ajouter_membre, name='ajouter_membre'),
    path('media/ajouter/', ajouter_media, name='ajouter_media'),
    path('emprunts/', liste_emprunts, name='liste_emprunts'),
    path('emprunt/ajouter/', ajouter_emprunt, name='ajouter_emprunt'),
    path('emprunt/<int:emprunt_id>/retourner/', rendre_emprunt, name='rendre_emprunt'),
]