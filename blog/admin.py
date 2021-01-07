from django.contrib import admin
from .models import  Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    raw_id_fields = ('author',)
    prepopulated_fields = {'slug':('title',)}
# Register your models here.
