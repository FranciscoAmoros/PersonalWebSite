from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "published")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Comment)