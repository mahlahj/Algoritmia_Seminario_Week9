from PySide2.QtGui import QColor
from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, Id = 0, origen_X = 0, origen_Y = 0, destino_X = 0, destino_Y = 0, velocidad = 0, rojo = 0, verde = 0, azul = 0, distancia = 0):
        self.Id = Id
        self.__origenX = origen_X
        self.__origenY = origen_Y
        self.__destinoX = destino_X
        self.__destinoY = destino_Y
        self.velocidad = velocidad
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
        self.distancia = distancia_euclidiana(origen_X, origen_Y, destino_X, destino_Y)

    def __str__(self):
        cadenas = \
            'Id: ' + str(self.Id) + '\n' +\
            'Origen en X: ' + str(self.__origenX) + '\n' +\
            'Origen en Y: ' + str(self.__origenY) + '\n' +\
            'Destino en X: ' + str(self.__destinoX) + '\n' +\
            'Destino en Y: ' + str(self.__destinoY) + '\n' +\
            'Velocidad: ' + str(self.velocidad) + '\n' +\
            'Rojo: ' + str(self.__rojo) + '\n' +\
            'Verde: ' + str(self.__verde) + '\n' +\
            'Azul: ' + str(self.__azul) + '\n' +\
            'Distancia: ' + str(self.distancia) + '\n'
        return str(cadenas)

    def __repr__(self): #to string de lista.
        return self.__str__()

    def to_dict(self):
        return {
            'id': self.Id,
	        'origen_x': self.__origenX,
	        'origen_y': self.__origenY,
	        'destino_x': self.__destinoX,
	        'destino_y': self.__destinoY,
	        'velocidad': 0,
	        'red': self.__rojo,
	        'green': self.__verde,
	        'blue': self.__azul
        }

    def getId(self):
        return str(self.Id)
    
    def getOrigen(self):
        return str( "(" + str(self.__origenX) + ", " + str(self.__origenY) + ")")
    
    def getDestino(self):
        return str("(" + str(self.__destinoX) + ", " + str(self.__destinoY) + ")")
    
    def getVelocidad(self):
        return str(self.velocidad)
    
    def getColor(self):
        return str("(" + str(self.__rojo) + ", " + str(self.__verde) + ", " + str(self.__azul) + ")")
    
    def getDistancia(self):
        return str(self.distancia)

    def color(self):
        return QColor(self.__rojo, self.__verde, self.__azul)
    
    def Xi(self):
        return self.__origenX
    
    def Yi(self):
        return self.__origenY

    def Xf(self):
        return self.__destinoX

    def Yf(self):
        return self.__destinoY