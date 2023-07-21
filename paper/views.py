from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ContentListView(LoginRequiredMixin, DataMixin, ListView):
    model = Paper  # get all items from the table and list them
    template_name = 'paper/routes/show_content.html'  # our template
    context_object_name = 'posts'  # replace object_list to posts
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = len(context['object_list'])
        context['request'] = self.request
        return context

    def get_queryset(self):
        return Paper.objects.filter(is_published=True)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Paper
    template_name = 'paper/routes/show_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class CategoriesDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = Categories
    template_name = 'paper/routes/show_categories.html'
    slug_url_kwarg = 'cat_slug'
    context_object_name = 'posts'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].paper_set.all()
        context['request'] = self.request
        return context


class PageCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    form_class = AddPostForm
    template_name = 'paper/routes/add_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'paper/routes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'paper/routes/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    print(request)
    logout(request)
    return redirect('login')