from django.contrib import admin
from .models import Category, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "created_at", "views", "category", "author")
    list_display_links = ("pk", "title")
    list_editable = ("category", "author")
    list_filter = ("category", "author", "created_at")
    readonly_fields = ("views",)


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)