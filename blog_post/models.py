from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings



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



class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields like features, duration, etc.

class UserSubscription(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

class SubscriptionRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, default="Menunggu Pembayaran")
    date =  models.DateField()
    
    # Other fields like features, duration, etc.