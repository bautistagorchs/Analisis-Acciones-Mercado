# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:16:38 2024

@author: agjar
"""

# 1)Extractora

# PRECONDICIONES:


# -Recorrer los archivos
# -Tomar los valores
# -Devolver diccio

# ESTRATEGIA:

# -Crear una función que reciba una lista por parámetro
# -Abrir y recorrer los archivos
# -Crear un diccio vacío 
# -Crear una segunda función que recorra los datos de cada accion



import matplotlib.pyplot as plt

################################   FORMATO FECHAS  ###########################################


from datetime import datetime

def convert_2_datetime(date_list):
 return [datetime.strptime(date, "%Y-%m-%d") for date in date_list]

        
def formatear_fecha(lista_fechas):
    nueva_lista = []
    datetime = convert_2_datetime(lista_fechas)
    
    for fecha in datetime:
        nueva_lista.append(fecha.year)
    return nueva_lista













     

################################   PARTE 1  ###########################################


acciones = ['AAPL','IBM','INTC','JNJ','MSFT','NSRGY']

def guardar_datos(archivo):
    datos_accion = {'Date':[], 'Open':[],'High':[],'Low':[],'Close':[]}
    linea0 = archivo.readline().strip().split(',')
    
    for linea in archivo:
        valores = linea.strip().split(',')
        for clave,valor in zip(linea0,valores):
            if clave == "Date":
                datos_accion[clave].append(valor)
            else:
                datos_accion[clave].append(float(valor))
        
    return datos_accion



def extractora (lista):
    info_acciones = {}
    for accion in lista:
        with open(f"{accion}.csv","r") as archivo:
            por_accion = guardar_datos(archivo)
            info_acciones[accion] = por_accion
    return info_acciones














            
################################   PARTE 2  ###########################################

def posiciones(lista):
    division = len(lista) / 9
    v = list(range(0, len(lista), int(division)))
    return v

def shown_labels(lista, posiciones_que_quiero):
    resultado = []
    
    for pos in posiciones_que_quiero:
        resultado.append(lista[pos])
        
    return resultado
        
        
          
def graficadora_accion(diccionario,accion):
    accs = extractora([accion])[accion]
        
    date = accs['Date']
    formated_date = formatear_fecha(date)
    posiciones_a_mostrar = posiciones(date)
    
    high = accs["High"]
    low = accs["Low"]
    opn = accs["Open"]
    close = accs["Close"]
    
    plt.figure()
    plt.title(accion)
    plt.tight_layout()
    
    plt.plot(date,opn,color='blue',label='Open')
    plt.plot(date,high,color='green',label='High')
    plt.plot(date,low,color='red',label='Low')
    plt.plot(date,close,color='orange',label='Close')
    
    plt.xlabel('Año')
    plt.ylabel('Valor')
    plt.xticks(ticks=posiciones_a_mostrar, labels=shown_labels(formated_date, posiciones_a_mostrar))
    
    plt.legend()
    plt.show()
    











################################   PARTE 3  ###########################################

def graficar_comparacion(diccionario, columna):
    graficar = {}
    
    if columna not in ["High", "Close", "Open", "Low"]:
        return print(f"La columna {columna} no existe")
    
    plt.figure()
    plt.title(columna)
    plt.tight_layout()
    # plt.spines()
    
    plt.xlabel('Año')
    plt.ylabel('Valor')
    
    for accion, valores in diccionario.items():
        fechas = valores["Date"]
        graficar[accion] = valores[columna]
        
    for accion in graficar:
        formated_date = formatear_fecha(fechas)
        posiciones_a_mostrar = posiciones(fechas)
        plt.plot(fechas, graficar[accion], label=accion)
        plt.xticks(ticks=posiciones_a_mostrar, labels=shown_labels(formated_date, posiciones_a_mostrar))
    
    plt.legend()
    plt.show()

# graficar_comparacion(extractora(acciones), "High")













################################   PARTE 4  ###########################################


