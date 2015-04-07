# -*- coding: iso-8859-15
import sys
import os
LOTE_DE_DATOS=0
if len(sys.argv) >= 2: 
    print sys.argv[1] 
    LOTE_DE_DATOS=sys.argv[1] ### Debe ser un Numero Entero
else:

    print "Necesito un parámetro"
     
####extraer las variables en arreglos
import xlwt
from xlwt import *
from numpy import *
import numpy as np
from datetime import datetime, date, time, timedelta
import random

def extraer_redcap(URL, API_KEY , VARIABLES_REDCap):
    
    from redcap import Project, RedcapError
    project = Project(URL, API_KEY)
    fields_of_interest = VARIABLES_REDCap
    subset = project.export_records(fields=fields_of_interest)
    return subset

######VARIABLES GLOBALES##################

## 'fecha_nacimiento','fecha_toma','sexo','lugar_de_toma','obs','muestras_complete','nombre_completo','nombres_complete',
VARIABLES=['codigo_de_muestra','cod_tarjeta','lote','type_dat','cartina_libre','acetil_carnitina','propionil','butiril','t3oh_butiril','tiglil','isovaleril','t3oh_isovaleril','hexanoil','t3oh_hexanoil','octenoil','octanoil','malonil','c10_2','decenoil','decanoil','metilmalonil','glutaril','dodecenoil','dodecanoil','t3me_glutaril','c12_oh','c14_2','c14_1','miristoil','c14_oh','c16_1','palmitoil','c16_1_oh','c16_oh','c16_dc','c18_2','c18_1','estearoil','c18_2_oh','c18_1_oh','c18_oh','c3_c2','c3_c16','c4_c2','c4_c3','c4_c8','c5_c0','c5_c2','c5_c3','c5oh_c8','c5oh_c0','c8_c2','c8_c10','c3dc_c10','glut_c5oh','glut_c8','glut_c16','c14_1_c16','c16oh_c16','c10_2_c10','acs_cit','c0__c16_c18_','c16_c18_1__c2','d9_c1','d_c3','d_c4','d3_c8','d9_c14','d3_c16','glicina','alanina','valina','xleucina','metionina','his_mrm','citrulina','fenilalanina','tirosina','aspartato','glutamato','ornitina','arginina','asa','prolina','ohpro','treo_mrm','ser_mrm','succinil_ac','figlu','val_fen','xleu_fen','xleu_ala','met_fen','cit_arg','fen_tyr','asa_arg','tyr_cit','c3_met','x_v_p_t','d2_glic','d8_val','d3_xleu','dxleu_mrm','d3_met','d5_fen','d6_tir','d2_orn','d4c_arg','d2_cit','sca_is','resultados_complete'
]
NEONATOS=extraer_redcap('http://claimproject.com/redcap570/api/',
                         'EF188911E775BD0103F6E9D6E4DC68F0' ,VARIABLES)
FILA=5 ##en que fila de la hoja de excel empieza a escribir
TIPO_DE_DATOS='2' ##2 = tipo de dato Resultados
#LOTE_DE_DATOS='2'

Percentil_mayor=99
Percentil_menor=1

PERCENTILES_CHEMOVIEW=[{"variable":"cartina_libre","sup":"71.5","inf":"13.3"},
{"variable":"acetil_carnitina","sup":"39","inf":"8.6"},
{"variable":"propionil","sup":"2.6","inf":"0.01"},
{"variable":"butiril","sup":"0.64","inf":"0.01"},
{"variable":"t3oh_butiril","sup":"0.45","inf":"0.01"},
{"variable":"tiglil","sup":"0.2","inf":"0"},
{"variable":"isovaleril","sup":"0.48","inf":"0.01"},
{"variable":"t3oh_isovaleril","sup":"0.43","inf":"0.01"},
{"variable":"hexanoil","sup":"0.38","inf":"0.01"},
{"variable":"t3oh_hexanoil","sup":"0.31","inf":"0.01"},
{"variable":"octenoil","sup":"0.37","inf":"0.01"},
{"variable":"octanoil","sup":"0.35","inf":"0.01"},
{"variable":"malonil","sup":"0.31","inf":"0"},
{"variable":"c10_2","sup":"0.22","inf":"0.01"},
{"variable":"decenoil","sup":"0.28","inf":"0.01"},
{"variable":"decanoil","sup":"0.4","inf":"0.01"},
{"variable":"metilmalonil","sup":"0.67","inf":"0.01"},
{"variable":"glutaril","sup":"0.24","inf":"0.01"},
{"variable":"dodecenoil","sup":"0.27","inf":"0"},
{"variable":"dodecanoil","sup":"0.85","inf":"0.02"},
{"variable":"t3me_glutaril","sup":"0.24","inf":"0"},
{"variable":"c12_oh","sup":"0.23","inf":"0.01"},
{"variable":"c14_2","sup":"0.24","inf":"0.01"},
{"variable":"c14_1","sup":"0.5","inf":"0.01"},
{"variable":"miristoil","sup":"0.68","inf":"0.01"},
{"variable":"c14_oh","sup":"0.24","inf":"0.01"},
{"variable":"c16_1","sup":"0.5","inf":"0.01"},
{"variable":"palmitoil","sup":"5.71","inf":"0.52"},
{"variable":"c16_1_oh","sup":"0.24","inf":"0.01"},
{"variable":"c16_oh","sup":"0.13","inf":"0"},
{"variable":"c16_dc","sup":"0.23","inf":"0.01"},
{"variable":"c18_2","sup":"0.71","inf":"0.01"},
{"variable":"c18_1","sup":"2.1","inf":"0.38"},
{"variable":"estearoil","sup":"1.81","inf":"0.24"},
{"variable":"c18_2_oh","sup":"0.92","inf":"0"},
{"variable":"c18_1_oh","sup":"0.19","inf":"0.01"},
{"variable":"c18_oh","sup":"0.2","inf":"0.01"},
{"variable":"c3_c2","sup":"0.13","inf":"0.01"},
{"variable":"c3_c16","sup":"1.93","inf":"0.1"},
{"variable":"c4_c2","sup":"0.04","inf":"0.01"},
{"variable":"c4_c3","sup":"0.84","inf":"0.1"},
{"variable":"c4_c8","sup":"5.4","inf":"0.7"},
{"variable":"c5_c0","sup":"0.02","inf":"0"},
{"variable":"c5_c2","sup":"0.03","inf":"0"},
{"variable":"c5_c3","sup":"0.62","inf":"0.08"},
{"variable":"c5oh_c8","sup":"3.8","inf":"0.4"},
{"variable":"c5oh_c0","sup":"0.02","inf":"0"},
{"variable":"c8_c2","sup":"0.02","inf":"0"},
{"variable":"c8_c10","sup":"2.3","inf":"0.4"},
{"variable":"c3dc_c10","sup":"2.7","inf":"0.3"},
{"variable":"glut_c5oh","sup":"1.2","inf":"0.1"},
{"variable":"glut_c8","sup":"1.5","inf":"0.2"},
{"variable":"glut_c16","sup":"0.19","inf":"0.01"},
{"variable":"c14_1_c16","sup":"0.29","inf":"0.01"},
{"variable":"c16oh_c16","sup":"0.16","inf":"0.01"},
{"variable":"c10_2_c10","sup":"1.7","inf":"0.2"},
{"variable":"acs_cit","sup":"8.6","inf":"1.4"},
{"variable":"c0__c16_c18_","sup":"29.6","inf":"4.8"},
{"variable":"c16_c18_1__c2","sup":"0.38","inf":"0.07"},
{"variable":"d9_c1","sup":"ND","inf":"2500"},
{"variable":"d_c3","sup":"ND","inf":"800"},
{"variable":"d_c4","sup":"ND","inf":"800"},
{"variable":"d3_c8","sup":"ND","inf":"1000"},
{"variable":"d9_c14","sup":"ND","inf":"1500"},
{"variable":"d3_c16","sup":"ND","inf":"3500"},
{"variable":"glicina","sup":"524","inf":"145"},
{"variable":"alanina","sup":"321","inf":"96"},
{"variable":"valina","sup":"209","inf":"69"},
{"variable":"xleucina","sup":"454","inf":"68"},
{"variable":"metionina","sup":"69","inf":"11"},
{"variable":"his_mrm","sup":"3.2","inf":"0.06"},
{"variable":"citrulina","sup":"28.3","inf":"8.3"},
{"variable":"fenilalanina","sup":"120","inf":"20"},
{"variable":"tirosina","sup":"195","inf":"45"},
{"variable":"aspartato","sup":"204","inf":"22"},
{"variable":"glutamato","sup":"849","inf":"65"},
{"variable":"ornitina","sup":"231","inf":"49"},
{"variable":"arginina","sup":"52","inf":"6.8"},
{"variable":"asa","sup":"0.96","inf":"0.05"},
{"variable":"prolina","sup":"634","inf":"88"},
{"variable":"ohpro","sup":"22.2","inf":"3.7"},
{"variable":"treo_mrm","sup":"2.6","inf":"0.7"},
{"variable":"ser_mrm","sup":"7.3","inf":"1.6"},
{"variable":"succinil_ac","sup":"2.2","inf":"0.01"},
{"variable":"figlu","sup":"1.5","inf":"0.1"},
{"variable":"val_fen","sup":"6","inf":"1.5"},
{"variable":"xleu_fen","sup":"15.5","inf":"1.5"},
{"variable":"xleu_ala","sup":"3.3","inf":"0.3"},
{"variable":"met_fen","sup":"1.8","inf":"0.3"},
{"variable":"cit_arg","sup":"2.4","inf":"0.3"},
{"variable":"fen_tyr","sup":"1.8","inf":"0.1"},
{"variable":"asa_arg","sup":"7.7","inf":"0.7"},
{"variable":"tyr_cit","sup":"14.5","inf":"2.4"},
{"variable":"c3_met","sup":"0.11","inf":"0.01"},
{"variable":"x_v_p_t","sup":"6.5","inf":"1"},
{"variable":"d2_glic","sup":"ND","inf":"15000"},
{"variable":"d8_val","sup":"ND","inf":"1000"},
{"variable":"d3_xleu","sup":"ND","inf":"3000"},
{"variable":"dxleu_mrm","sup":"ND","inf":"12000"},
{"variable":"d3_met","sup":"ND","inf":"800"},
{"variable":"d5_fen","sup":"ND","inf":"5000"},
{"variable":"d6_tir","sup":"ND","inf":"1500"},
{"variable":"d2_orn","sup":"ND","inf":"700"},
{"variable":"d4c_arg","sup":"ND","inf":"2000"},
{"variable":"d2_cit","sup":"ND","inf":"0"},
{"variable":"sca_is","sup":"ND","inf":"0"},
{"variable":"Pro_Cit","sup":"38.202 ","inf":"4.839"},                     
{"variable":"Arg_Ala","sup":"0.292","inf":"0.031"},                      
{"variable":"Cit_Fel","sup":"0.744","inf":"0.186"},                      
{"variable":"Arg_Orn","sup":"0.482","inf":"0.051"},                      
{"variable":"Arg_Fel","sup":"1.407","inf":"0.125"},                       
{"variable":"Met_Xle","sup":"0.769","inf":"0.027"},                      
{"variable":"Met_Tyr","sup":"1.119","inf":"0.089"},                      
{"variable":"Met_Cit","sup":"6.931","inf":"0.668"},                      
{"variable":"Glu_Cit","sup":"64.130","inf":"4.455"},                      
{"variable":"Orn_Cit","sup":"16.861","inf":"3.135"},                      
{"variable":"Ala_Cit","sup":"26.417","inf":"5.938"},                      
{"variable":"Xle_Tyr","sup":"7.044","inf":"0.000"},                      
{"variable":"Suc_Fel","sup":"0.065","inf":"0.010"},                      
{"variable":"Suc_Met","sup":"0.099","inf":"0.009"},                      
{"variable":"Suc_Tyr","sup":"0.037","inf":"0.004"},                      
{"variable":"Glut_Oct","sup":"2.000","inf":"0.248"},                       
{"variable":"Glut_Pal","sup":"0.179","inf":"0.010"},                       
{"variable":"C14_Ace","sup":"0.031","inf":"0.003"},                      
{"variable":"Glut_Mal","sup":"2.021","inf":"0.220"},                       
{"variable":"Glut_T30h","sup":"1.262","inf":"0.143"},                      
{"variable":"Metil_Glut","sup":"13.536","inf":"0.987"},                      
{"variable":"C18_2_Est","sup":"0.300","inf":"0.021"},                      
{"variable":"Metil_Ace","sup":"0.04","inf":"0.01"},                       
{"variable":"Glut_Car","sup":"0.010","inf":"0.001"}]

