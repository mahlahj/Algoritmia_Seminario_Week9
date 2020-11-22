from particula import Particula
import json

class Organizador:
    def __init__(self):
        self.organizador = []

    def agregar_inicio(self, part):
        self.organizador.insert(0,part)

    def agregar_final(self, part):
        self.organizador.append(part)

    def mostrar(self):
        cadenas = ""
        for particula in self.organizador:
            cadenas += str(particula) + "\n"
        return cadenas
    
    def guardar(self):
        cadenas = []
        for particula in self.organizador:
            cadenas.append(particula.to_dict())
        return cadenas
    
    def get(self, archivo):
        for p in archivo:
            particula = Particula(p['id'], p['origen_x'], p['origen_y'], p['destino_x'], p['destino_y'], p['velocidad'], p['red'], p['green'], p['blue'])
            self.agregar_final(particula)
            