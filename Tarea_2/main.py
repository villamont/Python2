##main 
import plotting_API_NASA as nasa

##variables golbales
Salir = True

##define lista de meses del anio
meses_anio=['None', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
print("""Este programa te muestra datos interesantes del proyecto MARS ROVER, 
por favor escoja una opcion del siguiente menu\n""")





def opciones_usr():
##---------------------------------- Curiosity-----------------------------------------
    #sal=' '
    #while sal != 'Salir':   
        
       # try:
            opcion=int(input("[1] ==> Fotos tomadas por la Sonda Curiosity en un mes y año determinado\n[2] ==> Fotos tomadas por la Sonda Opportunity en un mes y año deternimado\n[3] ==> Asteroides cercanos a la tierra en un rango de 5 dias\n\n"))
        
            if opcion == 1:
                print("""La base de datos de Curiosity muestra informacion en un rengo de fechas entre 2014-10-01 a la fecha actual (2023-08-10)\n
        \n1 => Enero\n2 => Febrero\n3 => Marzo\n4 => Abril\n5 => Mayo\n6 => Junio\n7 =>Julio\n8 => Agosto\n9 => Setiembre\n10 => Octubre\n11 => Noviembre\n12 => Diciembre 
        """)
                month=int(input("Por favor escoja un mes del anio de acuerdo al numero de mes:  "))    
                annio=int(input("Por favor escoga un anio en formato xxxx:  "))
                year=str(annio)
                nasa.getCuriosity(year, meses_anio[month], month)

        ##---------------------------------------------------------------------------------------


        ##----------------------------------Opportunity -----------------------------------------
            elif opcion == 2:
                print("""La base de datos de Opportunity muestra informacion en un rango de fechas entre 2004-01-26 hasta 2018-06-07\n
        \n1 => Enero\n2 => Febrero\n3 => Marzo\n4 => Abril\n5 => Mayo\n6 => Junio\n7 =>Julio\n8 => Agosto\n9 => Setiembre\n10 => Octubre\n11 => Noviembre\n12 => Diciembre 
        """)
                month=int(input("Por favor escoja un mes del anio de acuerdo al numero de mes:  "))
                annio=int(input("Por favor escoga un anio en formato xxxx:  "))
                year=str(annio)
                nasa.getOpportunity(year, meses_anio[month], month)

            elif opcion == 3:
                fecha_ini=str(input("\n Ingrese el rango de fechas (maximo de 5 dias) entre 1900-01-01 a la fecha actual (2023-08-04) \nPor favor ingrese una fecha inicial\n"))
                fecha_fin=str(input("\nPor favor ingrese una fecha final\n"))
                nasa.getAsteroids(fecha_ini, fecha_fin)

            else:
                print("Opcion equivocada")

        #except ValueError:
            #print("\nOpcion no valida, por favor ingresa un valor valido") 


        
##---------------------------------------------------------------------------------------


if __name__ == '__main__':
    

    while  Salir:
        opciones_usr()
        salr=str(input('Desea solicitar mas informacion\n si > continuar\n no > salir\n'))
        if salr=='si':
            opciones_usr()
            
        elif salr == 'no':
            Salir=False          
        
        else:
            print("Por favor escoja una opcion valida")