#### extraer segun el lote y tipo de datos
def consulta(LISTA,LOTE,TIPO_DATO):
    MATRIZ_DE_DATOS=[]
    for i in LISTA:
        if i['lote']==LOTE and i['type_dat']==TIPO_DATO:
           MATRIZ_DE_DATOS.append(i)

    return MATRIZ_DE_DATOS

def columnas (subset,NOMBRE_COLUMNA,LOTE,TIPO_DATO):
    TEMP=consulta(NEONATOS,LOTE,TIPO_DATO)
    COL_VAR=seleccionar_variable(TEMP,NOMBRE_COLUMNA)
    return COL_VAR

    
##retorna un vector numerico con la variable seleccionada 
def seleccionar_variable(ARREGLO_DE_DATOS,VARIABLE):
    COLUMNA=[]
    for i in ARREGLO_DE_DATOS:
        try:
            COLUMNA.append(float(i[VARIABLE]))
        except:
            if i[VARIABLE]=="":
                COLUMNA.append(0)
                print "VARIALBE NO NUMERICA OO ",i[VARIABLE]
            else:    
                COLUMNA.append(i[VARIABLE])
                print "VARIALBE NO NUMERICA ",i[VARIABLE]
    return COLUMNA

def percentil(LISTA_NUMERICA,PERCENT):
    A = np.array(LISTA_NUMERICA)       
    P = np.percentile(A, PERCENT)
    return P
        


## DIVIDIR ELEMENTOS DE DOS VECTORES
def dividir_elementos(L1,L2):
    RES=[]
    TMP=0
    if len(L1)==len(L2):
        for s in L1:
            try:
                DIVIDIR=float(s)/float(L2[TMP])
                RES.append(DIVIDIR)
            except:
                print "No se puede dividir",s
                RES.append(0)
            TMP=TMP+1 
    else:
        print "longitudes diferentes"
    return RES

def sum_lista(Lista):
    TMP=0
    for i in Lista:
        TMP=TMP+i
    return TMP

def pintar_celdas(HOJA, LISTA_GRUPOS, FILA_INICIAL):
    col = easyxf('pattern: pattern solid, fore_colour green')
    
    for i in LISTA_GRUPOS: ##range(FILA_INICIAL,suma):
        for j in range(i):
           HOJA.col(FILA_INICIAL+j).set_style(col)
           
        FILA_INICIAL=FILA_INICIAL+i 

        
################# CREAR HOJAS DE EXCEL ######################


########ESTILOS DE CELDA############
        
Esti_Rojo=' font: colour red ; align: vertical center, horizontal center;'
Estilo_Rojo=Style.easyxf(Esti_Rojo)
Esti_Azul=' font: colour blue ; align: vertical center, horizontal center;'
Estilo_Azul=Style.easyxf(Esti_Azul)

Sti1_hoja1='pattern: pattern solid, fore_colour 0x2a; align: vertical center, horizontal center;'
Estilo1_hoja1=Style.easyxf(Sti1_hoja1)
    
Sti2_hoja1='pattern: pattern solid, fore_colour 0x1a; align: vertical center, horizontal center;'
Estilo2_hoja1=Style.easyxf(Sti2_hoja1)

Sti1_2='pattern: pattern solid, fore_colour white; align: vertical center, horizontal center;'
Sti1='pattern: pattern solid, fore_colour 0x1A; align: vertical center, horizontal center;'

Sti11_div1='pattern: pattern solid, fore_colour 0x1A; align: vertical center, horizontal center; '##borders: bottom dashed'
Sti11_div2='pattern: pattern solid, fore_colour white; align: vertical center, horizontal center;'
Estilo_COLUMNA_P=Style.easyxf(Sti1_2)
Estilo_titulos=xlwt.easyxf('borders: top double, bottom double, left double, right double; font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz center;')
Estilo_ETIQUETA=xlwt.easyxf('borders: top double, bottom double, left double, right double; font: height 160, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz center;')
#Estilo_COLUMNA_P=Style.easyxf(Sti1_2)
Estilo_COLUMNA_P=xlwt.easyxf('borders: top double, bottom double, left double, right double; font: height 160, name Arial, colour_index black, bold off, italic off; align: wrap on, vert centre, horiz center;')

#Estilo_Percentil==xlwt.easyxf('borders: top double, bottom double, left , right double; font: height 200, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz center;')

##CREAR y LLENAR LA PRIMERA HOJA
def crear_hoja1(HOJA,ALTURA,VALORES):
    TMP=0;
    for i in VALORES:
        colocar_variable_columna_hoja1(HOJA,i,ALTURA,TMP)
        TMP=TMP+1
def imprimir_percentiles(hoja1,VARIABLE,FILA,COLUMNA,LISTA_PERCENTILES):
        for i in LISTA_PERCENTILES:
            
            if i["variable"]==VARIABLE:
                    Fila=hoja1.row(FILA)
                    Fila.write(COLUMNA,i['sup'],Estilo_COLUMNA_P)
                    Fila=hoja1.row(FILA+1)
                    Fila.write(COLUMNA,i['inf'],Estilo_COLUMNA_P)
                    
                    
def extraer_percentiles(VARIABLE,LISTA_PERCENTILES):
    COLUMNA=[]
    for i in LISTA_PERCENTILES:
            if i["variable"]==VARIABLE:
                COLUMNA.append(float(i['sup']))
                COLUMNA.append(float(i['inf']))
    return COLUMNA
    
def colocar_variable_columna_hoja1(hoja1, VARIABLE,FILA_INICIO,COLUMNA):
    
    
    num=FILA_INICIO
     
    Fila=hoja1.row(num)
    Fila=hoja1.row(num+1)
     
    Fila.write(COLUMNA,VARIABLE,Estilo2_hoja1)
    Fila=hoja1.col(COLUMNA).width=4500
    TEMP=consulta(NEONATOS,LOTE_DE_DATOS,TIPO_DE_DATOS)
    COL_VAR=seleccionar_variable(TEMP,VARIABLE)
    for i in COL_VAR:
        Fila=hoja1.row(num+2)
        Fila.write(COLUMNA,i,Estilo1_hoja1)
        
        num=num+1

def colocar_variable_columna(hoja1, VARIABLE,FILA_INICIO,COLUMNA,ESTILO,ETIQUETA):
    Ancho_celda=3000
    if ESTILO == 1:
            
            Estilo_COLUMNA=Style.easyxf(Sti1)
##            Estilo_PRECENTILES=Style.easyxf(Sti1)
            Estilo_NOMBRES=Style.easyxf(Sti1)
    else:
            
            Estilo_COLUMNA=Style.easyxf(Sti1_2)
