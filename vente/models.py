from django.db import models

# Create your models here.
class form_contact(models.Model):
    nom = models.CharField(max_length=200)
    sujet = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.nom