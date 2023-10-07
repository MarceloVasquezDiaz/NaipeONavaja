import random

numero = random.randint(1,13)
simbolo = random.randint(1,4)
vida = 10
supongoquesi = False
supongoquesi2 = False
atributo = ''

#Cambio de numero a palabra
if simbolo == 1:
    atributo = 'diamante'
elif simbolo == 2:
    atributo = 'pica'
elif simbolo == 3:
    atributo ='corazon'
else:
    atributo = 'trebol'

#Cambio de numeros a letras
if numero == 1:
    numero = 'A'
elif numero == 11:
    numero = 'J'
elif numero == 12:
    numero = 'Q'
elif numero == 13:
    numero = 'K'
else:
    numero = str(numero)

print('Bienvenido a naipe o navaja')
print('Sacare una carta al azar debes adivinar el numero y su palo')

#Adivina el numero
while supongoquesi != True:
    numerojugador = input('Adivina el numero primero')
    if numero == numerojugador:
        print('Haz acertado el numero, ahora el atributo')
        supongoquesi = True
    else:
        print('Aguanta la apuñalada')
        vida -= 1
        print('Te quedan ' + str(vida) + ' vidas.')
        if vida == 0:
            print('Te moriste')
            break

#Adivina el palo, si es que quedan vidas
if vida >= 1:
    while supongoquesi2 != True:
        atributoJugador = input('Ahora el atributo (diamante, pica, corazon, trebol)')
        if atributo == atributoJugador:
                print('Haz acertado el atributo, la carta era ' + str(numero) + ' de ' + str(atributo))
                supongoquesi2 = True
        else:
            print('Aguanta la apuñalada')
            vida -= 1
            print('Te quedan ' + str(vida) + ' vidas.')
            if vida == 0:
                print('Te moriste')
                break
print('Fin del juego')