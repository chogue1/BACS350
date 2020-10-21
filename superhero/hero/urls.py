from django.urls import path
from .views import HulkView, WidowView, LanternView, SpiderView, ThorView

urlpatterns = [
    path('hulk.html', HulkView.as_view(), name='hulk'),
    path('hulk', HulkView.as_view(), name='hulk'),
    path('black_widow', WidowView.as_view(), name='black_widow'),
    path('thor', ThorView.as_view(), name='thor'),
    path('spider_man', SpiderView.as_view(), name='spider_man'),
    path('green_lantern', LanternView.as_view(), name='green_lantern'),
    path('black_widow.html', WidowView.as_view(), name='black_widow'),
    path('thor.html', ThorView.as_view(), name='thor'),
    path('spider_man.html', SpiderView.as_view(), name='spider_man'),
    path('green_lantern.html', LanternView.as_view(), name='green_lantern'),
]