# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk:                 # solo la primera vez que se guarda
            obj.author = request.user  # el autor sos vos, quien está logueado en el admin
        super().save_model(request, obj, form, change)

admin.site.register(Comment)