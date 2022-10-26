import random as ra
import msvcrt

def principal(a):

    Letra=input('seleccione un caracter:')
    mostrar(a())
    Espacio=espacio() #(['a','s'],['p','q'])
    for x in Espacio:
        for t in x:
            print(t+1, end=' ')
    a=accion(campo(), Espacio, Letra)
    print(a)
    mostrar(a)
    algo=input('presione la barra espaciadora para continuar:')
    banderaBlanca=True
    while banderaBlanca==True:
        Espacio=movimiento(Espacio)
        print(Espacio)
        a=accion(campo(),Espacio,Letra)
        mostrar(a)
        if Espacio[0]==Espacio[1]:
            banderaBlanca=False
    print('Juego concluido, tú has llegado')

    pass

def campo():
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11=[],[],[],[],[],[],[],[],[],[],[],[]
    tuplaLista=(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)
    for x in tuplaLista:
        for z in range(12):
            x.append(' ö ')

    return tuplaLista

def mostrar(kampo):
    for x in kampo:
        print(''.join(x))
    pass

def espacio():
    J1=[]
    escape=[]
    for x in range(2):
        n=ra.randint(0,11)
        escape.append(n)
        
    for x in range(2):
        n=ra.randint(0,11)
        J1.append(n)
    return J1, escape

def accion(campo, lugar, caracter):
    campo[lugar[0][1]][lugar[0][0]]=caracter
    campo[lugar[1][1]][lugar[1][0]]='[·] '

    return campo


def movimiento(zona):
    sentido=input('<, >, ^, v:')
    if sentido=='<':
        zona[0][0]=zona[0][0]-1
    elif sentido=='>':
        zona[0][0]=zona[0][0]+1
    elif sentido=='v':
        zona[0][1]=zona[0][1]+1
    elif sentido=='^':
        zona[0][1]=zona[0][1]-1
    else:
        pass
    return zona


principal(campo)
