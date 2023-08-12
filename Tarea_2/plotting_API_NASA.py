##Tarea 2
import requests
import pandas as pd
import matplotlib.pyplot as plt


##Variables globales
fotos_por_dia=[]

##Creando un diccionario con los meses para determinar la cantidad de dias que tiene cada mes
meses={
    "Enero" : "31", #Enero
    "Febrero" : "28", #Febrero
    "Marzo" : "31", #Marzo
    "Abril" : "30",
    "Mayo" : "31",
    "Junio" : "30",
    "Julio" : "31",
    "Agosto" : "31",
    "Setiembre" : "30",
    "Octubre" : "31",
    "Noviembre" : "30",
    "Diciembre" : "31"
}

##-------------------------Funcion para solicitar asteroides cercanos a la tierra al servidor----------------------------------

def getAsteroids(fecha_inicial, fecha_final):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='
    start_date=fecha_inicial
    amper='&end_date='
    end_date=fecha_final
    key='&api_key='
    API_KEY='T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd'

    url1 = url + start_date + amper + end_date + key + API_KEY
    getResponse = requests.get(url1)

    
    if getResponse.status_code == 200:
        data = getResponse.json()
        aste=data["near_earth_objects"]
        #print(data)
        #print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        #print("Cantidad de asteroides cercanos de la tierra para el rango de fechas :",start_date, "al", end_date, "es: ", data["element_count"])
        print("\nDeberia de haber 4 elementos en aste:\n", len(aste), 'aste es del tipo', type(aste))
        
        #creando lista de asteroides por dia
        asters_dia=[]
        for llave in aste:
            print("\n\n tamanio de llave es: ",len(aste[llave]))
            asters_dia.append(len(aste[llave]))
            prueba=aste[llave]
        
        ##creando lista de llaves 
        list_llaves=aste.keys()
        list_keys=list(list_llaves)

        print("\nImprimiendo lista de llaves \n",list_keys, 'que es de tipo', type(list_keys))
        print("\n Imprimiendo asters_dia", asters_dia)

        ##concatenar 2 listas para crear el Dataframe
        array=pd.DataFrame({'Fecha': 
                        list_keys,
                      'Cantidad de asteriodes': 
                      asters_dia,
                        })
        print("----------------------------------------------------------------------------------------------------------------------------\n\n")       
        plt.plot(array['Fecha'], array['Cantidad de asteriodes'])
        plt.show()
    else:
        print('\nError al realizar la solicitud, por favor escoje otro rango diferente de fechas')

##-------------------------Funcion para solicitar cantidad de photos tomadas por Opportunity---------------------------------


def getOpportunity(anio, mes, month_num):
    part1='https://api.nasa.gov/mars-photos/api/v1/rovers/Opportunity/photos?earth_date='
    year=anio
    month=str(month_num)
    key='&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd'
    
    ##iterando sobre la cantidad de dias que tiene el mes escogido por el usuario
    cantidad_dias=meses[mes]
    numero_dias=int(cantidad_dias)
    #print("Cantidad de dias es: ", numero_dias, "del mes", mes)
    print('\n\nExtrayendo informacion de la base de datos de Opportunity\n ...')

    dias_mes=list()
    for dia in range(1, numero_dias+1):
        earth_date=anio + '-' + month + '-' + str(dia)
        dias_mes.append(earth_date)
        url= part1 + earth_date + key
             
        getResponse = requests.get(url)
                
        if getResponse.status_code == 200:
            fot_opportunity = getResponse.json()
            fotos_por_dia.append(len(fot_opportunity["photos"]))
            
        else:
           print('\n====> Error al realizar la solicitud, por favor ingresa una fecha valida')

    ##concatenar 2 listas para crear el Dataframe
    array=pd.DataFrame({'Fecha': 
                        dias_mes,
                      'Cantidad de fotos': 
                      fotos_por_dia,
                        })
    
    print("Imprimiendo cantidad de fotos tomadas por dia: \n", array)
    
    ##extrayendo el dia en que se tomaron mas fotos y la fecha respectiva
    x=array['Cantidad de fotos'].max()
    maxs=array['Cantidad de fotos'].idxmax()
    
    print('\nEl dia', dias_mes[maxs], "se tomo la mayor cantidad de fotos, un total de:  ", x, "\n")
    
    

    ##Realizando la graficacion de los datos
    print("\nGraficando cantidad de fotos tomadas por la Sonda Opportunity por dia para el mes: ", mes, 'del año', anio )
    plt.plot(dias_mes, fotos_por_dia, color='b', linestyle='solid', marker='o', label='Cantidad de fotos por dia') 
    plt.ylabel('Cantidad de fotos por dia')
    plt.title('Fotos Mes ')  
    plt.xticks(rotation=45, fontsize=6)
    plt.legend()
    plt.show()


    




    

