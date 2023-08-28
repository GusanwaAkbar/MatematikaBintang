"""MWB_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from MWB_home import views
from blog_post import viewsblog
#from django.contrib.auth.views import logout
from django.conf import settings
from django.urls import include, path

from blog_post import viewsblog



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='home'),


    path('users/', include('django.contrib.auth.urls')), 
    path('logout/', views.logout),
    path('login/', views.login),
    path('blog/', viewsblog.post),
    path('beta/', viewsblog.post),
    path('pricing/', viewsblog.pricing, name = 'pricing'),
    path('beta/<slug:slugInput>/', viewsblog.detailpost ),


    path('pesananku', viewsblog.pesananku, name = 'pesananku'),
    path('pesan-smp-3' ,viewsblog.pesan_smp3, name = 'pesan-smp-3' ),




    path('adminview', viewsblog.adminview, name= 'adminview'),
    path('admin-kelas', viewsblog.adminkelas, name = 'admin-kelas'),

    path('updatekelas/<int:pk>/', viewsblog.adminkelas, name = 'updatekelas'),
    path('updatebab/<int:bab_id>/', viewsblog.updatebab, name = 'updatebab'),
    path('updatemateri/<int:pk>/', viewsblog.adminkelas, name = 'updatemateri'),



    path('tambahdata', viewsblog.tambahdata, name = 'tambahdata'),
    path('deletedata/<int:id>/', viewsblog.deletedata, name = 'deletedata'),
    path('updatedata/<int:id>/', viewsblog.updatedata, name = 'updatedata'),
]
    
