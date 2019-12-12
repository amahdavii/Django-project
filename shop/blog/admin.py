from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug' , 'published', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'body')
    ordering = ['status', 'published']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)