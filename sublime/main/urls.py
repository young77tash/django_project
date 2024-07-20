from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('question', views.question, name='question'),
    path('money', views.money, name='money'),
]
