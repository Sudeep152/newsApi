from django.db import models

# Create your models here.
class Article(models.Model):
        story_unique_id = models.AutoField
        story_headline = models.CharField(max_length=64)
        story_category = models.CharField(max_length=100)
        story_region  = models.CharField(max_length=100)
        story_author_name = models.CharField(max_length=100)
        story_date = models.DateTimeField(auto_now_add=True)
        story_details = models.CharField(max_length=1000)

        def __str__(self):
                return self.story_headline
