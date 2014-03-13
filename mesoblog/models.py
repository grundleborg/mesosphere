from django.db import models

# Represents a category which articles can be part of
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name+" ["+str(self.id)+"]"


# Article model represents one article in the blog.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    contents = models.TextField()
    date_published = models.DateTimeField()
    published = models.BooleanField()
    primary_category = models.ForeignKey(Category, related_name='+')
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title+" ["+str(self.id)+"]"


