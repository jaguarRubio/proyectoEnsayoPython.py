import random
import msvcrt
import time

print("""\ncarrera de caballos""".title())
cantidadDeCaballos=int(input('\ningrese la cantidad de jinetes(1,3):'))

caja = ['bastón', 'copa  ', 'espada', 'oro   ']
jinetesCaja2 = ['bastón', 'copa  ', 'espada', 'oro   ']
print('\n🦯 bastón\n⚔ espada\n🥇 oro\n🍵 copa')
caballo1=input('selecciona un caballo:')
caballo2=random.randint(0,3)


def eleccionDeCaballo(equino):
    if equino == 'bastón' or 'baston':
        eleccion=0
    elif equino == 'copa':
        eleccion=1
    elif equino == 'espada':
        eleccion=2
    elif equino == 'oro':
        eleccion=3
    else:
        raise ValueError

    return eleccion #0baston, 1copa, 2espada, 3oro

# def maquina(njc, barril):
#     tomar=barril[njc]

#     return tomar
# tomado=maquina(caballo2, caja)

# seleccionDeComputadora=eleccionDeCaballo(tomado)
caballo1=jinetesCaja2.pop(eleccionDeCaballo(caballo1))

def participantes(cantidad, barril):
    participes=[]
    for x in range(len(barril)): #ERROR AQUÍ. ¿SOLUCIONADO?.. SOLUCIONADO
        mazoDeSeleccion = random.randint(0, (len(barril)-1))
        mutado = barril.pop(mazoDeSeleccion)
        participes.append(mutado)


    diccionario={
        1: {'cab1':participes[0]},
        2: {'cab1':participes[0], 'cab2':participes[1]},
        3: {'cab1':participes[0], 'cab2':participes[1], 'cab3':participes[2]},
    }
    return(diccionario[cantidad].values())

qalb=participantes(cantidadDeCaballos, jinetesCaja2) #1, 2, o 3 caballos. Con Elementos

losJinetes=list(qalb)
losJinetes.insert(0, caballo1)
print(losJinetes)
print('el 1ª jinete elijió:', caballo1,'\nel resto elijió:', qalb) #NOTA: ARREGLAR
meta = False

# ico2='♘ '
# ico1='♞ '

def avanzar(jinetes, barril):
    mazo=random.randint(0,3)

    for x in jinetes:
        if x == barril[mazo]:
            return(x)
    return(barril[mazo])

def hipodromo(presentes, banderaFantasma):
    establo=['♘ ', '♞ ']
#    obiWanKenowi=presentes[:]    #presentes está corrompido (con :♘)

    if banderaFantasma:
        for x in range(len(presentes)):
            caballo=random.randint(0,1) #estaba afuera del bucle for
            presentes[x]=presentes[x]+':'+(establo[caballo])#¡¿?!.. SOLUCIONADO (todos caballos blancos)

    return presentes #retorna ['oro:♘ ', 'copa:♘ ', 'espada:♞ ', 'bastón:♞ '] lista

banderaMistica=True #ver línea 102. (estaba asignado ahí)
obiWanKenowi=hipodromo(losJinetes[:], banderaMistica) #desde presentes. Una copia [:] fantasma para no alterar la lista jinetes.



def galope(listaMutada, jinete, aleatoriaCarta, banderaHueso):

    banderaHueso=False
    print(jinete, '<-tipos de elementos disponibles.')

    for x in range(len(jinete)):
        if jinete[x]==aleatoriaCarta:    #bastón.. == bastón
            
            limite=listaMutada[x].count(' ')
            if limite==11:
                print(listaMutada[x], '🏳 ⛄⛄🧉🧉🏳️  llegó')
                banderaHueso=True
                #listaMutada.remove(x) #falla al concluir.

            else:
                listaMutada[x]=list(listaMutada[x])
                numIndx=listaMutada[x].index(':')    #indice "oro':'♘ ", la lista mutada
                listaMutada[x].insert(numIndx+1, '  ')
                listaMutada[x]=''.join(listaMutada[x])
                print(listaMutada[x], ':·.')

        else:
            print(listaMutada[x])    #string 'oro:♘ '
        
    return banderaHueso

            # print(kamino)
            # print(listaMutada[x])
    
        # else:
        #     cadena=str(laListaVaAca[x])
#    return listaMutada

    # bidon=[]
    # for x in laListaVaAca: #Está corrompido (con :♘)
    #     cadena=str(x)
    #     cadena=cadena.rstrip(':♘ ') 
    #     cadena=cadena.rstrip(':♞ ')#baston . [:2]ba . [2:]ston
    #     if cadena == aleatoriaCarta:
    #         if banderaHueso:
    #             cadena+=':'
    #             cadena+='. . .'
    #         else:
    #             cadena+='. . .'
    #     print(cadena,'<-cadena, añadicion')
    #     bidon.append(cadena)
    # print(bidon, '<- bidon')
    # for z in bidon:
    #     print(z)
 
# ♞ espada\n♘

    # for x in presentes:
    #     LL=str(x+':')                      #bastón:
    #     print(LL)

c=48
print(obiWanKenowi)
print('presiona algo para avanzar turno.')
msvcrt.getch()
while c > 0:
    cartaAleatoria=avanzar(losJinetes, caja)
    print(cartaAleatoria, '<- carta aleatoria')
    meta=galope(obiWanKenowi, losJinetes, cartaAleatoria, banderaMistica)
    banderaMistica=False
    if meta:
        break
    msvcrt.getch()
    c-=1
print('presione cualquier tecla para concluir el programa')
msvcrt.getch()

#####################################################################################################################################
#     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #     #
#####################################################################################################################################

# diccionario={
#         'i5': {'ram1':'$800', 'ram2':'$900', 'ram3':'$1200'},
#         'i7': {'ram1':'$900', 'ram2':'$1000', 'ram3':'$1400'},
#         'i9': {'ram1':'$1000', 'ram2':'$1400', 'ram3':'$2000'},
#     }
# print('procesador:"i5", "i7", "i9"')
# ingresarTargeta=input('ingrese procesador:')
# print(diccionario[ingresarTargeta].items())
# ingresarRAM=input('ingrese el numero de RAM:')
# guardarSeleccion=diccionario[ingresarTargeta][ingresarRAM]
# print(diccionario[ingresarTargeta][ingresarRAM], '\ningrese la opcion 0:no extender, 1:extender. Si extiende el disco a un terabyte o no:')
# discoExtension=int(input('extensión:'))
# guardarSeleccion=int(guardarSeleccion.replace('$', ''))
# if discoExtension==1:
#    guardarSeleccion=guardarSeleccion+300
#    print('el total es:','$'+str(guardarSeleccion))
# elif discoExtension==0:
#    print('el total es:', guardarSeleccion)
# else:
#    print(None)
# print('programa finalizado')