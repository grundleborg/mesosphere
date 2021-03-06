from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags

from taggit.managers import TaggableManager

import random
import re
import string

from datetime import timedelta

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

# Represents one comment on an article
class Comment(models.Model):
    article = models.ForeignKey('Article', related_name='comments')
    parent = models.ForeignKey('Comment', related_name='children', blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    site = models.URLField(max_length=255, blank=True, null=True, verbose_name="Web Site")
    posted = models.DateTimeField()
    contents = models.TextField(verbose_name="Comments")
    notify_on_reply = models.BooleanField(default=False)
    notify_on_thread = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)
    user_ip = models.CharField(max_length=100, default="", blank=True)
    user_agent = models.CharField(max_length=255, default="", blank=True)
    referer = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        ordering = ['posted']

    def __str__(self):
        return "Comment ["+str(self.id)+"] on Article ["+str(self.article.id)+"] by "+self.name+"."

    def teaser(self):
        return self.contents[0:200]

# Images that can be put in a blog post
class Image(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    image = models.ImageField(upload_to="media/images")
    article = models.ForeignKey('Article', related_name='images')

# Article model represents one article in the blog.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    contents = models.TextField()
    date_published = models.DateTimeField()
    published = models.BooleanField(default=False)
    primary_category = models.ForeignKey(Category, related_name='+')
    categories = models.ManyToManyField(Category, blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-date_published']
    
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

    def top_level_comments(self):
        return self.comments.filter(parent__isnull=True, is_spam=False)

    def teaser(self):
        output = ""
        for line in self.contents.split('\n'):
            if line.strip():
                output = output + '\n' + line
            else:
                break
        return output

    def year(self):
        return str(self.date_published.year).zfill(4)

    def month(self):
        return str(self.date_published.month).zfill(2)

    def day(self):
        return str(self.date_published.day).zfill(2)

    def comments_open(self):
        if (timezone.now() - self.date_published) > timedelta(days=settings.MESOBLOG["close_comments_days"]):
            return False
        return True


