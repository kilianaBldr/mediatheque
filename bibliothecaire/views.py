from django.shortcuts import render, get_object_or_404, redirect
from .models import Membre, Media, Emprunt

def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliothecaire/liste_membres.html', {'membres': membres})

def ajouter_membre(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'])
        membre = Membre.objects.create(user=user)
        return redirect('liste_membres')
    return render(request, 'bibliothecaire/ajouter_membre.html')

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/liste_medias.html', {'medias': medias})

def ajouter_media(request):
    if request.method == 'POST':
        media = Media.objects.create(
            titre=request.POST['titre'],
            type=request.POST['type'],
            disponible=True
        )
        return redirect('liste_medias')
    return render(request, 'bibliothecaire/ajouter_media.html')

def ajouter_emprunt(request):
    if request.method == 'POST':
        membre = get_object_or_404(Membre, pk=request.POST['membre_id'])
        media = get_object_or_404(Media, pk=request.POST['media_id'])
        if membre.peut_emprunter() and media.est_disponible_pour_emprunt():
            Emprunt.objects.create(membre=membre, media=media)
            media.disponible = False
            media.save()
            return redirect('liste_emprunts')
    membres = Membre.objects.all()
    medias = Media.objects.filter(disponible=True)
    return render(request, 'bibliothecaire/ajouter_emprunt.html', {'membres': membres, 'medias': medias})

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'bibliothecaire/liste_emprunts.html', {'emprunts': emprunts})

def rendre_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, pk=emprunt_id)
    emprunt.rendre()
    return redirect('liste_emprunts')