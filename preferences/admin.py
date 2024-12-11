from django.contrib import admin
from .models import Tag, Post, User, Interaction

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'content')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'tags', 'preferences')

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('interaction_id', 'user', 'post', 'interaction_type', 'interaction_time')
