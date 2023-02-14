from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users, Likes, Rating, Post, Tags
from .forms import UsersForm, LikesForm, PostsForm, TagsForm, RatingForm, CreateUserForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, "main/index.html", {"role": get_role(request.user)})


def users(request):
    if get_role(request.user) not in ("admin"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    users = Users.objects.all()
    return render(request, "users/users.html", {"role": get_role(request.user), "result": users})


def likes(request):
    if get_role(request.user) not in ("admin"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    utypes = Likes.objects.all()
    return render(request, "likes/likes.html", {"role": get_role(request.user), "result": utypes})


def rating(request):
    if get_role(request.user) not in ("admin"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    ulikes = Rating.objects.all()
    return render(request, "rating/rating.html", {"role": get_role(request.user), "result": ulikes})


def posts(request):
    posts = Post.objects.all()
    ptags = Tags.objects.all()

    posted = {}
    tagged = {}

    for tag in ptags:
        if tag.pid not in tagged.keys():
            tagged.update({tag.pid: [tag.tag]})
        else:
            tagged[tag.pid].append(tag.tag)
    
    print(tagged)

    for post in posts:
        posted.update({post.pid: {"nickname": post.nickname, "header": post.header, "text": post.text, "likes": post.likes_cnt, "tags": ", ".join(tagged[post.pid]) if post.pid in tagged.keys() else None}})

    return render(request, "posts/posts.html", {"role": get_role(request.user), "result": posted})


def tags(request):
    if get_role(request.user) not in ("admin", "author"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    if get_role(request.user) in ("admin"):
        ptags = Tags.objects.all()
        return render(request, "tags/tags.html", {"role": get_role(request.user), "result": ptags})

    if get_role(request.user) in ("author"):
        posts = Post.objects.filter(nickname=request.user)
        ptags = Tags.objects.filter(pid__in=posts)
        return render(request, "tags/tags.html", {"role": get_role(request.user), "result": ptags})


def post_admin(request):
    if get_role(request.user) not in ("admin", "author"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    if get_role(request.user) in ("admin"):
        posts = Post.objects.all()
        return render(request, "main/post_admin.html", {"role": get_role(request.user), "result": posts})
    
    if get_role(request.user) in ("author"):
        posts = Post.objects.filter(nickname=request.user)
        return render(request, "tags/tags.html", {"role": get_role(request.user), "result": posts})



def post_handler(request):
    if get_role(request.user) not in ("admin", "author"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    err = ""

    if request.method == "POST":
        form = PostsForm(request.POST)
        print(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            return redirect("posts")
        else:
            err = "Ашпка"

    form = PostsForm({"nickname":request.user})
    data = {    
        "form": form,
        "err": err,
        "source": "publish",
        "role": get_role(request.user),
        "uu": request.user
    }

    return render(request, 'posts/post_update.html', data)


def like_handler(request):
    if get_role(request.user) not in ("admin"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    err = ""

    if request.method == "POST":
        form = LikesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("likes")
        else:
            err = "Ашпка"

    form = LikesForm()
    data = {    
        "form": form,
        "err": err,
        "role": get_role(request.user), 
        "source": "publish"
    }

    return render(request, 'likes/like_update.html', data)


def tag_handler(request):
    if get_role(request.user) not in ("admin", "author"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    err = ""

    if request.method == "POST":
        form = TagsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tags")
        else:
            err = "Ашпка"

    form = TagsForm()
    data = {    
        "form": form,
        "err": err,
        "role": get_role(request.user), 
        "source": "publish"
    }

    return render(request, 'tags/tag_update.html', data)


def user_handler(request):
    return register(request)
    """ err = ""
    
    if request.method == "POST":
        form = UsersForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("users")
        else:
            err = "Ашпка"

    form = UsersForm()
    data = {    
        "form": form,
        "err": err,
        "source": "publish"
    }

    return render(request, 'registration/registration.html', data) """


def rating_handler(request):
    if get_role(request.user) not in ("admin"):
        return render(request, "main/index.html", {"role": get_role(request.user)})

    err = ""

    if request.method == "POST":
        form = RatingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("rating")
        else:
            err = "Ашпка"

    form = RatingForm()
    data = {    
        "form": form,
        "err": err,
        "role": get_role(request.user), 
        "source": "publish"
    }

    return render(request, 'rating/rating_update.html', data)


def register(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        uform = UsersForm(request.POST)

        if form.is_valid() and uform.is_valid():
            form.save()
            uform.save()
            Group.objects.get(name="reader").user_set.add(User.objects.last())
            return redirect('login')

    return render(request, 'registration/registration.html', {"role": get_role(request.user), 'form': form, 'names': ['Логин', 'Пароль', 'Подтверждение пароля']})


def login(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        user = authenticate(request, nickname=nickname, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'registration/login.html', {"role": get_role(request.user), 'names': ['Логин', 'Пароль', 'Подтверждение пароля']})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['nickname', 'header', 'text']

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['role'] = get_role(self.request.user)

        return context

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin", "author"):
            return index(request)

        self.object = self.get_object()
        return super(PostUpdateView, self).get(request, *args, **kwargs)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_remove.html'
    success_url = "/posts"

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin", "author"):
            return index(request)

        self.object = self.get_object()
        return super(PostDeleteView, self).get(request, *args, **kwargs)


class RatingUpdateView(UpdateView):
    model = Rating
    template_name = 'rating/rating_update.html'
    fields = ['nickname', 'likes_sum']

    def get_context_data(self, **kwargs):
        context = super(RatingUpdateView, self).get_context_data(**kwargs)
        context['role'] = get_role(self.request.user)

        return context
    
    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin"):
            return index(request)

        self.object = self.get_object()
        return super(RatingUpdateView, self).get(request, *args, **kwargs)

class RatingDeleteView(DeleteView):
    model = Rating
    template_name = 'rating/rating_remove.html'
    success_url = "/rating"

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin"):
            return index(request)

        self.object = self.get_object()
        return super(RatingDeleteView, self).get(request, *args, **kwargs)


class TagUpdateView(UpdateView):
    model = Tags
    template_name = 'tags/tag_update.html'
    fields = ['idx', 'pid', 'tag']

    def get_context_data(self, **kwargs):
        context = super(TagUpdateView, self).get_context_data(**kwargs)
        context['role'] = get_role(self.request.user)

        return context
    
    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin", "author"):
            return index(request)

        self.object = self.get_object()
        return super(TagUpdateView, self).get(request, *args, **kwargs)

class TagDeleteView(DeleteView):
    model = Tags
    template_name = 'tags/tag_remove.html'
    success_url = "/tags"

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin", "author"):
            return index(request)

        self.object = self.get_object()
        return super(TagDeleteView, self).get(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = Users
    template_name = 'users/user_update.html'
    fields = ['idx', 'username', 'utype', 'uadmin', 'password1']

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin"):
            return index(request)

        self.object = self.get_object()
        return super(UserUpdateView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['role'] = get_role(self.request.user)

        return context

    def form_valid(self, form):
        if form.cleaned_data['utype']:
            Group.objects.get(name="author").user_set.add(User.objects.get(username=form.cleaned_data['username']))
        else:
            Group.objects.get(name="author").user_set.remove(User.objects.get(username=form.cleaned_data['username']))

        if form.cleaned_data['uadmin']:
            Group.objects.get(name="admin").user_set.add(User.objects.get(username=form.cleaned_data['username']))
        else:
            Group.objects.get(name="admin").user_set.remove(User.objects.get(username=form.cleaned_data['username']))
        
        nu = User.objects.get(username__exact=form.cleaned_data['username'])
        nu.set_password(form.cleaned_data['password1'])
        nu.save()

        return super().form_valid(form)

class UserDeleteView(DeleteView):
    model = Users
    template_name = 'users/user_remove.html'
    success_url = "/users"

    def form_valid(self, form):
        qquery = Users.objects.get(pk=self.request.path.split("/")[-1])
        query = User.objects.get(username=qquery.username)
        qquery.delete()
        query.delete()

        return super(UserDeleteView, self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin"):
            return index(request)

        self.object = self.get_object()
        return super(UserDeleteView, self).get(request, *args, **kwargs)


class LikeUpdateView(UpdateView):
    model = Likes
    template_name = 'likes/like_update.html'
    fields = ['post', 'nickname']

    def get_context_data(self, **kwargs):
        context = super(LikeUpdateView, self).get_context_data(**kwargs)
        context['role'] = get_role(self.request.user)

        return context

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin"):
            return index(request)

        self.object = self.get_object()
        return super(LikeUpdateView, self).get(request, *args, **kwargs)

class LikeDeleteView(DeleteView):
    model = Likes
    template_name = 'likes/like_remove.html'
    success_url = "/likes"

    def get(self, request, *args, **kwargs):
        if get_role(self.request.user) not in ("admin"):
            return index(request)

        self.object = self.get_object()
        return super(LikeDeleteView, self).get(request, *args, **kwargs)


def get_role(user):
    role = "None"

    if user.is_authenticated:
        if user.groups.filter(name='admin').exists() or user.is_superuser:
            role = "admin"
        elif user.groups.filter(name='author').exists():
            role = "author"
        elif user.groups.filter(name='reader').exists():
            role = "reader"
    
    return role
