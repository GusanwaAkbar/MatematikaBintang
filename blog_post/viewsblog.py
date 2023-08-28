from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime , timedelta




from .models import kelas
from .models import bab
from .models import materi
from .models import SubscriptionPlan

from django.utils.text import slugify

from .models import SubscriptionRequest
from .models import SubscriptionPlan
from .models import UserSubscription


from .forms import KelasUpdateForm
from .forms import BabUpdateForm
from .forms import MateriUpdateForm



from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView



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
    plan = SubscriptionPlan.objects.all()
    bablist = bab.objects.all()

    slugkelas = []

    for x in KELAS:
        slugkelas.append(materi.objects.filter(kelas__kelas = x).first)

    listkelas = zip(KELAS,slugkelas)


    context = {
        "slugkelas" : listkelas,
        "plan": plan,
        "bab": bablist,

    }

    return render(request,'pricing.html',context)

def belikelas(request,id):

    user = request.user
    plan = SubscriptionPlan.objects.get(id = id)

    if request.method == "POST":
        pesanan = SubscriptionRequest(user=user, subscription_plan=plan, date=datetime.now() )
        pesanan.save()

        return redirect('pesananku')

    return redirect('pesananku')

def pesananku (request):

    list_pesanan = SubscriptionRequest.objects.all()

    context = {

    "pesanan" : list_pesanan,

    }

    return render(request,'pesananku.html',context)

def kelasaktif(request):
    user_subscriptions = UserSubscription.objects.filter(user=request.user)
    gotoclass = []

    for x in user_subscriptions:
        m = materi.objects.filter(kelas__kelas=x.kelas).first()
        link = m.slug if m else None
        gotoclass.append(link)

    user_subscriptions_with_links = zip(user_subscriptions, gotoclass)

    context = {
        "user_subscriptions": user_subscriptions_with_links,
    }

    return render(request, 'kelasaktif.html', context)


def adminpesanan (request):

    list_pesanan = SubscriptionRequest.objects.all()

    context = {

    "pesanan" : list_pesanan,

    }

    return render(request,'adminpesanan.html',context)


def adminsetuju(request, id):

    if request.method == 'POST':
        user = request.user
        subscription_request = SubscriptionRequest.objects.get(id = id)
        k = subscription_request.subscription_plan.kelas
        tanggal_pesan = datetime.now()
        durasi = subscription_request.subscription_plan.durasi
        end_date = tanggal_pesan + timedelta(days=durasi)

        

        # Check if user already has a subscription for the same class
        existing_subs = UserSubscription.objects.filter(user=user, kelas=k).first()

        if existing_subs:
            # Update end_date based on existing record and new duration
            existing_end_date = existing_subs.end_date
            new_end_date = existing_end_date + timedelta(days=durasi)
            existing_subs.end_date = new_end_date
            existing_subs.save()

            subscription_request.status = "disetujui"
            subscription_request.save()


            return redirect('admin-pesanan')
        else:
            # Create a new UserSubscription record
            usersubs = UserSubscription(user=user, kelas=k, start_date=tanggal_pesan, end_date=end_date)
            usersubs.save()


            subscription_request.status = "disetujui"
            subscription_request.save()

            return redirect('admin-pesanan')

    return redirect('admin-pesanan')



def pesan_smp3(request):


    user = request.user
    plan = SubscriptionPlan.objects.get(name='smp-kelas-3')    
    price = 70000
    date = datetime.now()

    pesanan = SubscriptionRequest(user=user, subscription_plan=plan, price=price, date=date )
    pesanan.save()


    return redirect('pesananku')





def adminview(request):

    Materi = materi.objects.all() #daatkan materi sesuai slug
    
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


    return render(request, 'adminview.html', context)


