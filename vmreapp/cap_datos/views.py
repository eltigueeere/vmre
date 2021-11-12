from django.http import HttpResponse
from django.shortcuts import render
from cap_datos import models


def cap_datos(request):
    
    if request.method == "POST":
        print(request.POST)
        print("##########")
        print(request.POST.get("pan_postal", None))
        
        partido = "PAN"
        voto_postal = request.POST.get("pan_postal", None)
        voto_internet = request.POST.get("pan_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
    
    return render(request, "cap_datos/cap_datos.html")