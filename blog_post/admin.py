from django.contrib import admin
from .models import kelas
from .models import bab
from .models import materi
from .models import SubscriptionPlan
from .models import SubscriptionRequest
from .models import UserSubscription



# Register your models here.
admin.site.register(kelas)
admin.site.register(bab)
admin.site.register(materi)
admin.site.register(SubscriptionPlan)
admin.site.register(SubscriptionRequest)
admin.site.register(UserSubscription)