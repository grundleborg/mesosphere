from django.contrib import admin
from mesoblog.models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields  = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields  = {"slug": ("name",)}

# Register the Models
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