##            Estilo_PRECENTILES=Style.easyxf(Sti1_2)
            Estilo_NOMBRES=Style.easyxf(Sti1_2)
    
    num=FILA_INICIO
    TEMP=consulta(NEONATOS,LOTE_DE_DATOS,TIPO_DE_DATOS)
    COL_VAR=seleccionar_variable(TEMP,VARIABLE)
    try:
        per_may=percentil(COL_VAR,Percentil_mayor)
        per_men=percentil(COL_VAR,Percentil_menor)
        Fila=hoja1.row(num-2)## escribir el valor max
        Fila.write(COLUMNA,per_may,Estilo_COLUMNA_P)##,Estilo_NOMBRES)
        Fila=hoja1.row(num-1)## escribir el valor min
        Fila.write(COLUMNA,per_men,Estilo_COLUMNA_P)#Estilo_PRECENTILES)
        
        imprimir_percentiles(hoja1,VARIABLE,FILA_INICIO,COLUMNA,PERCENTILES_CHEMOVIEW)
        L_TMP=extraer_percentiles(VARIABLE,PERCENTILES_CHEMOVIEW)

        
        Fila=hoja1.row(num-3) ##Escribir nombre de varialbe
        Fila.write(COLUMNA,ETIQUETA,Estilo_ETIQUETA)#,Estilo_NOMBRES)
        Fila=hoja1.col(COLUMNA).width=Ancho_celda
        for i in COL_VAR:
            Fila=hoja1.row(num+2)
            if i>= L_TMP[0]:##per_may:
                Fila.write(COLUMNA,i,Estilo_Rojo)
            elif i <= L_TMP[1]:##per_men:
                Fila.write(COLUMNA,i,Estilo_Azul)
            else:
                Fila.write(COLUMNA,i,Estilo_COLUMNA)
                
            num=num+1
        
    except:
            Fila=hoja1.row(num-2)
            Fila.write(COLUMNA,"P 99 Lote:",Estilo_COLUMNA_P)
            Fila=hoja1.row(num-1)
            Fila.write(COLUMNA,"P 1 Lote:",Estilo_COLUMNA_P)
            Fila=hoja1.row(num)
            Fila.write(COLUMNA,"P 99 CHW:",Estilo_COLUMNA_P)
            Fila=hoja1.row(num+1)
            Fila.write(COLUMNA,"P 1 CHW:",Estilo_COLUMNA_P)
            Fila=hoja1.col(COLUMNA).width=Ancho_celda
            for i in COL_VAR:
                Fila=hoja1.row(num+2)
                Fila.write(COLUMNA,i,Estilo_COLUMNA)
                num=num+1

##colocar_variable de division A/B
def colocar_variable_columna_div(hoja,RESULT_LIST,FILA_INICIO,COLUMNA,NOMBRE_COLUMNA,ESTILO,VARIABLE):
    Ancho_celda=3000
    if ESTILO == 1:
            Estilo_COLUMNA=Style.easyxf(Sti11_div1)
            Estilo_PRECENTILES=Style.easyxf(Sti11_div1)
            Estilo_NOMBRES=Style.easyxf(Sti11_div1)
    else:
            Estilo_COLUMNA=Style.easyxf(Sti11_div2)
            Estilo_PRECENTILES=Style.easyxf(Sti11_div2)
            Estilo_NOMBRES=Style.easyxf(Sti11_div2)
    
    num=FILA_INICIO
    Fila=hoja.row(num-3)
    
    per_may=percentil(RESULT_LIST,Percentil_mayor)
    per_men=percentil(RESULT_LIST,Percentil_menor)
    Fila.write(COLUMNA,VARIABLE,Estilo_ETIQUETA)#,Estilo_NOMBRES)
    Fila=hoja.row(num-2)
    Fila.write(COLUMNA,per_may,Estilo_COLUMNA_P)#,Estilo_PRECENTILES)
    Fila=hoja.row(num-1)
    Fila.write(COLUMNA,per_men,Estilo_COLUMNA_P)#,Estilo_PRECENTILES)
    Fila=hoja.row(num)

    imprimir_percentiles(hoja,NOMBRE_COLUMNA,FILA_INICIO,COLUMNA,PERCENTILES_CHEMOVIEW)
    L_TMP=extraer_percentiles(NOMBRE_COLUMNA,PERCENTILES_CHEMOVIEW)

    
    for i in RESULT_LIST:
        Fila=hoja.row(num+2)
        
        if i>= L_TMP[0]:#per_may:
            Fila.write(COLUMNA,i,Estilo_Rojo)
        elif i <= L_TMP[1]:#per_men:
            Fila.write(COLUMNA,i,Estilo_Azul)
        else:
            Fila.write(COLUMNA,i,Estilo_COLUMNA)
        num=num+1

def colocar_titulos(hoja,FILA,COLUMNA_INICIAL,TAM,LABEL):
   
        TEMP=TAM-1
        
        if TAM ==1:
##            hoja.write(COLUMNA_INICIAL,FILA, LABEL, header_style )
            hoja.write_merge(FILA,FILA+1,COLUMNA_INICIAL,COLUMNA_INICIAL,LABEL,Estilo_titulos)#,header_style )
            
        else:
            
            hoja.write_merge(FILA,FILA+1,COLUMNA_INICIAL,COLUMNA_INICIAL+TEMP,LABEL,Estilo_titulos)#,header_style )
       
        
######EJECUCION########################
        
##Abrir libro     
libro = xlwt.Workbook()

## Crear Hoja inicial
hoja1 = libro.add_sheet("Chemview")

crear_hoja1(hoja1,3,VARIABLES)
## Crear Segunda Hoja
hoja2 = libro.add_sheet("AA")
## Crear tercera hoja AC
hoja3 = libro.add_sheet("AC")
##pintar_celdas(hoja2, [1,2,3,4,5,6],1)
## Crear tercera hoja BOX
hoja4 = libro.add_sheet("BOX")
#########AGREGAR VARIABLES HOJA 2#############



Cit=columnas(NEONATOS,'citrulina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Pro=columnas(NEONATOS,'prolina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Arg=columnas(NEONATOS,'arginina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Ala=columnas(NEONATOS,'alanina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Fel=columnas(NEONATOS,'fenilalanina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Orn=columnas(NEONATOS,'ornitina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Tyr=columnas(NEONATOS,'tirosina',LOTE_DE_DATOS,TIPO_DE_DATOS) 
Glu=columnas(NEONATOS,'glutamato',LOTE_DE_DATOS,TIPO_DE_DATOS)
Met=columnas(NEONATOS,'metionina',LOTE_DE_DATOS,TIPO_DE_DATOS) 
Xle=columnas(NEONATOS,'xleucina',LOTE_DE_DATOS,TIPO_DE_DATOS) 
Orn=columnas(NEONATOS,'ornitina',LOTE_DE_DATOS,TIPO_DE_DATOS)
Suc=columnas(NEONATOS,'succinil_ac',LOTE_DE_DATOS,TIPO_DE_DATOS)
Glut=columnas(NEONATOS,'glutaril',LOTE_DE_DATOS,TIPO_DE_DATOS)
Oct=columnas(NEONATOS,'octanoil',LOTE_DE_DATOS,TIPO_DE_DATOS)
Pal=columnas(NEONATOS,'palmitoil',LOTE_DE_DATOS,TIPO_DE_DATOS)
Mal=columnas(NEONATOS,'malonil',LOTE_DE_DATOS,TIPO_DE_DATOS)
T30h=columnas(NEONATOS,'t3oh_isovaleril',LOTE_DE_DATOS,TIPO_DE_DATOS)
Car=columnas(NEONATOS,'cartina_libre',LOTE_DE_DATOS,TIPO_DE_DATOS)
Metil=columnas(NEONATOS,'metilmalonil',LOTE_DE_DATOS,TIPO_DE_DATOS)
Ace=columnas(NEONATOS,'acetil_carnitina',LOTE_DE_DATOS,TIPO_DE_DATOS)
C14=columnas(NEONATOS,'c14_1',LOTE_DE_DATOS,TIPO_DE_DATOS)
C18_2=columnas(NEONATOS,'c18_oh',LOTE_DE_DATOS,TIPO_DE_DATOS)
Est=columnas(NEONATOS,'estearoil',LOTE_DE_DATOS,TIPO_DE_DATOS)



Pro_Cit=dividir_elementos(Pro,Cit)
Met_Cit=dividir_elementos(Met,Cit)
Arg_Ala=dividir_elementos(Arg,Ala)
Cit_Fel=dividir_elementos(Cit,Fel)
Arg_Orn=dividir_elementos(Cit,Orn)
Met_Tyr=dividir_elementos(Met,Tyr)
Arg_Fel=dividir_elementos(Arg,Fel)
Glu_Cit=dividir_elementos(Glu,Cit)
Ala_Cit=dividir_elementos(Ala,Cit)
Met_Xle=dividir_elementos(Met,Xle)
Orn_Cit=dividir_elementos(Orn,Cit)
Xle_Tyr=dividir_elementos(Xle,Tyr)
Suc_Met=dividir_elementos(Suc,Met)
Suc_Fel=dividir_elementos(Suc,Fel)
Suc_Tyr=dividir_elementos(Suc,Tyr)
Glut_Oct=dividir_elementos(Glut,Oct)
Glut_Pal=dividir_elementos(Glut,Pal)
Glut_Mal=dividir_elementos(Glut,Mal)
Glut_T30h=dividir_elementos(Glut,T30h)
Glut_Car=dividir_elementos(Glut,Car)
Metil_Glut=dividir_elementos(Metil,Glut)
Metil_Ace=dividir_elementos(Metil,Ace)
C14_Ace=dividir_elementos(C14,Ace)
C18_2_Est=dividir_elementos(C18_2,Est)

###################TPN##################3


colocar_variable_columna(hoja2, 'codigo_de_muestra',FILA,1,2,"CODIGO")

colocar_titulos(hoja2,FILA-5,2,7,'TPN')

colocar_variable_columna(hoja2, 'prolina',FILA,2,1,"Prolina")

colocar_variable_columna(hoja2, 'treo_mrm',FILA,3,1,"Treo MRM")
colocar_variable_columna(hoja2, 'metionina',FILA,4,1,"Metionina")
colocar_variable_columna(hoja2, 'valina',FILA,5,1,"Valina")
colocar_variable_columna(hoja2, 'xleucina',FILA,6,1,"Xleucina")
colocar_variable_columna(hoja2, 'fenilalanina',FILA,7,1,"Fenilalanina")
colocar_variable_columna_div(hoja2,Pro_Cit,FILA,8,'Pro_Cit',1,'PRO/CIT')


#################H_PRO#######################
colocar_titulos(hoja2,FILA-5,9,2,'H-PRO')

colocar_variable_columna(hoja2, 'prolina',FILA,9,2,"Prolina")
colocar_variable_columna_div(hoja2,Pro_Cit,FILA,10,'Pro_Cit',2,'PRO/CIT')


#######################NKHG######################
colocar_titulos(hoja2,FILA-5,11,1,'NKHG')

colocar_variable_columna(hoja2,'glicina',FILA,11,1,"Glicina")

################3PGDH##############
colocar_titulos(hoja2,FILA-5,12,7,'3PGDH')

colocar_variable_columna(hoja2, 'prolina',FILA,12,2,"Prolina")
colocar_variable_columna_div(hoja2,Pro_Cit,FILA,13,'Pro_Cit',2,'PRO/CIT')
colocar_variable_columna(hoja2,'ornitina',FILA,14,2,"Ornitina")
colocar_variable_columna(hoja2,'ser_mrm',FILA,15,2,"Ser MRM")
colocar_variable_columna(hoja2,'glicina',FILA,16,2,"Glicina")
colocar_variable_columna(hoja2,'glutamato',FILA,17,2,"Glutamato")
colocar_variable_columna_div(hoja2,Arg_Ala,FILA,18,'Arg_Ala',2,'Arg/Ala')

##############OAT##############################
colocar_titulos(hoja2,FILA-5,19,4,'OAT')


colocar_variable_columna(hoja2, 'prolina',FILA,19,1,"Prolina")
colocar_variable_columna_div(hoja2,Pro_Cit,FILA,20,'Pro_Cit',1,'Pro/Cit')
colocar_variable_columna(hoja2,'citrulina',FILA,21,1,"Citrulina")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,22,'Cit_Fel',1,'Cit/Phe')

###########ARGINEMIA##################################
colocar_titulos(hoja2,FILA-5,23,6,'ARGININEMIA')


colocar_variable_columna(hoja2,'arginina',FILA,23,2,"Arginina")
colocar_variable_columna_div(hoja2,Arg_Orn,FILA,24,'Arg_Orn',2,'Arg/Orn')
colocar_variable_columna_div(hoja2,Arg_Ala,FILA,25,'Arg_Ala',2,'Arg/Ala')
colocar_variable_columna_div(hoja2,Arg_Fel,FILA,26,'Arg_Fel',2,'Arg/Phe')
colocar_variable_columna(hoja2,'cit_arg',FILA,27,2,"Cit/Arg")
colocar_variable_columna(hoja2,'asa_arg',FILA,28,2,"Asa/Arg")

###########HCY/HMET(mat)##################################
colocar_titulos(hoja2,FILA-5,29,5,'HCY/HMET(mat)')



colocar_variable_columna(hoja2, 'metionina',FILA,29,1,"Metionina")
colocar_variable_columna(hoja2,'met_fen',FILA,30,1,"Met/Phe")
colocar_variable_columna_div(hoja2,Met_Xle,FILA,31,'Met_Xle',1,'Met/Xle')
colocar_variable_columna_div(hoja2,Met_Tyr,FILA,32,'Met_Tyr',1,'Met/Tyr')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,33,'Met_Cit',1,'Met/Cit')

###########MET##################################
colocar_titulos(hoja2,FILA-5,34,5,'MET')

colocar_variable_columna(hoja2, 'metionina',FILA,34,2,"Metionina")
colocar_variable_columna(hoja2,'met_fen',FILA,35,2,"Met/Phe")
colocar_variable_columna_div(hoja2,Met_Xle,FILA,36,'Met_Xle',2,'Met/Xle')
colocar_variable_columna_div(hoja2,Met_Tyr,FILA,37,'Met_Tyr',2,'Met/Tyr')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,38,'Met_Cit',2,'Met/Cit')

