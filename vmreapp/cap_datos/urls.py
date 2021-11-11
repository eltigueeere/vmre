from django.urls import path

from . import views

urlpatterns = [
    path('', views.cap_datos, name='cap_datos'),
]