from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Superhero
"""
class HomeView(TemplateView):
    template_name = 'hero_detail.html'
    
    def get_context_data(self,**kwargs):
        hero = Superhero.objects.get(pk=1)
        return {'hero': hero}
"""
class HeroDetail(DetailView):
    template_name = "hero_detail.html"
    model = Superhero

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/' + image):
            kwargs['missing'] = True
        return kwargs

class HeroIndex(ListView):
    template_name = "hero_index.html"
    model = Superhero

class HeroCreate(CreateView):
    template_name = "hero_create.html"
    model = Superhero
    fields = '__all__'

class HeroUpdate(UpdateView):
    template_name = "hero_update.html"
    model = Superhero
    fields = '__all__'


# Create your views here.