###########RMD##################################
colocar_titulos(hoja2,FILA-5,39,5,'RMD')


colocar_variable_columna(hoja2, 'metionina',FILA,39,1,"Metionina")
colocar_variable_columna(hoja2,'met_fen',FILA,40,1,"Met/Phe")
colocar_variable_columna_div(hoja2,Met_Tyr,FILA,41,'Met_Xle',1,'Met/Tyr')
colocar_variable_columna_div(hoja2,Met_Xle,FILA,42,'Met_Tyr',1,'Met/Xle')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,43,'Met_Cit',1,'Met/Cit')


###########Cit I##################################
colocar_titulos(hoja2,FILA-5,44,8,'Cit I')


colocar_variable_columna(hoja2,'citrulina',FILA,44,2,"Citrulina")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,45,'Cit_Fel',2,'Cit/Phe')
colocar_variable_columna(hoja2,'cit_arg',FILA,46,2,"Cit/Arg")
colocar_variable_columna_div(hoja2,Glu_Cit,FILA,47,'Glu_Cit',2,'Glu/Cit')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,48,'Met_Cit',2,'Met/Cit')
colocar_variable_columna_div(hoja2,Orn_Cit,FILA,49,'Orn_Cit',2,'Orn/Cit')
colocar_variable_columna_div(hoja2,Ala_Cit,FILA,50,'Ala_Cit',2,'Ala/Cit')
colocar_variable_columna_div(hoja2,Pro_Cit,FILA,51,'Pro_Cit',2,'Pro/Cit')

###########Cit II##################################
colocar_titulos(hoja2,FILA-5,52,7,'Cit II')

colocar_variable_columna(hoja2,'citrulina',FILA,52,1,"Citrulina")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,53,'Cit_Fel',1,'Cit/Phe')
colocar_variable_columna_div(hoja2,Ala_Cit,FILA,54,'Ala_Cit',1,'Ala/Cit')
colocar_variable_columna(hoja2,'cit_arg',FILA,55,1,"Cit/Arg")
colocar_variable_columna_div(hoja2,Glu_Cit,FILA,56,'Glu_Cit',1,'Glu/Cit')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,57,'Met_Cit',1,'Met/Cit')
colocar_variable_columna_div(hoja2,Orn_Cit,FILA,58,'Orn_Cit',1,'Orn/Cit')


###########ASA##################################
colocar_titulos(hoja2,FILA-5,59,9,'ASA')


colocar_variable_columna(hoja2,'citrulina',FILA,59,2,"Citrulina")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,60,'Cit_Fel',2,'Cit/Phe')
colocar_variable_columna_div(hoja2,Glu_Cit,FILA,61,'Glu_Cit',2,'Glu/Cit')
colocar_variable_columna_div(hoja2,Ala_Cit,FILA,62,'Ala_Cit',2,'Ala/Cit')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,63,'Met_Cit',2,'Met/Cit')
colocar_variable_columna(hoja2,'cit_arg',FILA,64,2,"Cit/Arg")
colocar_variable_columna(hoja2,'asa',FILA,65,2,"ASA")
colocar_variable_columna(hoja2,'asa_arg',FILA,66,2,"Asa/Arg")
colocar_variable_columna_div(hoja2,Orn_Cit,FILA,67,'Orn_Cit',2,'Orn/Cit')


###########PC##################################
colocar_titulos(hoja2,FILA-5,68,14,'PC')


colocar_variable_columna(hoja2,'citrulina',FILA,68,1,"Citrulina")
colocar_variable_columna(hoja2,'cit_arg',FILA,69,1,"Cit/Arg")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,70,'Cit_Fel',1,'Cit/Phe')
colocar_variable_columna_div(hoja2,Glu_Cit,FILA,71,'Glu_Cit',1,'Glu/Cit')
colocar_variable_columna_div(hoja2,Orn_Cit,FILA,72,'Orn_Cit',1,'Orn/Cit')
colocar_variable_columna_div(hoja2,Ala_Cit,FILA,73,'Ala_Cit',1,'Ala/Cit')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,74,'Met_Cit',1,'Met/Cit')
colocar_variable_columna(hoja2,'glutamato',FILA,75,1,"Glutamato")
colocar_variable_columna(hoja2,'val_fen',FILA,76,1,"Val/Phe")
colocar_variable_columna(hoja2,'tirosina',FILA,77,1,"Tirosina")
colocar_variable_columna(hoja2, 'fenilalanina',FILA,78,1,"Fenilalanina")
colocar_variable_columna(hoja2,'glicina',FILA,79,1,"Glicina")
colocar_variable_columna_div(hoja2,Met_Tyr,FILA,80,'Met_Tyr',1,'Met/Tyr')
colocar_variable_columna_div(hoja2,Xle_Tyr,FILA,81,'Xle_Tyr',1,'Xle/Tyr')

###########OTC/CPS##################################
colocar_titulos(hoja2,FILA-5,82,8,'OTC/CPS')



colocar_variable_columna(hoja2,'citrulina',FILA,82,2,"Citrulina")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,83,'Cit_Fel',2,'Cit/Phe')
colocar_variable_columna_div(hoja2,Met_Cit,FILA,84,'Met_Cit',2,'Met/Cit')
colocar_variable_columna_div(hoja2,Glu_Cit,FILA,85,'Glu_Cit',2,'Glu/Cit')
colocar_variable_columna_div(hoja2,Ala_Cit,FILA,86,'Ala_Cit',2,'Ala/Cit')
colocar_variable_columna_div(hoja2,Orn_Cit,FILA,87,'Orn_Cit',2,'Orn/Cit')
colocar_variable_columna_div(hoja2,Pro_Cit,FILA,88,'Pro_Cit',2,'Pro/Cit')
colocar_variable_columna(hoja2,'cit_arg',FILA,89,2,"Cit/Arg")


###########HIDROXIPRO##################################
colocar_titulos(hoja2,FILA-5,90,2,'HIDROXIPRO')


colocar_variable_columna(hoja2,'ohpro',FILA,90,1,"OHPro")
colocar_variable_columna(hoja2, 'xleucina',FILA,91,1,"Xleucina")

