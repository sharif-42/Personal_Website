from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from blog.models import Post


class HomeView(View):
    def get(self, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(self.request, "home.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
