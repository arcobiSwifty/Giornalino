from django.utils import timezone
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

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
        ctx = {'is_staff': request.user.is_staff}
        ctx['anni'] = ReleaseYear.objects.all()
        ctx['argomenti'] = Theme.objects.all()
        return render(request, self.template_name, ctx)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        print(context)
        return context

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

def ArticoliArgomento(request, argomento):
    articoli = Article.objects.filter(approved=True).filter(argument=Theme.objects.get(url_name=argomento))
    paginator = Paginator(articoli, 20)
    page_ctx = request.GET.get('page')
    if page_ctx == None:
        page = paginator.page(1)
    else:
        page = paginator.page(page_ctx)
    return render(request, 'app/article_list.html', {'object_list': articoli, 'is_paginated': paginator.count>1, 'page_obj': page, 'argomento': argomento})

def ArticoliAnno(request, anno):
    articoli = Article.objects.filter(approved=True).filter(release_year=ReleaseYear.objects.get(year=int(anno)))
    paginator = Paginator(articoli, 20)
    page_ctx = request.GET.get('page')
    if page_ctx == None:
        page = paginator.page(1)
    else:
        page = paginator.page(page_ctx)
    return render(request, 'app/article_list.html', {'object_list': articoli, 'is_paginated': paginator.count>1, 'page_obj': page, 'anno': anno})



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
