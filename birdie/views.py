from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post
from .forms import PostForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'birdie/home.html'

class AdminView(TemplateView):
    template_name= 'birdie/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminView, self).dispatch(request, *args, **kwargs)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'birdie/update.html'
    success_url = '/'
