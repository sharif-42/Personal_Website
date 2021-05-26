from django.urls import path

from blog.rest_apis.views import (
    HomeView,
    PostDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<uuid:post_uuid>/', PostDetailView.as_view(), name='post-detail'),
]