from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from app.forms import SignUpForm, AddPostForm
from app.models import AddPost
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView


class HomePageView(TemplateView):
    template_name = 'index.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User = authenticate(username=username, password=raw_password)
            login(request, User)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def AddPostView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.time = timezone.now()
            form.instance.username = request.user
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'confirmlogin.html', {'form': form})


class PoliticsListView(generic.ListView):
    model = AddPost
    context_object_name = 'post_list'
    template_name = 'posts.html'

    def get_queryset(self):
        return AddPost.objects.filter(category="Politics")


class LifeStyleListView(generic.ListView):
    model = AddPost
    context_object_name = 'post_list'
    template_name = 'posts.html'

    def get_queryset(self):
        return AddPost.objects.filter(category="Lifestyle")


class TechnologyListView(generic.ListView):
    model = AddPost
    context_object_name = 'post_list'
    template_name = 'posts.html'

    def get_queryset(self):
        return AddPost.objects.filter(category="Technology")


class PostListProfileView(generic.ListView):
    model = AddPost
    context_object_name = 'post_list'
    template_name = 'profile.html'

    def get_queryset(self):
        return AddPost.objects.filter(username=self.request.user)


class PostDelete(DeleteView):
    model = AddPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('profile')


class PostUpdate(UpdateView):
    model = AddPost
    fields = ('title', 'data',)
    template_name = 'update_post.html'
    success_url = reverse_lazy('profile')