from django.views.generic import ListView, TemplateView
from .models import Superhero

class HomeView(TemplateView):
    template_name = 'home.html'

class IndexView(ListView):
    model = Superhero
    template_name = 'index.html'
    context_object_name = 'heroeslist'
    
class HulkView(TemplateView):
    template_name = 'hulk.html'
    
class WidowView(TemplateView):
    template_name = 'black_widow.html'
    
class LanternView(TemplateView):
    template_name = 'green_lantern.html'

class ThorView(TemplateView):
    template_name = 'thor.html'
    
class SpiderView(TemplateView):
    template_name = 'spider_man.html'


# Create your views here.
