from django.contrib import admin

# Register your models here.
from blogsite.models import Post
from blogsite.models import Comment


admin.site.register(Post)
admin.site.register(Comment)