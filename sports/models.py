from django.db import models

# Create your models here.

class SportFormat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Sport(models.Model):
    forrmat_type = models.ForeignKey(SportFormat, on_delete=models.CASCADE)
    sport_name = models.CharField(max_length=100,blank=False, unique=True)
    description = models.TextField(blank=False)
    playing_area = models.CharField(max_length=100, blank=False)
    equipments_required = models.TextField(blank=False)
    history = models.TextField(blank=False)
    rules = models.TextField(blank=False)
    image = models.ImageField(upload_to='sports/')
    number_of_players = models.PositiveIntegerField(default=1)
    
    GAMES = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Dual-Sport', 'Dual-Sport'),
    )

    category = models.CharField(max_length=50, choices=GAMES)
    governing_body = models.CharField(max_length=100)

    def __str__(self):
        return self.sport_name
