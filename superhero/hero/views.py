from django.views.generic import ListView, TemplateView
from .models import Superhero

class HomeView(TemplateView):
    template_name = 'superhero_theme.html'

class IndexView(ListView):
    model = Superhero
    template_name = 'index.html'
    context_object_name = 'heroeslist'
    
class WidowView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return {
            'h1': 'Hero: Black Widow',
            'h2': 'Natasha Romanova AKA Наталья Альяновна "Наташа" Романова, is a fictional Marvel Superhero', 
            'p': 'Her debut was featured in Tales of Suspense #52 as a Russian spy and antagonist to Iron Man...',
            'img': '/static/images/black_widow.jpg',
            'alt': 'black_widow'
        }
    
class LanternView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return {
            'h1': 'Hero: Green Lantern',
            'h2': 'a DC comic hero considered to be a staple of the American fantasy', 
            'p': 'Green Lantern first appeared in All-American Comics #16, which then an entire series was written in 1941...',
            'img': '/static/images/green_lantern.jpg',
            'alt': 'green_lantern' 
        }

class HulkView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return {
            'h1': 'Hero: The Incredible Hulk',
            'h2': 'The hulk is a fictional Marvel superhero, the second face of Dr Robert Bruce Banner.', 
            'p': 'His debut issue of The Incredible Hulk told both sides to his story...',
            'img': '/static/images/hulk.jpg',
            'alt': 'hulk'
        }

class SpiderView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return {
            'h1': 'Hero: Spider Man',
            'h2': 'a Marvel comic hero straight from the spiderverse', 
            'p': 'Spiderman first appeared in Amazing Fantasy #15, which was the last issue of the series...',
            'img': '/static/images/spider_man.jpg',
            'alt': 'spider_man'
        }

class ThorView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return {
            'h1': 'Hero: Thor',
            'h2': 'a Marvel comic named Thor Odinson, possessing a mighty hammer', 
            'p': 'This comic hero is named after a Norse deity under the same name...',
            'img': '/static/images/thor.jpg',
            'alt': 'thor'
        }
        

# Create your views here.
