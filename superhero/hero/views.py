from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return { 
            'hero': 'hulk',
            'title': 'The hulk is a fictional Marvel superhero, the second face of Dr Robert Bruce Banner',
            'body' : 'His debut issue of The Incredible Hulk told both sides to his story.',
        }
    
class WidowView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return { 
            'hero': 'black_widow',
            'title': 'Natasha Romanova AKA Наталья Альяновна "Наташа" Романова, is a fictional Marvel Superhero',
            'body' : 'Her debut was featured in Tales of Suspense #52 as a Russian spy and antagonist to Iron Man...',
        }
    
class LanternView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return { 
            'hero': 'green_lantern',
            'title': 'a DC comic hero considered to be a staple of the American fantasy',
            'body': 'Green Lantern first appeared in All-American Comics #16, which then an entire series was written in 1941...',             
               }

class ThorView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return { 
            'hero': 'thor',
            'title': 'a Marvel comic named Thor Odinson, possessing a mighty hammer',
            'body': 'This comic hero is named after a Norse deity under the same name...',             
               }
    
class SpiderView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return { 
            'hero': 'spider_man',
            'title': 'a Marvel comic hero straight from the spiderverse',
            'body': 'Spiderman first appeared in Amazing Fantasy #15, which was the last issue of the series...',             
               }

