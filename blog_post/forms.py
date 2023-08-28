from django import forms
from .models import kelas
from .models import bab
from .models import materi


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