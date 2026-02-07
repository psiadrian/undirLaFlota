import random
from tablero import tablero 

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
# def espacioTotal(cuadricula):
#     total = len(cuadricula) #x
#     total = total * len(cuadricula[0])#y    #TODO:no me gusta el 0 
#     return total

#--------------------------


#---------colocando barcos-------------

#longitud y cantidad de los barcos
#TODO: modificar como se generan la informacion de los barcos 
CANT_PORTAVIONES = 1
LONG_PORTAVIONES = 4

CANT_SUBMARINOS = 2
LONG_SUBMARINOS = 3

CANT_DESTRUCTORES = 3
LONG_DESTRUCTORES = 2

#coloca los barcos manera aleatoria en el tablero,
#no pueden superponerse dos barcos en una misma casilla,
#ni salirse del tablero

#colocare los barcos en posicion horizontal o vertical , donde caiga empujare
#hacia dentro del tablero
def colocarBarcos(tablero):
    """
    recoge los datos de cantidad y longitud de los barcos
    
    :param tablero:
    """
    for i in range(CANT_PORTAVIONES):
        crearNave(LONG_PORTAVIONES)
    for i in range(CANT_SUBMARINOS):
        crearNave(LONG_SUBMARINOS)
    for i in range(CANT_DESTRUCTORES):
        crearNave(LONG_DESTRUCTORES)

#caben los barcos?
#compara el espacio de los barcos con el espacio de la cuadricula
#true si hay espacio false si no
def hayEspacio (cuadricula):
    espacioCuadricula = tablero.espacioTotal(cuadricula)
    espacioBarcos = espacioNaves()
    return True if espacioCuadricula < espacioBarcos else False


#calcula el espacio total de los barcos
def espacioNaves():
    #TODO refactorizar
    total = 0
    total = total + CANT_PORTAVIONES * LONG_PORTAVIONES
    total = total + CANT_SUBMARINOS * LONG_SUBMARINOS
    total = total + CANT_DESTRUCTORES *LONG_DESTRUCTORES
    return total


def hayHueco(posX, posY, longitud, esHorizontal, tablero):
    """
    Comprueba que se pueda colocar un barco en X,Y de longitud en el tablero
    RETURN TRUE si no hay otros barcos 
    :param posX: posicion en X donde empezar a comrpobar
    :param posy: posicion en Y donde empezar a comrpobar
    :param longitud: casisllas a comrpobar desde posX y posY
    :param esHorizontal: determina si aumentar en posX (TRUE) o posY(FALSE) las comprobaciones
    :param tablero: cuadricula donde comprobar 
    """
    sePuede = True
    for i in range(0, longitud):
        if esHorizontal:
            if tablero.getCasilla(posX + i, posY) != FONDO_TABLERO:
                sePuede = False
        else:
            if tablero.getCasilla(posX, posY + i) != FONDO_TABLERO:
                sePuede = False
    return sePuede

def asignarHueco(posX, posY, longitud, esHorizontal, tablero):
    """
    asgina los espacios a un barco en el tablero
    
    :param posX: 
    :param posY: 
    :param longitud: largo del barco
    :param esHorizontal: crece en horizontal o vertical
    :param tablero: array bidimensional a modificar
    """
    for i in range(0, longitud):
        if esHorizontal:
            tablero.setCasilla(posX + i, posY, HAY_BARCO)
        else:
            tablero.setCasilla(posX, posY + i, HAY_BARCO)

def crearNave(longitud, tablero):
    """
    marca desde una posicion aleatoria vertical u horizontal en la tablero
    y marca en longitud, si superpone busca otro sitio aleatorio
    
    :param longitud: longitud a marcar
    :param tablero: tablero a marcar
    """
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
    if hayHueco(posX, posY, longitud, horizontal, tablero):
        asignarHueco(posX, posY, longitud, horizontal, tablero)
    else:
        crearNave(longitud, tablero)


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
HAY_BARCO = "1"
FONDO_TABLERO = "~"
DIMENSION_MATRIZ_X = 10
DIMENSION_MATRIZ_Y = 10

mapa = tablero(DIMENSION_MATRIZ_X, DIMENSION_MATRIZ_Y)
mapa.fillWhitItem(FONDO_TABLERO)


#-----------probando el codigo------------------

def imprimirTablero():
    """
    imprime el tablero por pantalla
    
    :param tablero: array a imprimir
    """

    print(mapa)




imprimirTablero()