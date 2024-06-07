
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_repositories/', views.fetch_repositories, name='fetch_repositories'),
]
