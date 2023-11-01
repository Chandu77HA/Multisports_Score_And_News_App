from django.db import models

# Create your models here.

class AllPlayersList(models.Model):
    cricbuzz_id = models.PositiveBigIntegerField(verbose_name='Cricbuzz Id',  unique=True, blank=False)
    player_name = models.CharField(verbose_name='Player Name', max_length=500, blank=False)
    team_name = models.CharField(verbose_name='Team Name', max_length=500, blank=False)
    face_image_id = models.PositiveBigIntegerField(verbose_name='Face Image Id', default=182026, blank=False)
    class Meta:
        verbose_name = "All Players List"
        verbose_name_plural = "All Players List"
        ordering = ['cricbuzz_id']

    def __str__(self):
        return self.player_name
    
class InternationalTeams(models.Model):
    cricbuzz_team_id = models.PositiveBigIntegerField(verbose_name='Cricbuzz Team Id', unique=True, blank=False)
    team_name = models.CharField(verbose_name='Team Name', max_length=500, blank=False)
    team_sub_name = models.CharField(verbose_name='Team Sub Name', max_length=50, blank=False)
    image_id = models.PositiveBigIntegerField(verbose_name='Cricbuzz Image Id', blank=False)
    country_name = models.CharField(verbose_name='Country Name', max_length=500, blank=True)
    TEAM_TYPE = (
        ('TEST TEAM', 'Test Team'),
        ('ASSOCIATE TEAM', 'Associate Team'),
    )
    team_type = models.CharField(verbose_name='Team Type', max_length=50, choices=TEAM_TYPE)

    class Meta:
        verbose_name = "International Team"
        verbose_name_plural = "International Teams"
        ordering = ['cricbuzz_team_id']

    def __str__(self):
        return self.team_name
