from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_emprunts = models.IntegerField(default=0)

    def peut_emprunter(self):
        # Un membre ne peut pas emprunter plus de 3 médias et ne peut emprunter s'il a un emprunt en retard.
        emprunts_actifs = self.emprunt_set.filter(date_retour=None)
        if emprunts_actifs.count() >= 3:
            return False
        if emprunts_actifs.filter(date_due__lt=timezone.now()).exists():
            return False
        return True

class Media(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('cd', 'CD'),
        ('dvd', 'DVD'),
        ('jeu', 'Jeu de plateau'),
    ]

    titre = models.CharField(max_length=200)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    disponible = models.BooleanField(default=True)

    def est_disponible_pour_emprunt(self):
        return self.type != 'jeu' and self.disponible

class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField(default=timezone.now() + timedelta(weeks=1))
    date_retour = models.DateTimeField(null=True, blank=True)

    def rendre(self):
        self.date_retour = timezone.now()
        self.save()
        self.media.disponible = True
        self.media.save()