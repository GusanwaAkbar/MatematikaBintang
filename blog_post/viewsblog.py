from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime 




from .models import kelas
from .models import bab
from .models import materi
from django.utils.text import slugify

from .models import SubscriptionRequest
from .models import SubscriptionPlan

# Create your views here.
def post (request):

    KELAS = kelas.objects.all()

    slugkelas = []

    for x in KELAS:
        slugkelas.append(materi.objects.filter(kelas__kelas = x).first)

    listkelas = zip(KELAS,slugkelas)

    context = {
        "slugkelas" : listkelas,

    }

    return render(request,'blogpost3 copy.html',context)


def pricing (request):

    KELAS = kelas.objects.all()

    slugkelas = []

    for x in KELAS:
        slugkelas.append(materi.objects.filter(kelas__kelas = x).first)

    listkelas = zip(KELAS,slugkelas)

    context = {
        "slugkelas" : listkelas,

    }

    return render(request,'pricing.html',context)


def pesan_smp3(request):


    user = request.user
    plan = SubscriptionPlan.objects.get(name='smp-kelas-3')    
    price = 70000
    date = datetime.now()

    pesanan = SubscriptionRequest(user=user, subscription_plan=plan, price=price, date=date )
    pesanan.save()


    return redirect('pesananku')


def pesananku (request):

    list_pesanan = SubscriptionRequest.objects.all()

    context = {

    "pesanan" : list_pesanan,

    }

    return render(request,'pesananku.html',context)


def adminview(request):

    kelas = kelas.objects.all()
    bab = bab.objects.all()
    materi = materi.objects.all()


def detailpost (request,slugInput):

    Materi = materi.objects.get(slug = slugInput) #daatkan materi sesuai slug
    
    Bab = bab.objects.get(materi__judul = Materi) # dapatkan nama bab darimateri yang sedang di akses
    Kelas = kelas.objects.get(materi__judul = Materi) # dapatkan nama kelas dari materi yang sedang di akses

    listBab = bab.objects.filter(kelas__kelas = Kelas) #dapatkan semua bab dengan filter kelas
    listMateri = materi.objects.filter(bab__bab = Bab) #dapatkan semua materi dengan filter bab

    Slugbab = []

    for x in listBab:

        Slugbab.append(materi.objects.filter(bab__bab = x).first )

    babslug = zip(listBab,Slugbab)


    



  


    context = {
        "Judul" : Materi, #title
        "Bab"   : Bab, #list Bab
        "Materi"    : listMateri , #list Materi
        "Slug"  : slugInput, #list Slug
        "Slugbab" : Slugbab ,
        "babslug" : babslug ,
        "kelas" : Kelas
        
        

    }
    


    return render(request,'blogpost3 detail.html',context)

