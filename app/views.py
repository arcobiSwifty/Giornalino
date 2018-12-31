from django.utils import timezone

from django.shortcuts import render

from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ReleaseYear, Article, Theme, Edition
# Create your views here.
class Home(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name, {})

class ArticoliList(ListView):
    model = Article
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticoliDetail(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
