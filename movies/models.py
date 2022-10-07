from django.db import models

# Create your models here.
class Movie(models.Model):
    isim = models.CharField(max_length=100, verbose_name='Film resmi')
    resim = models.FileField(upload_to='filmler/', verbose_name='Film resmi')
    
    def __str__(self):
        return self.isim