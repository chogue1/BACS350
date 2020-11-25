# hero/urls.py
from django.urls import path
from hero.views import HeroAddView, HeroListView, HeroEditView, HeroDetailView, HeroDeleteView
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HeroListView.as_view(), name='hero_list'),
    path('', HeroListView.as_view(), name='hero_list.html'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail.html'),
    path('add', HeroAddView.as_view(), name='hero_add'),
    path('add', HeroAddView.as_view(), name='hero_add.html'),
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit.html'),
]
