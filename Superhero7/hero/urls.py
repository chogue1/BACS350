from django.urls import path
from hero.views import HeroCreate, HeroIndex, HeroUpdate, HeroDetail

urlpatterns = [
    path('', HeroIndex.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetail.as_view(), name='hero_detail'),
    path('add', HeroCreate.as_view(), name='hero_add'),
    path('<int:pk>/', HeroUpdate.as_view(), name='hero_edit'),
]
