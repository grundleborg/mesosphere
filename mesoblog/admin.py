from django.conf import settings
from django.contrib import admin
from django.forms import ModelForm

from pykismet3 import Akismet

from mesoblog.models import Article, Category, Comment, Image

class ImageInline(admin.StackedInline):
        model = Image

class ArticleAdminForm(ModelForm):
    class Meta:
        model = Article
        exclude = []

    def clean(self):
        # Make sure the primary category is included in the list of categories
        categories = list(self.cleaned_data['categories'])
        if self.cleaned_data['primary_category'] not in categories:
            categories.append(self.cleaned_data['primary_category'])
        self.cleaned_data['categories'] = categories
        return self.cleaned_data

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    prepopulated_fields  = {"slug": ("title",)}
    inlines = [
            ImageInline,
    ]
    list_display = ['__str__', 'slug', 'published']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields  = {"slug": ("name",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'teaser', 'is_spam']
    actions = ['mark_as_spam', 'mark_as_ham']

    ordering = ['-id']

    def mark_as_spam(self, request, queryset):
        ak = Akismet(blog_url=request.get_host(),
                     api_key=settings.AKISMET_API_KEY,
                     user_agent="Mesosphere/0.0.1")
        for comment in queryset:
            ak_dict = {'user_ip': comment.user_ip,
                       'user_agent': comment.user_agent,
                       'referrer': comment.referer,
                       'comment_content': comment.contents,
                       'comment_author': comment.name,
                      }
            if settings.DEBUG is True:
                ak_dict['is_test'] = 1
            ak.submit_spam(ak_dict)
            comment.delete()
  
        if len(queryset) == 1:
            message_bit = "1 comment was"
        else:
            message_bit = "%s comments were" % len(queryset)
        
        self.message_user (request, "%s sucessfully marked as spam and deleted." % message_bit)

    mark_as_spam.short_description = "Mark Comments as Spam & Delete"

    def mark_as_ham(self, request, queryset):
        ak = Akismet(blog_url=request.get_host(),
                     api_key=settings.AKISMET_API_KEY,
                     user_agent="Mesosphere/0.0.1")
        for comment in queryset:
            ak_dict = {'user_ip': comment.user_ip,
                       'user_agent': comment.user_agent,
                       'referrer': comment.referer,
                       'comment_content': comment.contents,
                       'comment_author': comment.name,
                      }
            if settings.DEBUG is True:
                ak_dict['is_test'] = 1
            ak.submit_ham(ak_dict)
            comment.is_spam = False;
            comment.save()

        if len(queryset) == 1:
            message_bit = "1 comment was"
        else:
            message_bit = "%s comments were" % len(queryset)
        
        self.message_user (request, "%s sucessfully marked as ham." % message_bit)
 
    mark_as_ham.short_description = "Mark Comments as Ham"

# Register the Models
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
