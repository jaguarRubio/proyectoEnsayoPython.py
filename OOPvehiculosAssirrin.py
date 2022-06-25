class vehiculosDeAsirrin():
    def __init__(self, nombre, desplazamiento):

        self.nombre=nombre
        self.desplazamiento=desplazamiento
        self.encendido=False
        self.frenando=False
        self.acelerando=False
    
    def acelerar(self):
        self.acelerando=True
    
    def frenar(self):
        self.frenando=True
    
    def encender(self):
        self.encendido=True
    
    def decirEstado(self):
        print ('\nInformación:', '\nnombre:', self.nombre, '\ndesplazamiento:', self.desplazamiento,
        '\nencedido:', self.encendido, '\nfrenando:', self.frenando, '\nacelerando:', self.acelerando)

class meñul(vehiculosDeAsirrin):
    flotando=False
    
    def decirEstado(self):
        print ('\nInformación:', '\nnombre:', self.nombre, '\ndesplazamiento:', self.desplazamiento,
        '\nencedido:', self.encendido, '\nfrenando:', self.frenando, '\nacelerando:', self.acelerando,
        '\nflotando:', self.flotando)

meñulDeAsalto = meñul('meñulDeAsalto', 'flotante')
meñulDeAsalto.decirEstado()