###########MSUD##################################
colocar_titulos(hoja2,FILA-5,92,8,'MSUD')


colocar_variable_columna(hoja2, 'xleucina',FILA,92,2,"Xleucina")
colocar_variable_columna(hoja2, 'valina',FILA,93,2,"Valina")
colocar_variable_columna(hoja2,'x_v_p_t',FILA,94,2,"(X+V)/(P+T)")
colocar_variable_columna(hoja2,'xleu_ala',FILA,95,2,"Xle/Ala")
colocar_variable_columna(hoja2,'xleu_fen',FILA,96,2,"Xle/Phe")
colocar_variable_columna_div(hoja2,Xle_Tyr,FILA,97,'Xle_Tyr',2,'Xle/Tyr')
colocar_variable_columna(hoja2,'val_fen',FILA,98,2,"Val/Phe")
colocar_variable_columna_div(hoja2,Met_Xle,FILA,99,'Met_Xle',2,'Met/Xle')


###########BCKDK##################################
colocar_titulos(hoja2,FILA-5,100,7,'BCKDK')



colocar_variable_columna_div(hoja2,Met_Xle,FILA,100,'Met_Xle',1,'Met/Xle')
colocar_variable_columna(hoja2,'xleu_ala',FILA,101,1,"Xle/Ala")
colocar_variable_columna(hoja2,'xleu_fen',FILA,102,1,"Xle/Phe")
colocar_variable_columna(hoja2, 'xleucina',FILA,103,1,"Xleucina")
colocar_variable_columna(hoja2,'x_v_p_t',FILA,104,1,"(X+V)/(P+T)")
colocar_variable_columna(hoja2,'alanina',FILA,105,1,"Alanina")
colocar_variable_columna_div(hoja2,Xle_Tyr,FILA,106,'Xle_Tyr',1,'Xle/Tyr')


###PKU
###########PKU##################################
colocar_titulos(hoja2,FILA-5,107,9,'PKU')


colocar_variable_columna(hoja2,'fenilalanina',FILA,107,2,"Fenilalanina")
colocar_variable_columna(hoja2,'fen_tyr',FILA,108,2,"Phe/Tyr")
colocar_variable_columna_div(hoja2,Suc_Fel,FILA,109,'Suc_Fel',2,'Suac/Phe')
colocar_variable_columna(hoja2,'met_fen',FILA,110,2,"Met/Phe")
colocar_variable_columna(hoja2,'val_fen',FILA,111,2,"Val/Phe")
colocar_variable_columna(hoja2,'xleu_fen',FILA,112,2,"Xle/Phe")
colocar_variable_columna_div(hoja2,Cit_Fel,FILA,113,'Cit_Fel',2,'Cit/Phe')
colocar_variable_columna(hoja2,'x_v_p_t',FILA,114,2,"(X+V)/(P+T)")
colocar_variable_columna_div(hoja2,Arg_Fel,FILA,115,'Arg_Fel',2,'Arg/Phe')



##TYRI
###########TYRI##################################
colocar_titulos(hoja2,FILA-5,116,4,'TYRI')

colocar_variable_columna(hoja2,'succinil_ac',FILA,116,1,"Succinil Ac")
colocar_variable_columna_div(hoja2,Suc_Met,FILA,117,'Suc_Met',1,'Suac/Met')
colocar_variable_columna_div(hoja2,Suc_Fel,FILA,118,'Suc_Fel',1,'Suac/Phe')
colocar_variable_columna(hoja2,'tirosina',FILA,119,1,"Tirosina")




###TYRI/TYR trans

##TYRI/TYR trans
###########TYRI/TYR trans##################################
colocar_titulos(hoja2,FILA-5,120,6,'TYRI/TYR trans')




colocar_variable_columna(hoja2,'tirosina',FILA,120,2,"Tirosina")
colocar_variable_columna_div(hoja2,Suc_Tyr,FILA,121,'Suc_Tyr',2,'Suac/Tyr')
colocar_variable_columna(hoja2,'fen_tyr',FILA,122,2,"Phe/Tyr")
colocar_variable_columna_div(hoja2,Xle_Tyr,FILA,123,'Xle_Tyr',2,'Xle/Tyr')
colocar_variable_columna(hoja2,'x_v_p_t',FILA,124,2,"(X+V)/(P+T)")
colocar_variable_columna_div(hoja2,Met_Tyr,FILA,125,'Met_Tyr',2,'Met/Tyr')


###TYR III
###########TYR III##################################
colocar_titulos(hoja2,FILA-5,126,8,'TYR III')

colocar_variable_columna(hoja2,'tirosina',FILA,126,1,"Tirosina")
colocar_variable_columna(hoja2,'asa',FILA,127,1,"ASA")
colocar_variable_columna(hoja2,'fen_tyr',FILA,128,1,"Phe/Tyr")
colocar_variable_columna_div(hoja2,Met_Tyr,FILA,129,'Met_Tyr',1,'Met/Tyr')
colocar_variable_columna_div(hoja2,Suc_Tyr,FILA,130,'Suc_Tyr',1,'Suac/Tyr')
colocar_variable_columna_div(hoja2,Xle_Tyr,FILA,131,'Xle_Tyr',1,'Xle/Tyr')
colocar_variable_columna(hoja2,'x_v_p_t',FILA,132,1,"(X+V)/(P+T)")
colocar_variable_columna_div(hoja2,Arg_Orn,FILA,133,'Arg_Orn',1,'Arg/Orn')


##########################>>>>>>>AC<<<<<<<<<<<<##################


CL=1
##################### Hojas #################################


####BIOT(C)#########

colocar_titulos(hoja3,FILA-5,2,2,'BIOT(C)')

colocar_variable_columna(hoja3, 'codigo_de_muestra',FILA,CL,2,"CODIGO")
colocar_variable_columna(hoja3, 'c18_2_oh',FILA,CL+1,1,"C18:2-OH")
colocar_variable_columna(hoja3,'fen_tyr',FILA,CL+2,1,"C14:1/C12:1")


##########3MCC3MGA-3MCC(mat)############

colocar_titulos(hoja3,FILA-5,4,4,'3MCC3MGA-3MCC(mat)')

colocar_variable_columna(hoja3, 't3oh_isovaleril',FILA,CL+3,2,"3OH-Isovaleril")
colocar_variable_columna(hoja3, 'c5oh_c8',FILA,CL+4,2,"C5OH/C8")
colocar_variable_columna(hoja3, 'c5oh_c0',FILA,CL+5,2,"C5OH/C0")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+6,2,"Glut/C5OH")


########2M3HBA###########

colocar_titulos(hoja3,FILA-5,8,5,'2M3HBA')

colocar_variable_columna(hoja3, 'tiglil',FILA,CL+7,1,"Tiglil")
colocar_variable_columna(hoja3, 't3oh_isovaleril',FILA,CL+8,1,"3OH-Isovaleril")
colocar_variable_columna(hoja3, 'c5oh_c8',FILA,CL+9,1,"C5OH/C8")
colocar_variable_columna(hoja3, 'c5oh_c0',FILA,CL+10,1,"C5OH/C0")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+11,1,"Glut/C5OH")


############BIOT(P)########################

colocar_titulos(hoja3,FILA-5,13,4,'BIOT(P)')

colocar_variable_columna(hoja3, 't3oh_isovaleril',FILA,CL+12,2,"3OH-Isovaleril")
colocar_variable_columna(hoja3, 'c5oh_c0',FILA,CL+13,2,"C5OH/C0")
colocar_variable_columna(hoja3, 'c5oh_c8',FILA,CL+14,2,"C5OH/C8")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+15,2,"Glut/C5OH")

######### HMG ##########################################

colocar_titulos(hoja3,FILA-5,17,5,'HMG')

colocar_variable_columna(hoja3, 't3oh_isovaleril',FILA,CL+16,1,"3OH-Isovaleril")
colocar_variable_columna(hoja3, 'c5oh_c0',FILA,CL+17,1,"C5OH/C0")
colocar_variable_columna(hoja3, 'c5oh_c8',FILA,CL+18,1,"C5OH/C8")
colocar_variable_columna(hoja3, 't3me_glutaril',FILA,CL+19,1,"3Me Glutaril")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+20,1,"Glut/C5OH")

################### MCD #####################################

colocar_titulos(hoja3,FILA-5,22,8,'MCD')

colocar_variable_columna(hoja3, 't3oh_isovaleril',FILA,CL+21,2,"3OH-Isovaleril")
colocar_variable_columna(hoja3, 'c5oh_c0',FILA,CL+22,2,"C5OH/C0")
colocar_variable_columna(hoja3, 'c5oh_c8',FILA,CL+23,2,"C5OH/C8")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+24,2,"Glut/C5OH")
colocar_variable_columna(hoja3, 'propionil',FILA,CL+25,2,"Propionil")
colocar_variable_columna(hoja3, 'c3_c16',FILA,CL+26,2,"C3/C16")
colocar_variable_columna(hoja3, 'c3_c2',FILA,CL+27,2,"C3/C2")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+28,2,"C4/C3")


################### BKT #####################################

colocar_titulos(hoja3,FILA-5,30,6,'BKT')

colocar_variable_columna(hoja3, 'tiglil',FILA,CL+29,1,"Tiglil")
colocar_variable_columna(hoja3, 't3oh_butiril',FILA,CL+30,1,"3OH-Butiril")
colocar_variable_columna(hoja3, 't3oh_isovaleril',FILA,CL+31,1,"3OH-Isovaleril")
colocar_variable_columna(hoja3, 'c5oh_c0',FILA,CL+32,1,"C5OH/C0")
colocar_variable_columna(hoja3, 'c5oh_c8',FILA,CL+33,1,"C5OH/C8")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+34,1,"Glut/C5OH")

################### Cbl C,D #####################################

colocar_titulos(hoja3,FILA-5,36,4,'Cbl C,D')

