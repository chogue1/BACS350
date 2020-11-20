# hero/urls.py
from django.urls import path
from hero.views import HeroAddView, HeroListView, HeroEditView, HeroDetailView, HeroDeleteView

urlpatterns = [
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'),
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
]
