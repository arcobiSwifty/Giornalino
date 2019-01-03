from django.utils import timezone
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import views as auth_views


from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ReleaseYear, Article, Theme, Edition
from .forms import CreaArticolo


#TODO:
#implement edizioni (aggiungi + rimuovi)
#implement filter articoli by name and by theme
#implement images (giornalino's pdf)
#UI


class Home(View):
    template_name = 'home.html'
    def get(self, request):
        is_staff = request.user.is_staff
        return render(request, self.template_name, {'is_staff': is_staff})

class Approvals(View):
    template_name = 'approvals.html'
    def get(self, request):
        if request.user.is_staff:
            articoli = Article.objects.filter(approved=False)
            return render(request, self.template_name, {'articles': articoli})
        return HttpResponse('<b>404 page not found</b>')

class ArticoliList(ListView):
    queryset = Article.objects.filter(approved=True)
    paginate_by = 20
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

class ArticoliDelete(DeleteView):
    model = Article
    success_url = '/approva'

class ArticoliCrea(CreateView):
    template_name = 'app/article_create.html'
    form_class = CreaArticolo
    success_url = '/success'

    def form_valid(self, form):
        now = datetime.datetime.now()
        article = form.save(commit=False)
        article.author = self.request.user
        article.release_year = ReleaseYear.objects.get(year=int(now.year))
        article.save()
        return super().form_valid(form)

class ArticoliApprova(UpdateView):
    model = Article
    fields = ['approved']
    success_url = '/approva'
    template_name_suffix = '_update_form'


class Success(View):
    template_name = 'success.html'
    def get(self, request):
        return render(request, self.template_name)