def adminkelas(request):
    kelas_objects = kelas.objects.all()
    bab_objects = bab.objects.all()
    materi_objects = materi.objects.all()

    kelas_filter = request.GET.get('kelas_filter')
    bab_filter = request.GET.get('bab_filter')

    if kelas_filter:
        # Apply filter to bab_objects based on selected kelas
        bab_objects = bab.objects.filter(kelas__id=kelas_filter)

    if bab_filter:
        # Apply filter to materi_objects based on selected bab
        materi_objects = materi.objects.filter(bab__id=bab_filter)


    kelasform = KelasUpdateForm()
    babform = BabUpdateForm()
    materiform = MateriUpdateForm()


     


    form_instances = [KelasUpdateForm(instance=kelas_obj) for kelas_obj in kelas_objects]
    form_bab = [BabUpdateForm(instance=bab_object) for bab_object in bab_objects]
    form_materi = [MateriUpdateForm(instance=materi_object) for materi_object in materi_objects]

    kelas_and_forms = zip(kelas_objects, form_instances)
    bab_and_forms = zip(bab_objects, form_bab)
    materi_and_forms = zip(materi_objects, form_materi)

    context = {
        'kelas_and_forms': kelas_and_forms,
        'bab_and_forms': bab_and_forms,
        'materi_and_forms': materi_and_forms,

        'kelasform' : kelasform,
        'babform': babform,
        'materiform': materiform,
    }

    return render(request, 'adminview.html', context)


def updatekelas(request,id,UpdateView = UpdateView):

    template_name = "editkelas.html"
    form_class = KelasUpdateForm
    success_url = ""

    model = kelas
    fields = ["kelas"]

    kelas_objects = kelas.objects.all()

    kelas_names = [kelas.kelas for kelas in kelas_objects]

    model = kelas
    

    template_name = "editkelas.html"
    form_class = KelasForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


    context = {

        'kelas' : kelas_objects,

    }

    return render(request, 'adminview.html', context)


def updatebab(request, bab_id):
    bab_object = bab.objects.get(id=bab_id)
    
    if request.method == 'POST':
        form = BabUpdateForm(request.POST, instance=bab_object)
        if form.is_valid():
            form.save()
            return redirect('admin-kelas')  # Redirect to the adminview page after successful update


def updatedata(request, id):

    form_id = request.POST.get('form_id')

    if request.method == 'POST' and form_id == 'updatebab':

        bab_object = bab.objects.get(id = id)
        form = BabUpdateForm(request.POST, instance=bab_object)

        if form.is_valid():
            form.save()
            return redirect('admin-kelas')  # Redirect to the adminview page after successful update

    if request.method == 'POST' and form_id == 'updatekelas':

        kelas_object = kelas.objects.get(id = id)
        form = KelasUpdateForm(request.POST, instance=kelas_object)
        
        if form.is_valid():
            form.save()
            return redirect('admin-kelas')  # Redirect to the adminview page after successful update

    if request.method == 'POST' and form_id == 'updatemateri':

        materi_object = materi.objects.get(id = id)
        form = MateriUpdateForm(request.POST, instance=materi_object)
        
        if form.is_valid():
            form.save()
            return redirect('admin-kelas')  # Redirect to the adminview page after successful update




def tambahdata(request):
    form_id = request.POST.get('form_id')

    print('form id printed')
    print(form_id)

    if request.method == 'POST' and form_id == 'tambahkelas':

        form = KelasUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-kelas')


    if request.method == 'POST' and form_id == 'tambahbab':

        form = BabUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-kelas')



    if request.method == 'POST' and form_id == 'tambahmateri':

        form = MateriUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-kelas')

    return redirect('admin-kelas')


def deletedata(request, id):
    form_id = request.POST.get('form_id')

    print('form id printed')
    print(form_id)

    if request.method == 'POST' and form_id == 'deletekelas':

        k = kelas.objects.get(id = id)
        k.delete()

        return redirect('admin-kelas')

    if request.method == 'POST' and form_id == 'deletebab':

        k = bab.objects.get(id = id)
        k.delete()

        return redirect('admin-kelas')

    if request.method == 'POST' and form_id == 'deletemateri':

        k = materi.objects.get(id = id)
        k.delete()

        return redirect('admin-kelas')


    

    return redirect('admin-kelas')


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


def materipost (request,slugInput):

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
