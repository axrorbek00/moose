from django.contrib import admin
from .models import Blog, ContactModel, CommentModel


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', ]
    list_display_links = ['name', 'email', 'created_at', ]


@admin.register(ContactModel)
class Admin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'created_at', 'is_solved']
    list_display_links = ['full_name', 'email', 'created_at']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_display_links = ['title', 'author', 'created_at']
    readonly_fields = ['slug']
