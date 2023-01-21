from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "published"]
    list_filter = ["published", "category", ("created", DateRangeFilter)]
    list_editable = ["published", "category", "title"]
    actions = ["yayinla"]
    actions_on_top = False
    actions_on_bottom = False
    actions_selection_counter = False
    readonly_fields = ["published"]
    list_per_page = 1
    ordering = ["title"]
    search_fields = ["title"]

    def yayinla(self, request, queryset):
        queryset.update(published=True)
        # TODO: Sosyal medyada paylaşma kodu
    yayinla.short_description = "Seçili yazıları yayınla"


admin.site.register(Post, PostAdmin)
