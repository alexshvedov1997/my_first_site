from django.contrib import admin
from .models import  Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    raw_id_fields = ('author',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','email','created','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','post','body')
# Register your models here.
