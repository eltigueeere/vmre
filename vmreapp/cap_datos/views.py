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
        
        
        partido = "PRI"
        voto_postal = request.POST.get("pri_postal", None)
        voto_internet = request.POST.get("pri_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        partido = "PRD"
        voto_postal = request.POST.get("prd_postal", None)
        voto_internet = request.POST.get("prd_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        partido = "VERDE"
        voto_postal = request.POST.get("verde_postal", None)
        voto_internet = request.POST.get("verde_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
        partido = "PT"
        voto_postal = request.POST.get("pt_postal", None)
        voto_internet = request.POST.get("pt_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
              
        
        partido = "MOVIMIENTO_CIUDADANO"
        voto_postal = request.POST.get("mov_ciuda_postal", None)
        voto_internet = request.POST.get("mov_ciuda_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
        partido = "MORENA"
        voto_postal = request.POST.get("morena_postal", None)
        voto_internet = request.POST.get("morena_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
        partido = "VERDE_PT_MORENA"
        voto_postal = request.POST.get("verde_pt_morena_postal", None)
        voto_internet = request.POST.get("verde_pt_morena_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
        partido = "VERDE_PT"
        voto_postal = request.POST.get("verde_pt_postal", None)
        voto_internet = request.POST.get("verde_pt_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
        partido = "VERDE_MORENA"
        voto_postal = request.POST.get("verde_morena_postal", None)
        voto_internet = request.POST.get("verde_morena_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
        partido = "PT_MORENA"
        voto_postal = request.POST.get("pt_morena_postal", None)
        voto_internet = request.POST.get("pt_morena_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        partido = "NO_REGISTRO"
        voto_postal = request.POST.get("no_registro_postal", None)
        voto_internet = request.POST.get("no_registro_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        partido = "VOTOS_NULOS"
        voto_postal = request.POST.get("votos_nulos_postal", None)
        voto_internet = request.POST.get("votos_nulos_internet", None)
        twz = models.votos.objects.create(partido = partido, voto_postal=voto_postal, voto_internet=voto_internet)
        twz.save()
        
        
    
    return render(request, "cap_datos/cap_datos.html")