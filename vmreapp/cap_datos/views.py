from django.http import HttpResponse
from django.shortcuts import render


def cap_datos(request):
    return render(request, "cap_datos/cap_datos.html")