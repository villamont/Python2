##main program to calculate sen,cos and tan for Pi

import ClaseTrig
import datetime
ruta='/home/jorgx/Documentos/Python/Nivel_2/Laboratorio_1/Laboratorio_1/'



#################################################################3
#Definicion de la funcion escritura en archivo

def escritura_resultado(resul,oper,time):
# open file with mode 'w'
    archivo = open(ruta + "log.txt", 'a+')
    #print(resul, oper, time,file=archivo)
    print("El resultado de: ", oper,"(Pi) es", resul, "ejecutado el:", time,file=archivo)
    archivo.close

#################################################################
#Menu de operaciones presentadas al Usuario
operacion = ' casa'

print('Este programa calcula las operaciones trigonometicas Seno, Coseno y Tangente del numero Pi')
operacion=str(input('\n\nPor favor escoja la operacion a realizar\n Seno de Pi => sen\n Coseno Pi => cos\n Tangente Pi => tan \n\n ====> '))


## Solicitud de operacion a realizar al usuario
while operacion != 'salir':
    if operacion == 'sen':
        sen=ClaseTrig.Trig("seno")
        print('\n*******************\nEl sen de Pi es: ',sen.senx())
        time=datetime.datetime.now()
        escritura_resultado(sen.senx(),operacion,time)
        operacion=str(input('\n\nPor favor escoja la operacion a realizar\n Seno de Pi => sen\n Coseno Pi => cos\n Tangente Pi => tan \n\n====> '))

    elif operacion == 'cos':
        coseno=ClaseTrig.Trig('coseno')
        print('\n*******************\nEl coseno de Pi es:', coseno.cosx())
        time=datetime.datetime.now()
        escritura_resultado(coseno.cosx(),operacion,time)
        operacion=str(input('\n\nPor favor escoja la operacion a realizar\n Seno de Pi => sen\n Coseno Pi => cos\n Tangente Pi => tan \n\n====> '))

    elif operacion == 'tan':
        tang=ClaseTrig.Trig('tangente')
        print('\n*******************\nLa tangente de Pi es:', tang.tanx())
        time=datetime.datetime.now()
        escritura_resultado(tang.tanx(),operacion,time)
        operacion=str(input('\n\nPor favor escoja la operacion a realizar\n Seno de Pi => sen\n Coseno Pi => cos\n Tangente Pi => tan \n\n====> '))

    else:
        operacion=input('\n ******** Operacion invalida **********\n Por favor escoja la operacion a realizar\n Seno de Pi => sen\n Coseno Pi => cos\n Tangente Pi => tan \n\n====> ')

print('Saliendo, muchas gracias por usar el programa TRIGONOMETRIA')