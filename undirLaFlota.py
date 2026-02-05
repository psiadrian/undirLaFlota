import random


#-------CLASE TABLERO--------------
#TODO: refactorizar en una clase

#genera un tablero de arrays de alto x largo
#deberia permtir cualquier valor dentro de estas
def genTablero(alto, ancho):
    #TODO descomentar cuando se refactorie en un aclase
    cuadricula = []
    for x in range(ancho):
        cuadricula.append([])

    for i in cuadricula:
        for y in range(alto):        
            i.append([])
    return(cuadricula)

#asigna el item a la casilla x,y 
def setCasilla(posX, posY, item, cuadricula):
    cuadricula[posX][posY] = item
    return cuadricula

#return el item en la casilla
def getCasilla(posX, posY, cuadricula):
    return cuadricula[posX][posY]

#llena todos los espacios del array de item
def fillWhitItem(item, cuadricula):
    for x in cuadricula:
        for y in range(len(cuadricula)):
            setCasilla(x,y,item)

#devuelve la cantidad de casillas totales
def espacioLibre(cuadricula):
    total = len(cuadricula) #x
    total = total * len(cuadricula[0])#y    #TODO:no me gusta el 0 
    return total

#--------------------------


#---------colocando barcos-------------

#longitud y cantidad de los barcos
#TODO: modificar como se generan la informacion de los barcos 
cantPortaviones = 1
longPortaviones = 4

cantSubmarinos = 2
longSubmarinos = 3

cantDestructores = 3
longDestructores = 2

#coloca los barcos manera aleatoria en el tablero,
#no pueden superponerse dos barcos en una misma casilla,
#ni salirse del tablero




#caben los barcos?
#compara el espacio de los barcos con el espacio de la cuadricula
#true si hay espacio false si no
def hayEspacio (cuadricula):
    espacioCuadricula = espacioLibre(cuadricula)
    espacioBarcos = espacioNaves()
    return True if espacioCuadricula < espacioBarcos else False


#calcula el espacio total de los barcos
def espacioNaves():
    #TODO refactorizar
    total = 0
    total = total + cantPortaviones * longPortaviones
    total = total + cantSubmarinos * longSubmarinos
    total = total + cantDestructores *longDestructores
    return total


#usa las variables de cantX y longX de los barcos
def colocarNaves(cuadricula):

    if hayEspacio(cuadricula):
        #TODO sacar texto
        raise Exception("no hay espacio en el tablero para colocar los barcos")
    
    






#-------CLASE JUEGO--------------




