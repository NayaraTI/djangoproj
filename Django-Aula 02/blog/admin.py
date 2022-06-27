from django.contrib import admin

# Register your models here.
from blogsite1.models import Post
from blogsite1.models import Comment


admin.site.register(Post)
admin.site.register(Comment)