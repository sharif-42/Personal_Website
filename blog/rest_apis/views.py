from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView

from blog.models.post import Post
from blog.services.post_services import PostService


class HomeView(View):
    def get(self, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(self.request, "home.html", context)


class PostDetailView(ListView, CreateView):
    model = Post
    template_name = 'post-detail.html'
    service_class = PostService()

    def get_context_data(self, **kwargs):
        context = {}
        post_instance = self.service_class.get_post_by_uuid(post_uuid=kwargs.get('post_uuid'))
        if post_instance:
            context = {
                "post": post_instance,
                "comments": post_instance.comments.all(),
            }
        return context

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(**kwargs)
        return render(self.request, self.template_name, context_data)

    def post(self, request, *args, **kwargs):
        context_data = {}
        post_instance = self.service_class.create_comment(post_uuid=kwargs.get('post_uuid'),
                                                          created_by=request.user,
                                                          form_data=request.POST
                                                          )

        if post_instance:
            context_data = {
                "post": post_instance,
                "comments": post_instance.comments.all(),
            }
        return render(self.request, self.template_name, context_data)
