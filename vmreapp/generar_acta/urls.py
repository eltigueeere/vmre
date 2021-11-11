from django.urls import path

from . import views

urlpatterns = [
    path('', views.gen_acta, name='gen_acta'),
]