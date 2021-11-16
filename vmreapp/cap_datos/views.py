import  openpyxl
from django.shortcuts import render
from cap_datos import models


def cap_datos(request):

    path = "C:\\vmre\data\\vmre.xlsx"
    libro = openpyxl.load_workbook(path)
    
    
    hoja = libro.active
    
    
    if request.method == "POST":
        print(request.POST)
        print("##########")
        print(request.POST.get("pan_postal", None))
        
        partido = "PAN"
        voto_postal = request.POST.get("pan_postal", None)
        voto_internet = request.POST.get("pan_internet", None)
        hoja["D2"] = voto_postal
        hoja["D3"] = voto_internet
        
        partido = "PRI"
        voto_postal = request.POST.get("pri_postal", None)
        voto_internet = request.POST.get("pri_internet", None)
        hoja["E2"] = voto_postal
        hoja["E3"] = voto_internet
        
        partido = "PRD"
        voto_postal = request.POST.get("prd_postal", None)
        voto_internet = request.POST.get("prd_internet", None)
        hoja["F2"] = voto_postal
        hoja["F3"] = voto_internet
        
        partido = "VERDE"
        voto_postal = request.POST.get("verde_postal", None)
        voto_internet = request.POST.get("verde_internet", None)
        hoja["G2"] = voto_postal
        hoja["G3"] = voto_internet
        
        
        partido = "PT"
        voto_postal = request.POST.get("pt_postal", None)
        voto_internet = request.POST.get("pt_internet", None)
        hoja["H2"] = voto_postal
        hoja["H3"] = voto_internet
        
              
        
        partido = "MOVIMIENTO_CIUDADANO"
        voto_postal = request.POST.get("mov_ciuda_postal", None)
        voto_internet = request.POST.get("mov_ciuda_internet", None)
        hoja["I2"] = voto_postal
        hoja["I3"] = voto_internet
        
        
        partido = "MORENA"
        voto_postal = request.POST.get("morena_postal", None)
        voto_internet = request.POST.get("morena_internet", None)
        hoja["J2"] = voto_postal
        hoja["J3"] = voto_internet
        
        
        partido = "VERDE_PT_MORENA"
        voto_postal = request.POST.get("verde_pt_morena_postal", None)
        voto_internet = request.POST.get("verde_pt_morena_internet", None)
        hoja["K2"] = voto_postal
        hoja["K3"] = voto_internet
        
        
        partido = "VERDE_PT"
        voto_postal = request.POST.get("verde_pt_postal", None)
        voto_internet = request.POST.get("verde_pt_internet", None)
        hoja["L2"] = voto_postal
        hoja["L3"] = voto_internet
        
        
        partido = "VERDE_MORENA"
        voto_postal = request.POST.get("verde_morena_postal", None)
        voto_internet = request.POST.get("verde_morena_internet", None)
        hoja["M2"] = voto_postal
        hoja["M3"] = voto_internet
        
        
        partido = "PT_MORENA"
        voto_postal = request.POST.get("pt_morena_postal", None)
        voto_internet = request.POST.get("pt_morena_internet", None)
        hoja["N2"] = voto_postal
        hoja["N3"] = voto_internet
        
        partido = "NO_REGISTRO"
        voto_postal = request.POST.get("no_registro_postal", None)
        voto_internet = request.POST.get("no_registro_internet", None)
        hoja["O2"] = voto_postal
        hoja["O3"] = voto_internet
        
        partido = "VOTOS_NULOS"
        voto_postal = request.POST.get("votos_nulos_postal", None)
        voto_internet = request.POST.get("votos_nulos_internet", None)
        hoja["P2"] = voto_postal
        hoja["P3"] = voto_internet
        
        
        libro.save(path)
        
        
    
    return render(request, "cap_datos/cap_datos.html")