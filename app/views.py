from django.utils import timezone
import datetime

from django.shortcuts import render

from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ReleaseYear, Article, Theme, Edition
from .forms import CreaArticolo

class Success(View):
    template_name = 'success.html'
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

class ArticoliCrea(CreateView):
    template_name = 'app/article_create.html'
    form_class = CreaArticolo
    success_url = '/success'

    def form_valid(self, form):
        now = datetime.datetime.now()
        article = form.save(commit=False)
        article.release_year = ReleaseYear.objects.get_or_create(year=int(now.year))
        article.save()
        return super().form_valid(form)
