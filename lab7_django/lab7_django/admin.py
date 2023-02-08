from django.contrib import admin
from .models import Users, Likes, Rating, Post, Tags

admin.site.register(Users)
admin.site.register(Rating)
admin.site.register(Likes)
admin.site.register(Post)
admin.site.register(Tags)
