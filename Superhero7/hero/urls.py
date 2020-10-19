from django.urls import path
from .views import HomeView, IndexView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home', HomeView.as_view(), name='home'),
    path('home.html', HomeView.as_view(), name='home'),
    path('index', IndexView.as_view(), name='index'),
    path('index.html', IndexView.as_view(), name='index'),
]
