# hero/views.py
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, ListView, TemplateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from os.path import exists
from django.urls import reverse_lazy

from .models import Superhero


# class HomeView(TemplateView):
#     template_name = 'hero_detail.html'
    
#     def get_context_data(self,**kwargs):
#         hero = Superhero.objects.get(pk=1)
#         return {'hero': hero}

class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/' + image):
            kwargs['missing'] = True
        return kwargs

class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero

# class HeroDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = "hero_delete.html"
#     model = Superhero
#     success_url = reverse_lazy('')

# class HeroDeleteView(DeleteView):
#     model = Superhero
#     template_name = 'hero_delete.html'
#     context_object_name = 'hero'

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.userprofile.soft_delete()
#         messages.success(request, 'Hero Deleted Successfully.')
#         return HttpResponseRedirect(reverse('')) 

# class HeroDeleteView(DeleteView):
#     template_name = "hero_delete.html"
#     model = Superhero
#     success_url = reverse_lazy('')
     
#     def delete_view(request, id): 
#         context = {} 
#         obj = get_object_or_404(Superhero, id = id) 
  
#         if request.method =="POST": 
#             obj.delete() 
#             return HttpResponseRedirect("/") 
  
#         return render(request, "hero_delete.html", context) 

class HeroAddView(LoginRequiredMixin, CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
class HeroEditView(LoginRequiredMixin, UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
