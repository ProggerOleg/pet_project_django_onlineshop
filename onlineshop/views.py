from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView
from .forms import *
from .models import *
from cart.forms import CartAddProductForm
# Create your views here.

cats = Category.objects.all()


def index(request):
    return render(request, 'index.html', {'title': 'Главная страница', 'cats': cats})


def about_us(request):
    return render(request, 'about.html', {'title': 'О нас', 'cats': cats})


class ShopHome(ListView):
    model = ShopList
    template_name = 'shopping.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        posts = ShopList.objects.all()
        return {'cats': cats, 'title': 'Магазин', 'posts': posts}

    def get_queryset(self):
        return ShopList.objects.all()


class ShowPost(DetailView):
    model = ShopList
    template_name = 'show_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        cart_product_form = CartAddProductForm()

        return {'cats': cats, 'title': 'Обьявление', 'product': self.get_object(),
                'cart_product_form': cart_product_form}


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class AddProduct(LoginRequiredMixin, CreateView):
    model = ShopList
    template_name = 'addpage.html'
    form_class = AddPostForm
    success_url = reverse_lazy('shop')
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        return {'cats': cats, 'title': 'Добавить новый товар', 'form': self.form_class}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        return {'cats': cats, 'title': 'Регистрация', 'form': self.form_class}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('shop')

    def get_context_data(self, **kwargs):
        return {'title': 'Авторизация', 'form': self.form_class, 'cats': cats}


def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(FormView):
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

    def get_context_data(self, **kwargs):
        return {'title': 'Связаться с нами', 'form': self.form_class, 'cats': cats}


class ShopCategory(ListView):
    model = ShopList
    template_name = 'shopping.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        posts = ShopList.objects.filter(cat__slug=self.kwargs['cat_slug'], available=True).select_related('cat')
        return posts

    def get_context_data(self, *, object_list=None, **kwargs):
        posts = ShopList.objects.filter(cat__slug=self.kwargs['cat_slug'], available=True).select_related('cat')
        return {'title': 'Категория - ' + str(posts[0].cat), 'posts': posts, 'cats': cats, 'cat': posts[0].cat}
