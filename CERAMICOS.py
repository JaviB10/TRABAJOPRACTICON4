#CONSIGNA DEL PROGRAMA
#Se requiere un programa para un negocio en el cual se soliciten los siguientes datos:
#Largo y Ancho de una habitacion
#Largo y Ancho de un ceramico elegido
#Precio por caja (sabiendo que por cada caja vienen 10 ceramicos)
#Para obtener:
#Cantida de ceramicos que se necesitan
#Cantidad de cajas a comprar
#Precio a pagar


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