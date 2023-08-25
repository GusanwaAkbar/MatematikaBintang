from django.db import models
from django.utils.text import slugify

# Create your models here.

#blog Post Models

#Judul

#Isi Video

#Deskripsi

# Map Model for Materi

#List Mate pelajaran

class kelas(models.Model):
    kelas = models.TextField()

    def __str__ (self):
        return "{}".format(self.kelas)

class bab (models.Model):
    bab = models.TextField()
    kelas = models.ManyToManyField(kelas)

    def __str__ (self):
        return "{}".format(self.bab)

class materi(models.Model):
    judul = models.TextField()
    link = models.TextField()
    deskripsi = models.TextField()
    bab = models.ManyToManyField(bab)
    kelas = models.ManyToManyField(kelas)

    slug = models.SlugField(blank = True)

    def save(self):
        self.slug = slugify(self.judul)
        super(materi,self).save()


    def __str__ (self):
        return "{}".format(self.judul)