from django import forms
from .models import kelas
from .models import bab
from .models import materi
from .models import SubscriptionPlan
from .models import SubscriptionRequest
from .models import UserSubscription


class KelasUpdateForm(forms.ModelForm):
    class Meta:
        model = kelas
        fields = ['kelas']  # Add fields you want to update

class BabUpdateForm(forms.ModelForm):
    class Meta:
        model = bab
        fields = ['bab','kelas']  # Add fields you want to update

class MateriUpdateForm(forms.ModelForm):
    class Meta:
        model = materi
        fields = ['judul','link','deskripsi', 'bab','kelas']  # Add fields you want to update

# class PlanForm(forms.ModelForm):
#     class Meta:
#         model = SubscriptionPlan
#         fields = ['judul','link','deskripsi', 'bab','kelas']  # Add fields you want to update

# class RequestForm(forms.ModelForm):
#     class Meta:
#         model = SubscriptionRequest
#         fields = ['judul','link','deskripsi', 'bab','kelas']  # Add fields you want to update

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserSubscription
#         fields = ['judul','link','deskripsi', 'bab','kelas']  # Add fields you want to update