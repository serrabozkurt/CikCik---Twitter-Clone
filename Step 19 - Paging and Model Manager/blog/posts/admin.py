from django.contrib import admin
from django.contrib import messages

from posts.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "published"]
    actions = ['publish']

    def publish(self, request, queryset):
        queryset.update(published=True)
        messages.success(request, "Seçili yazılar yayınlandı.")

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
