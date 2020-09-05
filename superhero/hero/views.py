from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hulk.html'
    def get_context_data(self, **kwargs):
        return { 'hero': 'hulk' }
    
class WidowView(TemplateView):
    template_name = 'black_widow.html'
    def get_context_data(self, **kwargs):
        return { 'hero': 'black_widow' }

