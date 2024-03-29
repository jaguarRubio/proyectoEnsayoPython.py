import random as ra
import msvcrt
import time

def principal(a):

    Letra=input('seleccione un caracter:')
    Letra=Letra[:1]
    Letra=' '+Letra+' '
    Eleccion=input('seleccione ser un depredador o una presa:')
    Eleccion=esOmega(Eleccion)
    segundo=caja(Eleccion)
    print(Eleccion)
    if Eleccion:
        Letra=Letra.lower()
    else:
        Letra=Letra.upper()

    mostrar(a())
    Espacio=espacio() #(['a','s'],['p','q'],['w','m'])
    for x in Espacio:
        for t in x:
            print(t+1, end=' ')
    a=accion(campo(), Espacio, Letra, segundo, Eleccion)
    print(a)
    mostrar(a)
    print('presione una tecla  para continuar:')
    msvcrt.getch()
    banderaBlanca=True

    while banderaBlanca==True:
        
        estado=comprobar(Espacio[0],Espacio[2], Eleccion)
        if estado:
            print('depredador {1} capturó la presa {0}, derrota'.format(Letra, segundo))
            banderaBlanca=False
            break

        print('¿?'*14)
        Espacio=movimiento(Espacio)
        print(Espacio)
        a=accion(campo(),Espacio,Letra, segundo, Eleccion)
        mostrar(a)
        print(Espacio, Eleccion)

        estado=comprobar(Espacio[0],Espacio[2], not Eleccion)
        if estado:
            print('depredador {0} capturó la presa {1}, victoria'.format(Letra, segundo))
            banderaBlanca=False
            break
        estado=comprobar(Espacio[0],Espacio[1],Eleccion)
        if estado:
            print('presa {0} logró huír, victoria'.format(Letra))
            banderaBlanca=False
            break

        time.sleep(0.3)
        Espacio=movimiento2(Eleccion, Espacio)
        a=accion(campo(),Espacio,Letra, segundo, Eleccion)
        mostrar(a)

        estado=comprobar(Espacio[2],Espacio[1], not Eleccion)
        if estado:
            print('presa {0} logró huír, derrota'.format(segundo))
            banderaBlanca=False
            break

    print('Juego concluido')
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
    escape, J2=[], []
    for x in range(2):
        n=ra.randint(0,11)
        escape.append(n)
        
    for x in range(2):
        n=ra.randint(0,11)
        J1.append(n)
    for x in range(2):
        n=ra.randint(0,11)
        J2.append(n)
    return J1, escape, J2

def accion(campo, lugar, caracter, j2, esOmega):
    if esOmega:
        campo[lugar[0][1]][lugar[0][0]]=caracter
        campo[lugar[2][1]][lugar[2][0]]=j2
        campo[lugar[1][1]][lugar[1][0]]='[:] '
    if not esOmega:
        campo[lugar[2][1]][lugar[2][0]]=j2
        campo[lugar[0][1]][lugar[0][0]]=caracter
        campo[lugar[1][1]][lugar[1][0]]='[:] '

    return campo


def movimiento(zona):
    sentido=input('<, >, ^, v:')
    if sentido=='<':
        zona[0][0]=zona[0][0]-1
    elif sentido=='>':
        zona[0][0]=zona[0][0]+1
    elif sentido=='v':
        zona[0][1]=zona[0][1]+1
    elif sentido=='^' or sentido=='^^':
        zona[0][1]=zona[0][1]-1
    else:
        None
    return zona

def movimiento2(esDepredador, zona):
    if esDepredador:
        if zona[0][0]<zona[2][0]:
            zona[2][0]=zona[2][0]-1
        elif zona[0][0]>zona[2][0]:
            zona[2][0]=zona[2][0]+1
            
        elif zona[0][1]<zona[2][1]:
            zona[2][1]=zona[2][1]-1
        elif zona[0][1]>zona[2][1]:
            zona[2][1]=zona[2][1]+1
    if not esDepredador:    #(['a','s'],['p','q'],['w','m'])
        if zona[1][0]<zona[2][0]:
            zona[2][0]=zona[2][0]-1
        elif zona[1][0]>zona[2][0]:
            zona[2][0]=zona[2][0]+1
            
        elif zona[1][1]<zona[2][1]:
            zona[2][1]=zona[2][1]-1
        elif zona[1][1]>zona[2][1]:
            zona[2][1]=zona[2][1]+1
            
        pass
    return zona

def caja(esDepredador):
    diacritico=('á','ä','à','â', 'é','ë','è','ê','ö','ô','ò','ó','ï','î','ì','í','ü','û','ù','ú','ç','ã','õ','ñ')#,'¨','^')
    arabe=('ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي','ء','ى','ئ','أ')
#    plus=('·','#','$','€', '%','¬','&','/',"\",'=','+','-','*','_','.',':',';','º','ª','|','@','~')
#    simbolo=('¡','!','¿','?','"',"'", '`','´','(',')','[',']','{','}')
#    numero=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    latin=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    todo=latin+diacritico+arabe
    n=ra.randint(0, len(todo))
    if esDepredador:
        return ' '+todo[n].upper()+' '
    else:
        return ' '+todo[n]+' '
        

def esOmega(valor):
    auxiliar=valor.isdigit()
    if auxiliar:
        if int(valor)==1:
            omega=False

        else:
            omega=True
    else:
        auxiliar=valor.isalpha()
        if auxiliar:
            valor=valor.lower()
            if valor=='depredador':
                omega=False

            else:
                omega=True
                
    return omega

def comprobar(var1,var2,esOmega):
    if var1==var2 and esOmega:
        return True
    else:
        return False
    






principal(campo)