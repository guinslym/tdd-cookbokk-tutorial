from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('exerpt', )

    def excerpt(self, obj):
        return obj.get_excerpt(5)

admin.site.register(Post, PostAdmin)
