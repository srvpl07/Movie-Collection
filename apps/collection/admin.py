from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Genere)
admin.site.register(Movies)
admin.site.register(Collection)
admin.site.register(RequestCounter)