colocar_variable_columna(hoja3, 'c3_c2',FILA,CL+35,2,"C3/C2")
colocar_variable_columna(hoja3, 'propionil',FILA,CL+36,2,"Propionil")
colocar_variable_columna(hoja3, 'c3_c16',FILA,CL+37,2,"C3/C16")
colocar_variable_columna(hoja3, 'c3_met',FILA,CL+38,2,"C3/Met")

################### B12 Def(mat) #####################################

colocar_titulos(hoja3,FILA-5,40,5,'B12 Def(mat)')

colocar_variable_columna(hoja3, 'propionil',FILA,CL+39,1,"Propionil")
colocar_variable_columna(hoja3, 'c3_c16',FILA,CL+40,1,"C3/C16")
colocar_variable_columna(hoja3, 'c3_met',FILA,CL+41,1,"C3/Met")
colocar_variable_columna(hoja3, 'c3_c2',FILA,CL+42,1,"C3/C2")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+43,1,"C4/C3")


################### MUT-Cbl A,B #####################################

colocar_titulos(hoja3,FILA-5,45,6,'MUT-Cbl A,B')

colocar_variable_columna(hoja3, 'c3_c2',FILA,CL+44,2,"C3/C2")
colocar_variable_columna(hoja3, 'propionil',FILA,CL+45,2,"Propionil")
colocar_variable_columna(hoja3, 'c3_c16',FILA,CL+46,2,"C3/C16")
colocar_variable_columna(hoja3, 'c3_met',FILA,CL+47,2,"C3/Met")
colocar_variable_columna(hoja3, 'c16_1_oh',FILA,CL+48,2,"C16:1-OH")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+49,2,"C4/C3")

################### PROP #####################################

colocar_titulos(hoja3,FILA-5,51,8,'PROP')

colocar_variable_columna(hoja3, 'c3_c2',FILA,CL+50,1,"C3/C2")
colocar_variable_columna(hoja3, 'propionil',FILA,CL+51,1,"Propionil")
colocar_variable_columna(hoja3, 'c3_c16',FILA,CL+52,1,"C3/C16")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+53,1,"C4/C3")
colocar_variable_columna(hoja3, 'c5_c3',FILA,CL+54,1,"C5/C3")
colocar_variable_columna(hoja3, 'c3_met',FILA,CL+55,1,"C3/Met")
colocar_variable_columna(hoja3, 'c16_1_oh',FILA,CL+56,1,"C16:1-OH")
colocar_variable_columna(hoja3, 'c16_1_oh',FILA,CL+57,1,"Prolina")


################### 2MBG #####################################

colocar_titulos(hoja3,FILA-5,59,4,'2MBG')

colocar_variable_columna(hoja3, 'isovaleril',FILA,CL+58,2,"Isovaleril")
colocar_variable_columna(hoja3, 'c5_c0',FILA,CL+59,2,"C5/C0")
colocar_variable_columna(hoja3, 'c5_c2',FILA,CL+60,2,"C5/C2")
colocar_variable_columna(hoja3, 'c5_c3',FILA,CL+61,2,"C5/C3")

################### IVA #####################################

colocar_titulos(hoja3,FILA-5,63,4,'IVA')

colocar_variable_columna(hoja3, 'isovaleril',FILA,CL+62,1,"Isovaleril")
colocar_variable_columna(hoja3, 'c5_c0',FILA,CL+63,1,"C5/C0")
colocar_variable_columna(hoja3, 'c5_c2',FILA,CL+64,1,"C5/C2")
colocar_variable_columna(hoja3, 'c5_c3',FILA,CL+65,1,"C5/C3")

################### EE #####################################

colocar_titulos(hoja3,FILA-5,67,8,'EE')

colocar_variable_columna(hoja3, 'butiril',FILA,CL+66,2,"Butiril")
colocar_variable_columna(hoja3, 'c4_c2',FILA,CL+67,2,"C4/C2")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+68,2,"C4/C3")
colocar_variable_columna(hoja3, 'c4_c8',FILA,CL+69,2,"C4/C8")
colocar_variable_columna(hoja3, 'isovaleril',FILA,CL+70,2,"Isovaleril")
colocar_variable_columna(hoja3, 'c5_c0',FILA,CL+71,2,"C5/C0")
colocar_variable_columna(hoja3, 'c5_c2',FILA,CL+72,2,"C5/C2")
colocar_variable_columna(hoja3, 'c5_c3',FILA,CL+73,2,"C5/C3")


################### FIGLU #####################################

colocar_titulos(hoja3,FILA-5,75,5,'FIGLU')

colocar_variable_columna(hoja3, 'figlu',FILA,CL+74,1,"FIGLU")
colocar_variable_columna(hoja3, 'butiril',FILA,CL+75,1,"Butiril")
colocar_variable_columna(hoja3, 'c4_c2',FILA,CL+76,1,"C4/C2")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+77,1,"C4/C3")
colocar_variable_columna(hoja3, 'c4_c8',FILA,CL+78,1,"C4/C8")


################### IBG #####################################

colocar_titulos(hoja3,FILA-5,80,4,'IBG')

colocar_variable_columna(hoja3, 'butiril',FILA,CL+79,2,"Butiril")
colocar_variable_columna(hoja3, 'c4_c2',FILA,CL+80,2,"C4/C2")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+81,2,"C4/C3")
colocar_variable_columna(hoja3, 'c4_c8',FILA,CL+82,2,"C4/C8")


################### GA-I #####################################

colocar_titulos(hoja3,FILA-5,84,7,'GA-I')

colocar_variable_columna(hoja3, 'glutaril',FILA,CL+83,1,"Glutaril")
colocar_variable_columna_div(hoja3,Glut_Oct,FILA,CL+84,'Glut_Oct',1,'C5DC/C8')
colocar_variable_columna_div(hoja3,Glut_Pal,FILA,CL+85,'Glut_Pal',1,'C5DC/C16')
colocar_variable_columna_div(hoja3,Glut_Mal,FILA,CL+86,'Glut_Mal',1,'C5DC/C3DC')
colocar_variable_columna_div(hoja3,Glut_T30h,FILA,CL+87,'Glut_T30h',1,'C5DC/C5OH')
colocar_variable_columna_div(hoja3,Glut_Car,FILA,CL+88,'Glut_Car',1,'C5DC/C0')
colocar_variable_columna_div(hoja3,Metil_Glut ,FILA,CL+89,'Metil_Glut',1,'C4DC/C5DC')





################### GA-I(mat) #####################################

colocar_titulos(hoja3,FILA-5,91,13,'GA-I(mat)')

colocar_variable_columna(hoja3, 'glut_c16',FILA,CL+90,2,"Glut/C16")
colocar_variable_columna(hoja3, 'c8_c10',FILA,CL+91,2,"C8/C10")
colocar_variable_columna(hoja3, 'cartina_libre',FILA,CL+92,2,"Carnitina Libre")
colocar_variable_columna(hoja3, 'butiril',FILA,CL+93,2,"Butiril")
colocar_variable_columna(hoja3, 'c4_c2',FILA,CL+94,2,"C4/C2")
colocar_variable_columna(hoja3, 'c4_c3',FILA,CL+95,2,"C4/C3")
colocar_variable_columna(hoja3, 'c4_c8',FILA,CL+96,2,"C4/C8")
colocar_variable_columna(hoja3, 'estearoil',FILA,CL+97,2,"Estearoil")
colocar_variable_columna(hoja3, 'c18_1',FILA,CL+98,2,"C18:1")
colocar_variable_columna(hoja3, 'glut_c5oh',FILA,CL+99,2,"Glut/C5OH")
colocar_variable_columna(hoja3, 'miristoil',FILA,CL+100,2,"Miristoil")
colocar_variable_columna(hoja3, 'c14_1',FILA,CL+101,2,"C14:1")
colocar_variable_columna(hoja3, 'c16_1',FILA,CL+102,2,"C16:1")


################### SUCLA2 #####################################

colocar_titulos(hoja3,FILA-5,104,3,'SUCLA2')

colocar_variable_columna(hoja3, 'metilmalonil',FILA,CL+103,1,"Metilmalonil")
colocar_variable_columna_div(hoja3,Metil_Glut ,FILA,CL+104,'Metil_Glut',1,'C4DC/C5DC')
colocar_variable_columna_div(hoja3,Metil_Ace ,FILA,CL+105,'Metil_Ace',1,'C4DC/C2')


################### SUCLG1 #####################################

colocar_titulos(hoja3,FILA-5,107,4,'SUCLG1')

colocar_variable_columna(hoja3, 'metilmalonil',FILA,CL+106,2,"Metilmalonil")
colocar_variable_columna(hoja3, 'c3_c16',FILA,CL+107,2,"C3/C16")
colocar_variable_columna_div(hoja3,Metil_Ace ,FILA,CL+108,'Metil_Ace',2,'Metil/Ace')
colocar_variable_columna_div(hoja3,Metil_Glut ,FILA,CL+109,'Metil_Glut',2,'Metil/Glut')


################### MAL #####################################

colocar_titulos(hoja3,FILA-5,111,2,'MAL')

colocar_variable_columna(hoja3, 'malonil',FILA,CL+110,1,"Malonil")
colocar_variable_columna(hoja3, 'c3dc_c10',FILA,CL+111,1,"C3DC/C10")




###################HOJA 4 Box################################3



####B2 def(mat)#########

colocar_titulos(hoja4,FILA-5,2,7,'B2 Def(mat)')

colocar_variable_columna(hoja4, 'codigo_de_muestra',FILA,CL,2,"CODIGO")
colocar_variable_columna(hoja4, 'c5_c0',FILA,CL+1,1,"C5/C0")
colocar_variable_columna(hoja4, 'c5_c2',FILA,CL+2,1,"C5/C2")
colocar_variable_columna(hoja4, 'c5_c3',FILA,CL+3,1,"C5/C3")
colocar_variable_columna(hoja4, 'c8_c2',FILA,CL+4,1,"C8/C2")
colocar_variable_columna_div(hoja4,Met_Cit,FILA,CL+5,'Met_Cit',1,'Met/Cit')
colocar_variable_columna(hoja4, 'propionil',FILA,CL+6,1,"Propionil")
colocar_variable_columna_div(hoja4,Met_Xle,FILA,CL+7,'Met_Xle',1,'Met/Xle')

