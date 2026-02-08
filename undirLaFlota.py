import random
from tablero import tablero 

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
def colocarBarcos():
    """
    recoge los datos de cantidad y longitud de los barcos y genera los barcos en mapa
    
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


def hayHueco(posX, posY, longitud, esHorizontal):
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
    try:
        for i in range(0, longitud):
            if esHorizontal:
                if mapa.getCasilla(posX + i, posY) != FONDO_TABLERO:
                    sePuede = False
            else:
                if mapa.getCasilla(posX, posY + i) != FONDO_TABLERO:
                    sePuede = False
    except IndexError:
        sePuede=False
    return sePuede

def asignarHueco(posX, posY, longitud, esHorizontal):
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
            mapa.setCasilla(posX + i, posY, HAY_BARCO)
        else:
            mapa.setCasilla(posX, posY + i, HAY_BARCO)

def crearNave(longitud):
    """
    marca desde una posicion aleatoria vertical u horizontal en la tablero
    y marca en longitud, si superpone busca otro sitio aleatorio
    
    :param longitud: longitud a marcar
    :param tablero: tablero a marcar
    """
    #seed de las posiciones 
    #establece un punto de inicio y si crece a la derecha o abajo segun longitud
    posX = random.randint(0, mapa.getAncho())
    posY = random.randint(0, mapa.getAlto())
    horizontal = esHorizontal()

    #arreglando las posiciones que se salen fuera de los bordes
    #empujarlos hacia dentro
    if horizontal:
        #horinzontal X
        if posX + longitud > mapa.getAncho():
            posX = (posX + longitud) - mapa.getAncho()
    else:
        #vertical Y
        if posY + longitud > mapa.getAlto():
            posY = (posY + longitud) - mapa.getAlto()

    #comprobar superposicion de barcos
    if hayHueco(posX, posY, longitud, horizontal):
        asignarHueco(posX, posY, longitud, horizontal)
    else:
        crearNave(longitud)


def esHorizontal():
    """
    decide de manera aleatoria 50% entre true o false
    """
    if random.randint(0,1) == 1:
        return True
    else:
        return False
        
#-------------------------------------------------------


#-------PEDIR DATOS AL USUARIO---------------

#LENGUAJE
LANG_ERROR_INSERT_NUMBER = "Inserta un numero valido"
LANG_ERROR_REPEAT_INSERT_NUMBER = "El numero debe de estar entre"


def pedirInt(min, max, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if min <= numero <= max:
                return numero
            else:
                print(LANG_ERROR_REPEAT_INSERT_NUMBER)
        except ValueError:
            print(LANG_ERROR_INSERT_NUMBER)




#-------CLASE JUEGO--------------


WATER = "O"
SHIP_TOCADA  = "X"
HAY_BARCO = "1"
FONDO_TABLERO = "~"
DIMENSION_MATRIZ_X = 10
DIMENSION_MATRIZ_Y = 10

#inicializar mapa de juego y colocar barcos
mapa = tablero(DIMENSION_MATRIZ_X, DIMENSION_MATRIZ_Y)
mapa.fillWhitItem(FONDO_TABLERO)
colocarBarcos()

#tablero donde juega el jugaodor
mapaJug = tablero(DIMENSION_MATRIZ_X, DIMENSION_MATRIZ_Y)
mapaJug.fillWhitItem(FONDO_TABLERO)



#-----------probando el codigo------------------

def imprimirTablero():
    """
    imprime el tablero por pantalla
    
    :param tablero: array a imprimir
    """

    
    for x in range(mapa.ancho):
        linea=""
        for y in range(mapa.alto):
            linea= linea + mapa.getCasilla(x,y)
        print(linea)


imprimirTablero()