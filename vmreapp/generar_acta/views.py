from django.shortcuts import render, HttpResponse

# Create your views here.


def gen_acta(request):
    return render(request, "generar_acta/gen_acta.html")