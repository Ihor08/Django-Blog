from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'update']
    list_display_links = ['update']
    class Meta:
        model = Post



admin.site.register(Post, PostModelAdmin)

