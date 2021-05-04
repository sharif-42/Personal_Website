from django.urls import path

from blog.rest_apis.views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail'),
]