################ CUID ###########################

colocar_titulos(hoja4,FILA-5,9,8,'CUID')

colocar_variable_columna(hoja4, 'cartina_libre',FILA,CL+8,2,"Carnitina Libre")
colocar_variable_columna(hoja4, 'acetil_carnitina',FILA,CL+9,2,"Acetil Carnitina")
colocar_variable_columna(hoja4, 'propionil',FILA,CL+10,2,"Propionil")
colocar_variable_columna(hoja4, 'c3_met',FILA,CL+11,2,"C3/Met")
colocar_variable_columna(hoja4, 'miristoil',FILA,CL+12,2,"Miristoil")
colocar_variable_columna(hoja4, 'palmitoil',FILA,CL+13,2,"Palmitoil")
colocar_variable_columna(hoja4, 'estearoil',FILA,CL+14,2,"Estearoil")
colocar_variable_columna(hoja4, 'c18_1',FILA,CL+15,2,"C18:1")

################ CUID (mat)###########################

colocar_titulos(hoja4,FILA-5,17,10,'CUID (mat)')

colocar_variable_columna(hoja4, 'cartina_libre',FILA,CL+16,1,"Carnitina Libre")
colocar_variable_columna(hoja4, 'acetil_carnitina',FILA,CL+17,1,"Acetil Carnitina")
colocar_variable_columna(hoja4, 'propionil',FILA,CL+18,1,"Propionil")
colocar_variable_columna(hoja4, 'c3_met',FILA,CL+19,1,"C3/Met")
colocar_variable_columna(hoja4, 'metilmalonil',FILA,CL+20,1,"Metilmalonil")
colocar_variable_columna(hoja4, 'palmitoil',FILA,CL+21,1,"Palmitoil")
colocar_variable_columna(hoja4, 'estearoil',FILA,CL+22,1,"Estearoil")
colocar_variable_columna(hoja4, 'c18_1',FILA,CL+23,1,"C18:1")
colocar_variable_columna(hoja4, 'c18_2',FILA,CL+24,1,"C18:2")
colocar_variable_columna(hoja4, 'glutaril',FILA,CL+25,1,"GlutMRM")


################ CPT I ###########################

colocar_titulos(hoja4,FILA-5,27,12,'CPT I')

colocar_variable_columna(hoja4, 'cartina_libre',FILA,CL+26,2,"Carnitina Libre")
colocar_variable_columna(hoja4, 'c0__c16_c18_',FILA,CL+27,2,"C0/(C16+C18)")
colocar_variable_columna(hoja4, 'c5oh_c0',FILA,CL+28,2,"C5OH/C0")
colocar_variable_columna(hoja4, 'c16_c18_1__c2',FILA,CL+29,2,"(C16+C18:1)/C2")
colocar_variable_columna(hoja4, 'c3_c16',FILA,CL+30,2,"C3/C16")
colocar_variable_columna(hoja4, 'c5_c0',FILA,CL+31,2,"C5/C0")
colocar_variable_columna(hoja4, 'palmitoil',FILA,CL+32,2,"Palmitoil")
colocar_variable_columna(hoja4, 'estearoil',FILA,CL+33,2,"Estearoil")
colocar_variable_columna(hoja4, 'c18_1',FILA,CL+34,2,"C18:1")
colocar_variable_columna(hoja4, 'c18_2',FILA,CL+35,2,"C18:2")
colocar_variable_columna(hoja4, 'glutaril',FILA,CL+36,2,"GlutMRM")
colocar_variable_columna_div(hoja4,Glu_Cit,FILA,CL+37,'Glu_Cit',2,'Glu/Cit')


################ CPT I(p479I) ###########################

colocar_titulos(hoja4,FILA-5,39,10,'CPT I(p479I)')


colocar_variable_columna(hoja4, 'c0__c16_c18_',FILA,CL+38,1,"C0/(C16+C18)")
colocar_variable_columna(hoja4, 'c16_1',FILA,CL+39,1,"C16:1")
colocar_variable_columna(hoja4, 'glutaril',FILA,CL+40,1,"GlutMRM")
colocar_variable_columna_div(hoja4,Glu_Cit,FILA,CL+41,'Glu_Cit',1,'Glu/Cit')
colocar_variable_columna(hoja4, 'cartina_libre',FILA,CL+42,1,"Carnitina Libre")
colocar_variable_columna(hoja4, 'c3_c16',FILA,CL+43,1,"C3/C16")
colocar_variable_columna(hoja4, 'c14_1_c16',FILA,CL+44,1,"C14:1/C16")
colocar_variable_columna(hoja4, 'c5oh_c0',FILA,CL+45,1,"C5OH/C0")
colocar_variable_columna(hoja4, 'palmitoil',FILA,CL+46,1,"Palmitoil")
colocar_variable_columna(hoja4, 'c16_c18_1__c2',FILA,CL+47,1,"(C16+C18:1)/C2")


################ CPT II ####################################

colocar_titulos(hoja4,FILA-5,49,21,'CPT II')


colocar_variable_columna(hoja4, 'palmitoil',FILA,CL+48,2,"Palmitoil")
colocar_variable_columna(hoja4, 'c16_1',FILA,CL+49,2,"C16:1")
colocar_variable_columna(hoja4, 'estearoil',FILA,CL+50,2,"Estearoil")
colocar_variable_columna(hoja4, 'c16_c18_1__c2',FILA,CL+51,2,"(C16+C18:1)/C2")
colocar_variable_columna(hoja4, 'prolina',FILA,CL+52,2,"ProMRM")
colocar_variable_columna(hoja4, 'asa',FILA,CL+53,2,"ASA")
colocar_variable_columna(hoja4, 'dodecanoil',FILA,CL+54,2,"Dodecanoil")
colocar_variable_columna(hoja4, 'miristoil',FILA,CL+55,2,"Miristoil")
colocar_variable_columna(hoja4, 'c16_oh',FILA,CL+56,2,"C16-OH")
colocar_variable_columna(hoja4, 'c18_1',FILA,CL+57,2,"C18:1")
colocar_variable_columna(hoja4, 'c18_1_oh',FILA,CL+58,2,"C18:1-OH")
colocar_variable_columna(hoja4, 'c18_2',FILA,CL+59,2,"C18:2")
colocar_variable_columna_div(hoja4,C14_Ace,FILA,CL+60,'C14_Ace',2,'C14:1/C2')
colocar_variable_columna(hoja4, 'c0__c16_c18_',FILA,CL+61,2,"C0/(C16+C18)")
colocar_variable_columna(hoja4, 'acetil_carnitina',FILA,CL+62,2,"Acetil Carnitina")
colocar_variable_columna(hoja4, 'propionil',FILA,CL+63,2,"Propionil")
colocar_variable_columna(hoja4, 'c3_c16',FILA,CL+64,2,"C3/C16")
colocar_variable_columna(hoja4, 'c3_met',FILA,CL+65,2,"C3/Met")
colocar_variable_columna(hoja4, 'c3dc_c10',FILA,CL+66,2,"C3DC/C10")
colocar_variable_columna(hoja4, 't3oh_butiril',FILA,CL+67,2,"3OH-Butiril")
colocar_variable_columna(hoja4, 'glut_c16',FILA,CL+68,2,"Glut/C16")

################ CACT ####################################

colocar_titulos(hoja4,FILA-5,70,14,'CACT')

colocar_variable_columna(hoja4, 'miristoil',FILA,CL+69,1,"Miristoil")
colocar_variable_columna(hoja4, 'palmitoil',FILA,CL+70,1,"Palmitoil")
colocar_variable_columna(hoja4, 'c16_1',FILA,CL+71,1,"C16:1")
colocar_variable_columna(hoja4, 'c16_c18_1__c2',FILA,CL+72,1,"(C16+C18:1)/C2")
colocar_variable_columna(hoja4, 'c0__c16_c18_',FILA,CL+73,1,"C0/(C16+C18)")
colocar_variable_columna(hoja4, 'dodecanoil',FILA,CL+74,1,"Dodecanoil")
colocar_variable_columna(hoja4, 'c16_oh',FILA,CL+75,1,"C16-OH")
colocar_variable_columna(hoja4, 'estearoil',FILA,CL+76,1,"Estearoil")
colocar_variable_columna(hoja4, 'c18_1',FILA,CL+77,1,"C18:1")
colocar_variable_columna(hoja4, 'c18_2',FILA,CL+78,1,"C18:2")
colocar_variable_columna(hoja4, 'c18_oh',FILA,CL+79,1,"C18-OH")
colocar_variable_columna(hoja4, 'asa',FILA,CL+80,1,"ASA")
colocar_variable_columna(hoja4, 'asa_arg',FILA,CL+81,1,"Asa/Arg")
colocar_variable_columna(hoja4, 'c3_c16',FILA,CL+82,1,"C3/C16")


################ GA II ####################################

colocar_titulos(hoja4,FILA-5,84,25,'GA II')

