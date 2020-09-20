"""superhero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hero.views import HulkView, WidowView, LanternView, SpiderView, ThorView
from pages.views import HeroView, AboutView, IndexView, HomeView

urlpatterns = [
    path('about', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('index', IndexView.as_view()),
    path('', HomeView.as_view()),
    path('hulk', HulkView.as_view()),
    path('black_widow', WidowView.as_view()),
    path('hero/<str:identity>', HeroView.as_view()),
    path('thor', ThorView.as_view()),
    path('spider_man', SpiderView.as_view()),
    path('green_lantern', LanternView.as_view()),
]
