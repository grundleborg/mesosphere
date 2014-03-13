from django.contrib import admin
from mesoblog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields  = {"slug": ("title",)}

# Register the Models
admin.site.register(Article, ArticleAdmin)

