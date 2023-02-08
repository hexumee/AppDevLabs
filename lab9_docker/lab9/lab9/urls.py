"""lab7_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lab9 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("post_admin/", views.post_admin, name="post_admin"),

    path("users/", views.users, name="users"),
    path("likes/", views.likes, name="likes"),
    path("rating/", views.rating, name="rating"),
    path("posts/", views.posts, name="posts"),
    path("tags/", views.tags, name="tags"),
    
    path("post_create/", views.post_handler, name="post_create"),
    path("post_update/<int:pk>", views.PostUpdateView.as_view(), name="post_update"),
    path("post_delete/<int:pk>", views.PostDeleteView.as_view(), name="post_delete"),

    path("like_create/", views.like_handler, name="like_create"),
    path("like_update/<int:pk>", views.LikeUpdateView.as_view(), name="like_update"),
    path("like_delete/<int:pk>", views.LikeDeleteView.as_view(), name="like_delete"),

    path("rating_create/", views.rating_handler, name="rating_create"),
    path("rating_update/<str:pk>", views.RatingUpdateView.as_view(), name="rating_update"),
    path("rating_delete/<str:pk>", views.RatingDeleteView.as_view(), name="rating_delete"),

    path("tag_create/", views.tag_handler, name="tag_create"),
    path("tag_update/<int:pk>", views.TagUpdateView.as_view(), name="tag_update"),
    path("tag_delete/<int:pk>", views.TagDeleteView.as_view(), name="tag_delete"),

    path("user_create/", views.user_handler, name="user_create"),
    path("user_update/<int:pk>", views.UserUpdateView.as_view(), name="user_update"),
    path("user_delete/<int:pk>", views.UserDeleteView.as_view(), name="user_delete"),

    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", include('django.contrib.auth.urls'), name="logout", kwargs={'next_page': '/index'}),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
