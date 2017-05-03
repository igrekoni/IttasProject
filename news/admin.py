from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "updated", "timestamp", "draft"]
    list_display_links = ["__unicode__"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["__unicode__", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
