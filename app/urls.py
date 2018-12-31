from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('articoli', views.ArticoliList.as_view(), name='articoli-list'),
    path('articoli/<int:pk>', views.ArticoliDetail.as_view(), name='articoli-detail'),
    path('crea', views.ArticoliCrea.as_view(), name='articoli-crea'),
    path('success', views.Success.as_view(), name='success'),
]
