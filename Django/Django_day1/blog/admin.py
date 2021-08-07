from django.contrib import admin

# Register your models here.

from blog.models import Article

# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'latitude', 'longitude']