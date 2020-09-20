from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'superhero-theme.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page',
            'body': 'There are many like this but this one is mine',
        }
    
class HomeView(TemplateView):
    template_name = 'superhero-theme.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'The SuperHero News Network',
            'body': 'There are many like this but this one is mine',
        }
    
class IndexView(TemplateView):
    template_name = 'superhero-theme.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'The Superhero Index',
            'body': 'There are many like this but this one is mine',
        }
    
class HeroView(TemplateView):
    template_name = "hero.html"
    def get_context_data(self, **kwargs):
        return { 'hero': kwargs['identity'] }