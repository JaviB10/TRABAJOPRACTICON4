#CONSIGNA DEL PROGRAMA
#Se requiere un programa para un negocio en el cual se soliciten los siguientes datos:
#Largo y Ancho de una habitacion
#Largo y Ancho de un ceramico elegido
#Precio por caja (sabiendo que por cada caja vienen 10 ceramicos)
#Para obtener:
#Cantida de ceramicos que se necesitan
#Cantidad de cajas a comprar
#Precio a pagar

import math

SUPERFICIEHAB = 0
SUPERFICIECER = 0
SUPERFICIECAJA = 0
CANTIDADCER = 0
CANTIDADCAJ = 0
PRECTOTAL = 0

#Primero preguntamos si se desea utilizar el programa para calcular
NEGOCIO = str(input("Si desea ingresar los datos ponga S, de lo contrario ponga N"))

while NEGOCIO == "S":

    #Solicitamos en largo y ancho de la habitacion
    LARGOHAB = float(input("Ingrese el largo de la habitacion: "))
    ANCHOHAB = float(input("Ingrese el ancho de la habitacion: "))

    #Ahora solicitamos el largo y ancho del ceramico que elegimos
    LARGOCER = float(input("Ingrese el largo del ceramico: "))
    ANCHOCER = float(input("Ingrese el ancho del ceramico: "))

    #Ahora solicitaremos el precio por caja de los ceramicos elegidos
    PRECIOCER = float(input("Ingrese el precio por caja de los ceramicos elegidos: "))

    #En esta primera parte solicitamos los datos para realizar los calculos

#Ahora que ya tenemos todos los datos proseguiremos a calcular lo que se necesita

    #Primero calculamos las superficies
    SUPERFICIEHAB = LARGOHAB * ANCHOHAB
    SUPERFICIECER = LARGOCER * ANCHOCER
    #Este calculo corresponde a la superficie que cubren los 10 ceramicos que trae la caja
    SUPERFICIECAJA = SUPERFICIECER * 10

    #En esta segunda parte calculamos las superficies que necesitamos para responder a las preguntas finales

#Ahora que ya calculamos las superficies proseguiremos a calcular lo que se necesita para responder a las solicitudes finales

    #Calculamos la cantidad de ceramicos que se necesitan
    CANTIDADCER = SUPERFICIEHAB / SUPERFICIECER
    CANTIDADCER = math.ceil(CANTIDADCER)

    #Calculamos las cajas que necesitaremos (sabiendo que por cada caja vienen 10 ceramicos)
    CANTIDADCAJ = SUPERFICIEHAB / SUPERFICIECAJA
    CANTIDADCAJ = math.ceil(CANTIDADCAJ)

    #Calculamos el precio a pagar por las cajas que necesitaremos
    PRECTOTAL = CANTIDADCAJ * PRECIOCER

    #En esta tercera parte calculamos las cantidades necesarias y el precio total que deberemos pagar
