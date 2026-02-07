import random
import tablero

#-------CLASE TABLERO--------------
# #TODO: refactorizar en una clase

# #genera un tablero de arrays de alto x largo
# #deberia permtir cualquier valor dentro de estas
# def genTablero(alto, ancho):
#     #TODO descomentar cuando se refactorie en un aclase
#     cuadricula = []
#     for x in range(ancho):
#         cuadricula.append([])

#     for i in cuadricula:
#         for y in range(alto):
#             i.append([])
#     return(cuadricula)

# #asigna el item a la casilla x,y 
# def setCasilla(posX, posY, item, cuadricula):
#     cuadricula[posX][posY] = item
#     return cuadricula

# #return el item en la casilla
# def getCasilla(posX, posY, cuadricula):
#     return cuadricula[posX][posY]

# #llena todos los espacios del array de item
# def fillWhitItem(item, cuadricula):
#     for x in cuadricula:
#         for y in range(len(cuadricula)):
#             setCasilla(x,y,item)

# #devuelve la cantidad de casillas totales
# def espacioLibre(cuadricula):
#     total = len(cuadricula) #x
#     total = total * len(cuadricula[0])#y    #TODO:no me gusta el 0 
#     return total

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

#colocare los barcos en posicion horizontal o vertical , donde caiga empujare
#hacia dentro del tablero


#caben los barcos?
#compara el espacio de los barcos con el espacio de la cuadricula
#true si hay espacio false si no
def hayEspacio (cuadricula):
    espacioCuadricula = tablero.espacioLibre(cuadricula)
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


def hayHueco(posX, posy, longitud, esHorizontal, tablero):
    """
    Comprueba que se pueda colocar un barco en X,Y de longitud en el tablero
    RETURN TRUE si no hay otros barcos 
    :param posX: posicion en X donde empezar a comrpobar
    :param posy: posicion en Y donde empezar a comrpobar
    :param longitud: casisllas a comrpobar desde posX y posY
    :param esHorizontal: determina si aumentar en posX (TRUE) o posY(FALSE) las comprobaciones
    :param tablero: cuadricula donde comprobar 
    """

    


def colocarNaves(longitud, cantidad, tablero):
    """
    marca desde una posicion aleatoria vertical u horizontal en la tablero
    y marca en longitud, si superpone busca otro sitio aleatorio
    
    :param longitud: longitud a marcar
    :param cantidad: distintas marcas a realizar
    :param tablero: tablero a marcar
    """
    for i in range(cantidad):
        #seed de las posiciones 
        #establece un punto de inicio y si crece a la derecha o abajo segun longitud
        posX = random(0, tablero.ancho())
        posY = random(0, tablero.alto())
        horizontal = esHorizontal()

        #arreglando las posiciones que se salen fuera de los bordes
        #empujarlos hacia dentro
        if horizontal:
            #horinzontal X
            if posX + longitud > tablero.ancho():
                posX = (posX + longitud) - tablero.ancho()
        else:
            #vertical Y
            if posY + longitud > tablero.alto():
                posY = (posY + longitud) - tablero.alto()

        #comprobar superposicion de barcos
        superposicion = False
        if horizontal:
            #horizontal
            for x in range( posX, posX + longitud):
                if tablero.getCasilla(x, posY) == SHIP_SIN_TOCAR:
                    
        else:
            #vertical



def esHorizontal():
    """
    decide de manera aleatoria 50% entre true o false
    """
    if random(0,1) == 1:
        return True
    else:
        return False
        

#-------CLASE JUEGO--------------


WATER = "O"
SHIP_TOCADA  = "X"
SHIP_SIN_TOCAR = "T"


