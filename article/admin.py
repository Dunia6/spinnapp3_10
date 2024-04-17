from django.contrib import admin
from .models import Article, ArticleImage, Category

# Register your models here.

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