colocar_variable_columna(hoja4, 'butiril',FILA,CL+83,2,"Butiril")
colocar_variable_columna(hoja4, 'c4_c2',FILA,CL+84,2,"C4/C2")
colocar_variable_columna(hoja4, 'c4_c3',FILA,CL+85,2,"C4/C3")
colocar_variable_columna(hoja4, 'isovaleril',FILA,CL+86,2,"Isovaleril")
colocar_variable_columna(hoja4, 'c5_c0',FILA,CL+87,2,"C5/C0")
colocar_variable_columna(hoja4, 'c5_c2',FILA,CL+88,2,"C5/C2")
colocar_variable_columna(hoja4, 'c5_c3',FILA,CL+89,2,"C5/C3")
colocar_variable_columna(hoja4, 'glutaril',FILA,CL+90,2,"Glutaril")
colocar_variable_columna(hoja4, 'glut_c5oh',FILA,CL+91,2,"Glut/C5OH")
colocar_variable_columna(hoja4, 'hexanoil',FILA,CL+92,2,"Hexanoil")
colocar_variable_columna(hoja4, 'octanoil',FILA,CL+93,2,"Octanoil")
colocar_variable_columna(hoja4, 'c8_c2',FILA,CL+94,2,"C8/C2")
colocar_variable_columna(hoja4, 'decanoil',FILA,CL+95,2,"Decanoil")
colocar_variable_columna(hoja4, 'decenoil',FILA,CL+96,2,"Decenoil")
colocar_variable_columna(hoja4, 'dodecanoil',FILA,CL+97,2,"Dodecanoil")
colocar_variable_columna(hoja4, 'dodecenoil',FILA,CL+98,2,"Dodecenoil")
colocar_variable_columna(hoja4, 'miristoil',FILA,CL+99,2,"Miristoil")
colocar_variable_columna(hoja4, 'c14_1',FILA,CL+100,2,"C14:1")
colocar_variable_columna(hoja4, 'c14_1_c16',FILA,CL+101,2,"C14:1/C16")
colocar_variable_columna(hoja4, 'c14_2',FILA,CL+102,2,"C14:2")
colocar_variable_columna(hoja4, 'c16_1',FILA,CL+103,2,"C16:1")
colocar_variable_columna_div(hoja4,C14_Ace,FILA,CL+104,'C14_Ace',2,'C14:1/C2')
colocar_variable_columna(hoja4, 'c16_c18_1__c2',FILA,CL+105,2,"(C16+C18:1)/C2")
colocar_variable_columna(hoja4, 'c3dc_c10',FILA,CL+106,2,"C3DC/C10")
colocar_variable_columna(hoja4, 'c5oh_c8',FILA,CL+107,2,"C5OH/C8")


##############RED #########################

colocar_titulos(hoja4,FILA-5,109,9,'RED')


colocar_variable_columna(hoja4, 'c10_2',FILA,CL+108,1,"C10:2")
colocar_variable_columna(hoja4, 'isovaleril',FILA,CL+109,1,"Isovaleril")
colocar_variable_columna(hoja4, 'miristoil',FILA,CL+110,1,"Miristoil")
colocar_variable_columna(hoja4, 'c14_1',FILA,CL+111,1,"C14:1")
colocar_variable_columna(hoja4, 'c16_oh',FILA,CL+112,1,"C16-OH")
colocar_variable_columna(hoja4, 'c18_1_oh',FILA,CL+113,1,"C18:1-OH")
colocar_variable_columna(hoja4, 'tirosina',FILA,CL+114,1,"TyrMRM")
colocar_variable_columna_div(hoja4,C14_Ace,FILA,CL+115,'C14_Ace',1,'C14:1/C2')
colocar_variable_columna(hoja4,'fen_tyr',FILA,CL+116,1,"Phe/Tyr")

###################### VLCAD #####################################

colocar_titulos(hoja4,FILA-5,118,8,'VLCAD')


colocar_variable_columna(hoja4, 'miristoil',FILA,CL+117,2,"Miristoil")
colocar_variable_columna(hoja4, 'c14_1',FILA,CL+118,2,"C14:1")
colocar_variable_columna(hoja4, 'c14_1_c16',FILA,CL+119,2,"C14:1/C16")
colocar_variable_columna_div(hoja4,C14_Ace,FILA,CL+120,'C14_Ace',2,'C14:1/C2')
colocar_variable_columna(hoja4,'fen_tyr',FILA,CL+121,2,"C14:1/C12:1")
colocar_variable_columna(hoja4, 'dodecanoil',FILA,CL+122,2,"Dodecanoil")
colocar_variable_columna(hoja4, 'dodecenoil',FILA,CL+123,2,"Dodecenoil")
colocar_variable_columna(hoja4, 'c14_2',FILA,CL+124,2,"C14:2")


###################### LCHAD/TFP #####################################

colocar_titulos(hoja4,FILA-5,126,14,'LCHAD/TFP')


colocar_variable_columna(hoja4, 'c16_oh',FILA,CL+125,1,"C16-OH")
colocar_variable_columna(hoja4, 'c16oh_c16',FILA,CL+126,1,"C16OH/C16")
colocar_variable_columna(hoja4, 'c18_1_oh',FILA,CL+127,1,"C18:1-OH")
colocar_variable_columna(hoja4, 'c18_oh',FILA,CL+128,1,"C18-OH")
colocar_variable_columna_div(hoja4,C18_2_Est,FILA,CL+129,'C18_2_Est',1,'C18-OH/C18')
colocar_variable_columna(hoja4, 'dodecanoil',FILA,CL+130,1,"Dodecanoil")
colocar_variable_columna(hoja4, 'miristoil',FILA,CL+131,1,"Miristoil")
colocar_variable_columna(hoja4, 'c14_1',FILA,CL+132,1,"C14:1")
colocar_variable_columna_div(hoja4,C14_Ace,FILA,CL+133,'C14_Ace',1,'C14:1/C2')
colocar_variable_columna(hoja4, 'c14_1_c16',FILA,CL+134,1,"C14:1/C16")
colocar_variable_columna(hoja4, 'c14_2',FILA,CL+135,1,"C14:2")
colocar_variable_columna(hoja4, 'c16_1',FILA,CL+136,1,"C16:1")
colocar_variable_columna(hoja4, 'c16_1_oh',FILA,CL+137,1,"C16:1-OH")
colocar_variable_columna(hoja4, 'c18_2_oh',FILA,CL+138,1,"C18:2-OH")

###################### M/SCHAD #####################################

colocar_titulos(hoja4,FILA-5,140,5,'M/SCHAD')

colocar_variable_columna(hoja4, 't3oh_butiril',FILA,CL+139,2,"3OH-Butiril")
colocar_variable_columna(hoja4, 'c3_c16',FILA,CL+140,2,"C3/C16")
colocar_variable_columna(hoja4, 'glut_c16',FILA,CL+141,2,"Glut/C16")
colocar_variable_columna(hoja4, 'glut_c8',FILA,CL+142,2,"Glut/C8")
colocar_variable_columna(hoja4, 't3oh_hexanoil',FILA,CL+143,2,"3OH-Hexanoil")


###################### MCAD #####################################
colocar_titulos(hoja4,FILA-5,145,9,'MCAD')

colocar_variable_columna(hoja4, 'octanoil',FILA,CL+144,1,"Octanoil")
colocar_variable_columna(hoja4, 'c8_c10',FILA,CL+145,1,"C8/C10")
colocar_variable_columna(hoja4, 'c8_c2',FILA,CL+146,1,"C8/C2")
colocar_variable_columna(hoja4, 'hexanoil',FILA,CL+147,1,"Hexanoil")
colocar_variable_columna(hoja4, 'decenoil',FILA,CL+148,1,"Decenoil")
colocar_variable_columna(hoja4, 'c4_c8',FILA,CL+149,1,"C4/C8")
colocar_variable_columna(hoja4, 'glut_c8',FILA,CL+150,1,"Glut/C8")
colocar_variable_columna(hoja4, 'c5oh_c8',FILA,CL+151,1,"C5OH/C8")
colocar_variable_columna(hoja4, 'decanoil',FILA,CL+152,1,"Decanoil")


###################### MCAD (het) #####################################

colocar_titulos(hoja4,FILA-5,154,5,'MCAD (het)')

colocar_variable_columna(hoja4, 'octanoil',FILA,CL+153,2,"Octanoil")
colocar_variable_columna(hoja4, 'decanoil',FILA,CL+154,2,"Decanoil")
colocar_variable_columna(hoja4, 'hexanoil',FILA,CL+155,2,"Hexanoil")
colocar_variable_columna(hoja4, 'c8_c2',FILA,CL+156,2,"C8/C2")
colocar_variable_columna(hoja4, 'c5oh_c8',FILA,CL+157,2,"C5OH/C8")


###################### MCAD (mat) #####################################

colocar_titulos(hoja4,FILA-5,159,6,'MCAD (mat)')

colocar_variable_columna(hoja4, 'octanoil',FILA,CL+158,1,"Octanoil")
colocar_variable_columna(hoja4, 'c8_c2',FILA,CL+159,1,"C8/C2")
colocar_variable_columna(hoja4, 'cartina_libre',FILA,CL+160,1,"Carnitina Libre")
colocar_variable_columna(hoja4, 'acetil_carnitina',FILA,CL+161,1,"Acetil Carnitina")
colocar_variable_columna(hoja4, 'c5oh_c8',FILA,CL+162,1,"C5OH/C8")
colocar_variable_columna(hoja4, 'c18_1',FILA,CL+163,1,"C18:1")


###################### SCAD #####################################

colocar_titulos(hoja4,FILA-5,165,4,'SCAD')

colocar_variable_columna(hoja4, 'butiril',FILA,CL+164,2,"Butiril")
colocar_variable_columna(hoja4, 'c4_c2',FILA,CL+165,2,"C4/C2")
colocar_variable_columna(hoja4, 'c4_c3',FILA,CL+166,2,"C4/C3")
colocar_variable_columna(hoja4, 'c4_c8',FILA,CL+167,2,"C4/C8")



LOTE=str(LOTE_DE_DATOS)
fecha= datetime.now()
ran=str(random.randrange(99))
string_fecha=str(fecha.day+fecha.month+fecha.year+fecha.hour)
Archivo="files/Tamizaje_Lote_"+LOTE+"_V_"+str(fecha.hour)+str(fecha.minute)+"-"+str(fecha.second)+".xls"
print LOTE 
libro.save(Archivo)


        
##TEMP=consulta(NEONATOS,LOTE_DE_DATOS,TIPO_DE_DATOS)
####imprimir(TEMP)
##COLUMNA=seleccionar_variable(TEMP,'prolina')

##C=percentil(COLUMNA,50)

        
