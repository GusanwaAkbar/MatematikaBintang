from django.contrib import admin
from .models import kelas
from .models import bab
from .models import materi

# Register your models here.
admin.site.register(kelas)
admin.site.register(bab)
admin.site.register(materi)