##-------------------------Funcion para solicitar cantidad de photos tomadas por curiosity----------------------------------
#url_curiosity="https://api.nasa.gov/mars-photos/api/v1/manifests/Curiosity?api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd&sol=800"


def getCuriosity(anio, mes, month_num):
    p1='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date='
    year=anio
    month=str(month_num)
    api_key='&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd'
    
##iterando sobre la cantidad de dias que tiene el mes escogido por el usuario
    cantidad_dias=meses[mes]
    numero_dias=int(cantidad_dias)
    #print("Cantidad de dias es: ", numero_dias, "del mes", mes)
    print('\n\nExtrayendo informacion de la base de datos de Curiosity\n ...')

    dias_mes=list()
    for dia in range(1, numero_dias+1):
        earth_date=anio + '-' + month + '-' + str(dia)
        dias_mes.append(earth_date)
        url_curiosity= p1 + earth_date + api_key
             
        getResponse = requests.get(url_curiosity)
                
        if getResponse.status_code == 200:
            fot_Curiosity = getResponse.json()
            fotos_por_dia.append(len(fot_Curiosity["photos"]))
            #print("\n\n\nXXXXXXXXXXXXXXX--Mostrando cantidad de fotos tomadas por Mars Curiosity segun fecha dada por el usuario--XXXXXXXXXXXXXXX")
            #print("Cantidad total de fotos tomadas por Curiosity:", fot_Curiosity["photos"][0]["rover"]["total_photos"])
            #print('Cantidad total de fotos tomadas por Curiosity el dia:',earth_date, " fue ", len(fot_Curiosity["photos"]) )
            #print("----------------------------------------------------------#---------------------------------------------------------------------\n\n")
        else:
           print('\n====> Error al realizar la solicitud, por favor ingresa una fecha valida')

    ##concatenar 2 listas para crear el Dataframe
    array=pd.DataFrame({'Fecha': 
                        dias_mes,
                      'Cantidad de fotos': 
                      fotos_por_dia,
                        })
    
    print("Imprimiendo cantidad de fotos tomadas por dia: \n", array)
    
    ##extrayendo el dia en que se tomaron mas fotos y la fecha respectiva
    x=array['Cantidad de fotos'].max()
    maxs=array['Cantidad de fotos'].idxmax()
    
    print('\nEl dia', dias_mes[maxs], "se tomo la mayor cantidad de fotos, un total de:  ", x, "\n")
    
    

    ##Realizando la graficacion de los datos
    print("\nGraficando cantidad de fotos tomadas por la Sonda Curiosity por dia para el mes: ", mes, 'del año', anio )
    plt.plot(dias_mes, fotos_por_dia, color='b', linestyle='solid', marker='o', label='Cantidad de fotos por dia') 
    plt.ylabel('Cantidad de fotos por dia')
    plt.title('Fotos Mes ')  
    plt.xticks(rotation=45, fontsize=6)
    plt.legend()
    plt.show()


    


