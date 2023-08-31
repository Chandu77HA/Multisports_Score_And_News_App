from django.db import models

# Create your models here.

class SaveAllIndianSportsNews(models.Model):
    description = models.TextField(default='No Description Found', blank = True, null = True)
    title = models.CharField(max_length=2000, blank = True, null = True, default='No Title Found')
    source_name = models.CharField(max_length=2000, blank = True, null = True, default='No Title Found')
    author = models.CharField(max_length=2000, blank = True, null = True, default='No Author Found')
    published_at = models.CharField(max_length=2000, blank = True, null = True, default='No Published Date Found')
    url = models.URLField(max_length=2000, blank = True, null = True, default='No URL Found')
    url_to_image = models.URLField(max_length=2000, blank = True, null = True, default='No Image Link Found')
    content = models.TextField(blank = True, null = True, default='No Content Found')

    def __str__(self):
        if self.title == None:
            return "The title name is Null"
        return self.title