from django.db import models

# Article model represents one article in the blog.
class Article(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    date_published = models.DateTimeField()
    published = models.BooleanField()
    
    def __str__(self):
        return self.title+" ["+str(self.id)+"]"


