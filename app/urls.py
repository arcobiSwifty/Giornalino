from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Home.as_view()),
    path('accounts/login', auth_views.LoginView.as_view()),
    path('accounts/logout', auth_views.LogoutView.as_view()),
    path('articoli', views.ArticoliList.as_view(), name='articoli-list'),
    path('articoli/<int:pk>', views.ArticoliDetail.as_view(), name='articoli-detail'),
    path('crea', login_required(views.ArticoliCrea.as_view()), name='articoli-crea'),
    path('success', views.Success.as_view(), name='success'),
]
