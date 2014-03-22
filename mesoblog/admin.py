from django.contrib import admin
from django.forms import ModelForm

from mesoblog.models import Article, Category, Comment

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

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields  = {"slug": ("name",)}

# Register the Models
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
