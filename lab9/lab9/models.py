from django.db.models import *


class Users(Model):
    idx = AutoField(verbose_name="Индекс", primary_key=True)
    username = TextField(verbose_name="Никнейм", unique=True)
    utype = BooleanField(verbose_name="Является автором")
    uadmin = BooleanField(verbose_name="Администратор?", default=False)
    password1 = TextField(verbose_name="Пароль")
    password2 = TextField(verbose_name="Пароль еще раз")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_absolute_url(self):
        return "/users"

class Rating(Model):
    nickname = TextField(verbose_name="Никнейм", primary_key=True)
    likes_sum = IntegerField(verbose_name="Рейтинг", default=0)

    class Meta:
        verbose_name = "Рейтинг пользователя"
        verbose_name_plural = "Рейтинг пользователей"
    
    def get_absolute_url(self):
        return "/rating"

class Post(Model):
    pid = AutoField(verbose_name="Идентификатор поста", primary_key=True)
    nickname = TextField(verbose_name="Никнейм")
    header = TextField(verbose_name="Заголовок")
    text = TextField(verbose_name="Текст")
    likes = IntegerField(verbose_name="Количество лайков", default=0)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def get_absolute_url(self):
        return "/posts"

class Tags(Model):
    idx = AutoField(verbose_name="Индекс", primary_key=True)
    pid = IntegerField(verbose_name="Идентификатор поста")
    tag = TextField(verbose_name="Тег")

    class Meta:
        verbose_name = "Тег поста"
        verbose_name_plural = "Теги постов"
    
    def get_absolute_url(self):
        return "/tags"

class Likes(Model):
    idx = AutoField(verbose_name="Индекс", primary_key=True)
    post = IntegerField(verbose_name="Номер поста")
    nickname = TextField(verbose_name="Никнейм")

    class Meta:
        verbose_name = "Лайк пользователя"
        verbose_name_plural = "Лайки пользователей"
    
    def get_absolute_url(self):
        return "/likes"
