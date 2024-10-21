# Generated by Django 5.1.2 on 2024-10-21 12:34

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('livre', 'Livre'), ('cd', 'CD'), ('dvd', 'DVD'), ('jeu', 'Jeu de plateau')], max_length=10)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_emprunts', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField(auto_now_add=True)),
                ('date_due', models.DateTimeField(default=datetime.datetime(2024, 10, 28, 12, 34, 12, 69818, tzinfo=datetime.timezone.utc))),
                ('date_retour', models.DateTimeField(blank=True, null=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.media')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.membre')),
            ],
        ),
    ]
