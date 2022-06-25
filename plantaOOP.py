class plantula():
    def __init__(self, nombre, alimentacion, terreno, color):
        self.sitiadoEnElSustrato=True
        fotosintesis=False
        self.crecimiento=True
        self.nombre=self.nombre
        self.alimentacion=self.alimentacion
        self.terreno=self.terreno
        self.color=self.color

    def generVegetal(self):
        self.fotosintesis=True
    
    def estado(self):
        if self.sitiadoEnElSustrato:
            S = 'Está en el sustrato'
        elif self.sitiadoEnElSustrato:
            S = 'No está en el sustrato'
        else:
            S = 'Desconocido'
        if self.fotosintesis:
            F = 'Está haciendo fotosintesis'
        elif self.fotosintesis:
            F = 'No está haciendo fotosintesis'
        else:
            F = 'Desconocido'
        if self.crecimiento:
            C = 'Está creciendo'
        elif self.creciendo:
            C = 'No está creciendo'
        else:
            C = 'Desconocido'
        print('El nombre es:', self.nombre, '\nLa alimentacion es:', self.alimentacion, '\nEl terreno es:',
        self.terreno, '\nEl color es:', self.color, '\n\n Otras anotaciones:', '\nSustrato:', S,
        '\nFotisintesis', F, '\nCrecimiento', C)
    

class flor(plantula):
    def petalos(self, abrirPetalos):
        self.estadoPetalos=abrirPetalos
        if (self.estadoPetalos):
            return 'petalos abiertos'
        else:
            return 'petalos cerrados'

class musgo(plantula):
    def microEspora(self, EsporaLanzar):
        self.esporaLanzada=EsporaLanzar
        if (self.esporaLanzada):
            return 'espora arrojada'
        else:
            return 'espora quieta'

class arbol(plantula):
    def generarResina(self, Res):
        self.resina=Res
        if (self.resina):
            return 'resina activada'
        else:
            return 'resina desactivada'