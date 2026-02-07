class tablero:

    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
       
        self.cuadricula = []
        for x in range(alto):
            temp = []
            for y in range(ancho):
                temp.append("")
            self.cuadricula.append(temp)
        

        # dado por la ia
        #self.cuadricula = [ [ [] for _ in range(alto) ] for _ in range(ancho) ]

    #asigna el item a la casilla x,y 
    def setCasilla(self, posX, posY, item):
        self.cuadricula[posX][posY] = item
        #return cuadricula

    #return el item en la casilla
    def getCasilla(self, posX, posY):
        return self.cuadricula[posX][posY]

    #llena todos los espacios del array de item
    def fillWhitItem(self, item):
        for x in self.cuadricula:
            for y in range(len(self.cuadricula)):
                self.setCasilla(x,y,item)

    #devuelve la cantidad de casillas totales
    def espacioTotal(self):
        return len(self.cuadricula) * len(self.cuadricula[0])
    
    def getAncho(self):
        return self.ancho
    
    def getAlto(self):
        return self.alto