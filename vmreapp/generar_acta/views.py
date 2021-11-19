from django.shortcuts import render

import pandas as pd
import time
import math
from funciones import numero_letras as numerosLetras
#**********************************PDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create your views here.





def gen_acta(request):
        
    #**********************************FUNCIONES VOTOS
    def fraccionVotos(votosTotalCoalicion, dividendo):
        fracicion = votosTotalCoalicion/dividendo
        fracicion = math.floor(fracicion)
        #print("1-->" + str (fracicion))
        return fracicion
    #********************************************************************
    def fraccionSobrante(votosTotalCoalicion, dividendo):
        fracicion = votosTotalCoalicion/dividendo
        fracicion = math.floor(fracicion)
        fraccionSobranteR = votosTotalCoalicion-fracicion*dividendo
        #print("2-->" + str (fraccionSobranteR))
        return fraccionSobranteR
    #**********************************
    def divicionDeVotos(fraccionVotos, partidos):
        for part in partidos:
            sumaCol[part] = sumaCol[part] + fraccionVotos
    #**********************************
    def divicionDeVotosSobranteUno(fraccionSobrante, partidos):
        if len(partidos) == 3:
            partidoMayor = elMayor(partidos)
            sumaCol[partidoMayor] = sumaCol[partidoMayor] + fraccionSobrante
        
        else:
            if(sumaCol[partidos[0]] == sumaCol[partidos[1]]):
                sumaCol[partidos[0]] = sumaCol[partidos[0]] + fraccionSobrante
            else:
                partidoMayor = elMayor(partidos)
                sumaCol[partidoMayor] = sumaCol[partidoMayor] + fraccionSobrante

    #**********************************
    def divicionDeVotosSobranteDos(fraccionSobrante, partidos):
        if( fraccionSobrante == 2  )    :
            fraccionSobrante = fraccionSobrante -1
            if(sumaCol[partidos[0]] == sumaCol[partidos[1]] and
            sumaCol[partidos[0]] == sumaCol[partidos[2]]):
                sumaCol[partidos[0]] = sumaCol[partidos[0]] + fraccionSobrante
                sumaCol[partidos[1]] = sumaCol[partidos[1]] + fraccionSobrante
            else:
                partidoMayor = elMayor(partidos)
                sumaCol[partidoMayor] = sumaCol[partidoMayor] + fraccionSobrante
                if(len(partidos) > 2 ):
                    partidos.remove(partidoMayor)
                divicionDeVotosSobranteUno(fraccionSobrante, partidos)
        else:
            divicionDeVotosSobranteUno(fraccionSobrante, partidos)
    #**********************************
    def divicionDeVotosSobranteTres(fraccionSobrante, partidos):
        if( fraccionSobrante == 3 ):
            fraccionSobrante = fraccionSobrante - 2
            if(sumaCol[partidos[0]] == sumaCol[partidos[1]] and
            sumaCol[partidos[0]] == sumaCol[partidos[2]] and
            sumaCol[partidos[0]] == sumaCol[partidos[3]]):
                sumaCol[partidos[0]] = sumaCol[partidos[0]] + fraccionSobrante
                sumaCol[partidos[1]] = sumaCol[partidos[1]] + fraccionSobrante
                sumaCol[partidos[2]] = sumaCol[partidos[3]] + fraccionSobrante
            else:
                partidoMayor = elMayor(partidos)
                sumaCol[partidoMayor] = sumaCol[partidoMayor] + fraccionSobrante
                if(len(partidos) > 3 ):
                    partidos.remove(partidoMayor)
                divicionDeVotosSobranteDos(fraccionSobrante+1, partidos)
        else:
            divicionDeVotosSobranteDos(fraccionSobrante, partidos)

    #**********************************
    def elMayor(partidos):
        elMayorNum=0
        elMayorStr=""
        for part in partidos:
            if(sumaCol_abc[part] > elMayorNum):
                elMayorNum = sumaCol_abc[part]
                elMayorStr = part
                #print(sumaCol[part])
            #else:
                #print("NADA")
        return elMayorStr
    #**********************************
    def excel01():
        sumaColExcel01=df.groupby(by=['estados']).sum().groupby(level=[0]).cumsum().loc[estado]
        totalDefExc = math.floor(sumaColExcel01['PAN']) + math.floor(sumaColExcel01['PRI']) + math.floor(sumaColExcel01['PRD']) + math.floor(sumaColExcel01['PT']) + math.floor(sumaColExcel01['VERDE']) + math.floor(sumaColExcel01['MOVIMIENTO_CIUDADANO']) + math.floor(sumaColExcel01['MORENA']) + math.floor(sumaColExcel01['VERDE_PT_MORENA']) + math.floor(sumaColExcel01['VERDE_PT']) + math.floor(sumaColExcel01['VERDE_MORENA']) + math.floor(sumaColExcel01['PT_MORENA']) + math.floor(sumaColExcel01['CANDIDATOS_NO_REGISTRADOS']) + math.floor(sumaColExcel01['VOTOS_NULOS'])
        datos=(
        ('PAN', math.floor(sumaColExcel01['PAN']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['PAN']))),
        ('PRI', math.floor(sumaColExcel01['PRI']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['PRI']))),
        ('PRD', math.floor(sumaColExcel01['PRD']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['PRD']))),
        ('VERDE', math.floor(sumaColExcel01['VERDE']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['VERDE']))),
        ('PT', math.floor(sumaColExcel01['PT']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['PT']))),
        ('MOVIMIENTO CIUDADANO', math.floor(sumaColExcel01['MOVIMIENTO_CIUDADANO']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['MOVIMIENTO_CIUDADANO']))),
        ('MORENA', math.floor(sumaColExcel01['MORENA']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['MORENA']))),
        ('VERDE_PT_MORENA', math.floor(sumaColExcel01['VERDE_PT_MORENA']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['VERDE_PT_MORENA']))),
        ('VERDE_PT', math.floor(sumaColExcel01['VERDE_PT']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['VERDE_PT']))),
        ('VERDE_MORENA', math.floor(sumaColExcel01['VERDE_MORENA']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['VERDE_MORENA']))),
        ('PT_MORENA', math.floor(sumaColExcel01['PT_MORENA']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['PT_MORENA']))),
        ('CANDIDATOS_NO_REGISTRADOS', math.floor(sumaColExcel01['CANDIDATOS_NO_REGISTRADOS']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['CANDIDATOS_NO_REGISTRADOS']))),
        ('VOTOS_NULOS', math.floor(sumaColExcel01['VOTOS_NULOS']),numerosLetras.numero_a_letras(math.floor(sumaColExcel01['VOTOS_NULOS']))),
        ('TOTAL', totalDefExc, numerosLetras.numero_a_letras(totalDefExc))
        )
        
        return datos
    #**********************************
    def excel02():        
        totalDefExc = math.floor(sumaCol['PAN']) + math.floor(sumaCol['PRI']) + math.floor(sumaCol['PRD']) + math.floor(sumaCol['PT']) + math.floor(sumaCol['VERDE']) + math.floor(sumaCol['MOVIMIENTO_CIUDADANO']) + math.floor(sumaCol['MORENA']) + math.floor(sumaCol['CANDIDATOS_NO_REGISTRADOS']) + math.floor(sumaCol['VOTOS_NULOS'])
        datos=(
        ('PAN', math.floor(sumaCol['PAN']),numerosLetras.numero_a_letras(math.floor(sumaCol['PAN']))),
        ('PRI', math.floor(sumaCol['PRI']),numerosLetras.numero_a_letras(math.floor(sumaCol['PRI']))),
        ('PRD', math.floor(sumaCol['PRD']),numerosLetras.numero_a_letras(math.floor(sumaCol['PRD']))),
        ('VERDE', math.floor(sumaCol['VERDE']),numerosLetras.numero_a_letras(math.floor(sumaCol['VERDE']))),
        ('PT', math.floor(sumaCol['PT']),numerosLetras.numero_a_letras(math.floor(sumaCol['PT']))),
        ('MOVIMIENTO CIUDADANO', math.floor(sumaCol['MOVIMIENTO_CIUDADANO']),numerosLetras.numero_a_letras(math.floor(sumaCol['MOVIMIENTO_CIUDADANO']))),
        ('MORENA', math.floor(sumaCol['MORENA']),numerosLetras.numero_a_letras(math.floor(sumaCol['MORENA']))),
        ('CANDIDATOS_NO_REGISTRADOS', math.floor(sumaCol['CANDIDATOS_NO_REGISTRADOS']),numerosLetras.numero_a_letras(math.floor(sumaCol['CANDIDATOS_NO_REGISTRADOS']))),
        ('VOTOS_NULOS', math.floor(sumaCol['VOTOS_NULOS']),numerosLetras.numero_a_letras(math.floor(sumaCol['VOTOS_NULOS']))),
        ('TOTAL', totalDefExc, numerosLetras.numero_a_letras(totalDefExc))
        )
        #rb = open_workbook('Nayarit.xls',formatting_info=True)
        #wb = copy(rb)
        #sheet = wb.get_sheet('dato')
        #sheet.write(1,3,"Votos Fracionados")
        #row1=2
        #row2=2
        #for dato in zip(datos):
        #    sheet.write(row1, 4, str(dato[0][0]))
        #    sheet.write(row2, 3, dato[0][1])
        #    row1 = row1 + 1
        #    row2 = row2 + 1
        #wb.save('Nayarit.xls')
        return datos
    #**********************************                
    def excel03():    
        sumaColExcel01Excel01=df.groupby(by=['estados']).sum().groupby(level=[0]).cumsum().loc[estado]    
        datos=[
        (
            'PAN', math.floor(sumaColExcel01Excel01['PAN']),
            numerosLetras.numero_a_letras(math.floor(sumaColExcel01Excel01['PAN']))
        ),
        (
            'PRI', math.floor(sumaColExcel01Excel01['PRI'] ),
            numerosLetras.numero_a_letras(math.floor(sumaColExcel01Excel01['PRI']   ))
        ),
        (
            'PRD', math.floor(sumaColExcel01Excel01['PRD']), numerosLetras.numero_a_letras(sumaColExcel01Excel01['PRD'])
        ),
        (
            'VERDE_PT_MORENA', math.floor(sumaColExcel01Excel01['VERDE_PT_MORENA'] + sumaColExcel01Excel01['VERDE_PT'] + sumaColExcel01Excel01['VERDE_MORENA'] + sumaColExcel01Excel01['PT_MORENA'] + sumaColExcel01Excel01['VERDE'] + sumaColExcel01Excel01['PT'] + sumaColExcel01Excel01['MORENA']), numerosLetras.numero_a_letras(sumaColExcel01Excel01['VERDE_PT_MORENA'] + sumaColExcel01Excel01['VERDE_PT'] + sumaColExcel01Excel01['VERDE_MORENA'] + sumaColExcel01Excel01['PT_MORENA'] + sumaColExcel01Excel01['VERDE'] + sumaColExcel01Excel01['PT'] + sumaColExcel01Excel01['MORENA'])
        ),
        (
            'MOVIMIENTO_CIUDADANO', math.floor(sumaColExcel01Excel01['MOVIMIENTO_CIUDADANO'] ),
            numerosLetras.numero_a_letras(math.floor(sumaColExcel01Excel01['MOVIMIENTO_CIUDADANO']   ))
        ),
        (
            'CANDIDATOS_NO_REGISTRADOS', math.floor(sumaColExcel01Excel01['CANDIDATOS_NO_REGISTRADOS']), numerosLetras.numero_a_letras(sumaColExcel01Excel01['CANDIDATOS_NO_REGISTRADOS'])
            ),
        (
            'VOTOS_NULOS', math.floor(sumaColExcel01Excel01['VOTOS_NULOS']), numerosLetras.numero_a_letras(sumaColExcel01Excel01['VOTOS_NULOS'])
            )
        ]
        return datos
    
    
    
    
    
    
    
    #**********************************VAR
    partidos=[]
    estado='Nayarit'
    coalicionDeCuatroPartidoUno=""
    coalicionDeCuatroPartidoDos=""
    coalicionDeCuatroPartidoTres=""
    coalicionDeCuatroPartidoCuatro=""
    coalicionDeCuatroPargtidos=""
    coalicionDeTresPartidoUno=""
    coalicionDeTresPartidoDos=""
    coalicionDeTresPartidoTres=""
    coalicionDeTresPartidos=""
    coalicionDeDosPartidoUno=""
    coalicionDeDosPartidoDos=""
    coalicionDeDosPartidos=""
    dia=time.strftime('%d', time.localtime())
    hora=time.strftime('%H:%M:%S', time.localtime())
    #**********************************ARCHIVO
    url=""
    try:
        url = "C:\\vmre\data\\vmre.xlsx"
        print("Inicia " + estado)
    except:
        print("Verificar la ruta --> " + url)
    vmre = pd.ExcelFile(url)
    df=vmre.parse('Hoja1')
    #**********************************AGRUPAR
    sumaCol=df.groupby(by=['estados']).sum().groupby(level=[0]).cumsum().loc[estado]
    sumaCol_abc=df.groupby(by=['estados']).sum().groupby(level=[0]).cumsum().loc[estado]
    
    #**********************************
    divicionDeVotos(fraccionVotos(votosTotalCoalicion=sumaCol['VERDE_PT_MORENA'], dividendo=3), partidos=["VERDE","PT","MORENA"])
    divicionDeVotosSobranteTres(fraccionSobrante(votosTotalCoalicion=sumaCol['VERDE_PT_MORENA'], dividendo=3), partidos=["VERDE","PT","MORENA"] )
    #**********************************
    divicionDeVotos(fraccionVotos(votosTotalCoalicion=sumaCol['VERDE_PT'], dividendo=2), partidos=["VERDE","PT"])
    divicionDeVotosSobranteTres(fraccionSobrante(votosTotalCoalicion=sumaCol['VERDE_PT'], dividendo=2), partidos=["VERDE","PT"] )
    ##**********************************
    divicionDeVotos(fraccionVotos(votosTotalCoalicion=sumaCol['VERDE_MORENA'], dividendo=2), partidos=["VERDE","MORENA"])
    divicionDeVotosSobranteTres(fraccionSobrante(votosTotalCoalicion=sumaCol['VERDE_MORENA'], dividendo=2), partidos=["VERDE","MORENA"] )
    ##**********************************
    divicionDeVotos(fraccionVotos(votosTotalCoalicion=sumaCol['PT_MORENA'], dividendo=2), partidos=["PT","MORENA"])
    divicionDeVotosSobranteTres(fraccionSobrante(votosTotalCoalicion=sumaCol['PT_MORENA'], dividendo=2), partidos=["PT","MORENA"] )
    ##**********************************
    #*********************PDF
    path="C:/vmre/data/"
    tb1=excel01()
    tb2=excel02()
    tb3=excel03()
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    #can.drawString(90, 529, "Nayarit")
    can.drawString(22,  496, str(hora))
    can.drawString(109, 496, str(dia))
    can.drawString(30, 511, "CENTRO DE ESCRUTINIO Y CÓMPUTO")
    can.drawString(90, 296, tb1[0][2]) 
    can.drawString(280, 296, str(tb1[0][1])) 
    can.drawString(90, 277, tb1[1][2]) 
    can.drawString(280, 277, str(tb1[1][1])) 
    can.drawString(90, 258, tb1[2][2]) 
    can.drawString(280, 258, str(tb1[2][1])) 
    can.drawString(90, 239, tb1[3][2]) 
    can.drawString(280, 239, str(tb1[3][1])) 
    can.drawString(90, 220, tb1[4][2]) 
    can.drawString(280, 220, str(tb1[4][1])) 
    can.drawString(90, 201, tb1[5][2]) 
    can.drawString(280, 201, str(tb1[5][1])) 
    can.drawString(90, 182, tb1[6][2]) 
    can.drawString(280, 182, str(tb1[6][1]))
    can.drawString(90, 160, tb1[7][2]) 
    can.drawString(280, 160, str(tb1[7][1]))  
    can.drawString(90, 141, tb1[8][2]) 
    can.drawString(280, 141, str(tb1[8][1]))  
    can.drawString(90, 121, tb1[9][2]) 
    can.drawString(280, 121, str(tb1[9][1]))  
    can.drawString(90, 101, tb1[10][2]) 
    can.drawString(280, 101, str(tb1[10][1]))  
    can.drawString(90, 80, tb1[11][2]) 
    can.drawString(280, 80, str(tb1[11][1]))  
    can.drawString(90, 60, tb1[12][2]) 
    can.drawString(280, 60, str(tb1[12][1]))  
    can.drawString(90, 41, tb1[13][2]) 
    can.drawString(280, 41, str(tb1[13][1]))  
    
    ##tb2
    #   
    can.drawString(400, 510, tb2[0][2]) 
    can.drawString(590, 510, str(tb2[0][1]))  
    can.drawString(400, 484, tb2[1][2]) 
    can.drawString(590, 484, str(tb2[1][1]))  
    can.drawString(400, 457, tb2[2][2]) 
    can.drawString(590, 457, str(tb2[2][1]))  
    can.drawString(400, 430, tb2[3][2]) 
    can.drawString(590, 430, str(tb2[3][1]))  
    can.drawString(400, 403, tb2[4][2]) 
    can.drawString(590, 403, str(tb2[4][1]))  
    can.drawString(400, 376, tb2[5][2]) 
    can.drawString(590, 376, str(tb2[5][1]))  
    can.drawString(400, 351, tb2[6][2]) 
    can.drawString(590, 351, str(tb2[6][1]))  
    can.drawString(400, 324, tb2[7][2]) 
    can.drawString(590, 324, str(tb2[7][1]))  
    can.drawString(400, 298, tb2[8][2]) 
    can.drawString(590, 298, str(tb2[8][1]))  
    can.drawString(400, 273, tb2[9][2]) 
    can.drawString(590, 273, str(tb2[9][1]))  
    #Tb3
    can.drawString(400, 220, tb3[0][2]) 
    can.drawString(590, 220, str(tb3[0][1]))  
    can.drawString(400, 190, tb3[1][2]) 
    can.drawString(590, 190, str(tb3[1][1]))  
    can.drawString(400, 160, tb3[2][2]) 
    can.drawString(590, 160, str(tb3[2][1]))  
    can.drawString(400, 134, tb3[3][2]) 
    can.drawString(590, 134, str(tb3[3][1]))  
    can.drawString(400, 106, tb3[4][2]) 
    can.drawString(590, 106, str(tb3[4][1]))  
    can.drawString(400, 79, tb3[5][2]) 
    can.drawString(590, 79, str(tb3[5][1]))   
    can.drawString(400, 50, tb3[6][2]) 
    can.drawString(590, 50, str(tb3[6][1])) 
        
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(path+"pdfOrg/nayarit.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(path+"pdfNew/nayarit.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    print("Termina " + estado)
    
    return render(request, "generar_acta/gen_acta.html")