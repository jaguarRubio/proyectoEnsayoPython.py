
import random

import msvcrt


def maq():
    caja=['piedra', 'papel', 'tijera']
    dal=random.randint(0,2)
    return caja[dal]

ingrese=input('ingrese: ')
ola_k_ace = maq()
if ingrese == 'piedra' and ola_k_ace == 'papel':
    final=0
elif ingrese == 'piedra' and ola_k_ace == 'tijera':
    final=1
elif ingrese == 'piedra' and ola_k_ace == 'piedra':
    final=2

elif ingrese == 'papel' and ola_k_ace == 'tijera':
    final=0
elif ingrese == 'papel' and ola_k_ace == 'piedra':
    final=1
elif ingrese == 'papel' and ola_k_ace == 'papel':
    final=2

elif ingrese == 'tijera' and ola_k_ace == 'piedra':
    final=0
elif ingrese == 'tijera' and ola_k_ace == 'papel':
    final=1
elif ingrese == 'tijera' and ola_k_ace == 'tijera':
    final=2
else:
    raise ValueError
if final==1:
    print( 'gano')
elif final==0:
    print( 'derrota')
elif final==2:
    print( 'empate')
else:
    print( '¿?')



print('la máquina elijió:',ola_k_ace)
print('presione cualquier tecla para concluir el programa.')
msvcrt.getch()