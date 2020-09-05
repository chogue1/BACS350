from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page',
            'body': 'There are many like this but this one is mine',
        }
    
class HomeView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page',
            'body': 'There are many like this but this one is mine',
        }
    
class ProfileView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Profile Page',
            'body': 'There are many like this but this one is mine',
        }
    
class HeroView(TemplateView):
    template_name = "hero.html"
    def get_context_data(self, **kwargs):
        return { 'hero': kwargs['identity'] }