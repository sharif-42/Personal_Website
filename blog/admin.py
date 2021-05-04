from django.contrib import admin
from .models.post import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    # list_display = ('title', 'slug', 'created_date')


admin.site.register(Post, PostAdmin)
