from django.contrib import admin
from sports.models import Sport, AllSports, SportFormat

# Register your models here.

admin.site.register(Sport)
admin.site.register(AllSports)
admin.site.register(SportFormat)