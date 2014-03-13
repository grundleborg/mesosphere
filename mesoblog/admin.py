from django.contrib import admin
from mesoblog.models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields  = {"slug": ("title",)}

# Register the Models
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
