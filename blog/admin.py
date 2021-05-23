from django.contrib import admin
from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    # list_display = ('title', 'slug', 'created_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'parent', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
