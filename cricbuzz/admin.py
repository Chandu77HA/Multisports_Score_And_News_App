from django.contrib import admin
from cricbuzz import models
from cricbuzz.models import AllPlayersList

# Register your models here.

admin.site.register(AllPlayersList)
class AllPlayersListAdmin(admin.ModelAdmin):
    list_display = ('id', 'cricbuzz_id', 'player_name', 'team_name', 'face_image_id')
    list_display_links = ('player_name',)
