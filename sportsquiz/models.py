from django.db import models
from sports.models import Sport, AllSports
from authentication.models import User

# Create your models here.

class SportsQuizCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True, blank=True)
    all_sports = models.ForeignKey(AllSports, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Sports Quiz Category'
        ordering = ['-id']
        unique_together = ('sport', 'all_sports')

    def __str__(self):
        return self.title

class SportQuestionModel(models.Model):
    question = models.CharField(max_length=2000)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    category = models.ForeignKey(SportsQuizCategory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Sport Question Model"
        
    def __str__(self):
        return str(self.category) + " - (Question) - " + (self.question) + " - (Answer) - " + (self.answer)
   
