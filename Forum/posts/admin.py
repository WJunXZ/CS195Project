from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'featured', 'user')
    list_display_links = ('id', 'title')
    list_filter = ('user',)
    list_editable = ('featured',)
    search_fields = ('title', 'content',)
    list_per_page=10

admin.site.register(Post, PostAdmin)