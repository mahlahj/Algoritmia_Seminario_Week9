import math

def distanciaEuclidiana(destino, origen):
    distancia = math.sqrt( abs(destino[0] - origen[0])**2 + abs(destino[1] - origen[1])**2 )
    return distancia

