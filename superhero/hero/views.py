from django.views.generic import TemplateView

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

