from django.contrib import admin
from cricbuzz import models
from cricbuzz.models import AllPlayersList, InternationalTeams

# Register your models here.

admin.site.register(AllPlayersList)
admin.site.register(InternationalTeams)
