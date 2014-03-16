from django.db import models

import random
import re
import string

# Represents a category which articles can be part of
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name+" ["+str(self.id)+"]"

    def save(self):
        # Make sure that the slug is:
        #   a) not just integers so it doen't look like an ID
        #   b) unique amongst all other objects of that type
        
        # a):
        if re.match(r'^\d+$', self.slug):
            self.slug += "_"
        # b):
        try:
            other = Category.objects.get(slug=self.slug)
            if not (other.id is self.id):
                self.slug += "_"
                self.slug += ''.join(random.sample(string.ascii_lowercase + string.digits, 8))
        except self.DoesNotExist:
            pass
        super(Category, self).save()


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

    def save(self):
        # Make sure that the slug is:
        #   a) not just integers so it doen't look like an ID
        #   b) unique amongst all other objects of that type
        
        # a):
        if re.match(r'^\d+$', self.slug):
            self.slug += "_"
        # b):
        try:
            other = Article.objects.get(slug=self.slug)
            if not (other.id is self.id):
                self.slug += "_"
                self.slug += ''.join(random.sample(string.ascii_lowercase + string.digits, 8))
        except self.DoesNotExist:
            pass

        super(Article, self).save()


