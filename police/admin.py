from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Station)
admin.site.register(PoliceRegistration)
admin.site.register(OccurenceRecords)
admin.site.register(OccurenceReport)
admin.site.register(UserReport)