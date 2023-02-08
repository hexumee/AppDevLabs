from .models import Users, Likes, Post, Tags, Rating
from django.forms import ModelForm, TextInput, Textarea, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['idx', 'username', 'utype', 'uadmin', 'password1', 'password2']

    widgets = {
        "username": TextInput(attrs={"placeholder": "Никнейм"}),
    }

class LikesForm(ModelForm):
    class Meta:
        model = Likes
        fields = ['post', 'nickname']

    widgets = {
        "post": TextInput(attrs={"placeholder": "Номер поста"}),
        "nickname": TextInput(attrs={"placeholder": "Никнейм"}),
    }

class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['nickname', 'header', 'text']
    
    widgets = {
        "nickname": TextInput(attrs={"placeholder": "Никнейм"}),
        "header": TextInput(attrs={"placeholder": "Заголовок"}),
        "text": Textarea(attrs={"placeholder": "Текст"}),
    }

class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['idx', 'pid', 'tag']
    
    widgets = {
        "tag": TextInput(attrs={"placeholder": "Тег"}),
    }

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['nickname', 'likes_sum']
    
    widgets = {
        "nickname": TextInput(attrs={"placeholder": "Никнейм"}),
        "likes_sum": TextInput(attrs={"placeholder": "Рейтинг"}),
    }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
