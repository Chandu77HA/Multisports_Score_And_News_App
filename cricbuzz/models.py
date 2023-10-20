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
    


