import random
def adivina_numero(x,numero_generado):
    if x > numero_generado:
        print('El número que has ingresado es mayor que el número que deseas adivinar')
    elif x < numero_generado:
        print('El número que has ingresado es menor que el número que deseas adivinar')
    else:
        print('El número que has adivinado es correcto. Felicidades')
        return True
    print('Reintente')
    return False

def proceso_juego():
    verdad = False
    numero_gen = random.randrange(0,11)
    print('Adivina el número en el rango de 0 a 10')
    while verdad == False:
        x = input('Ingrese el número: ')
        if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
            verdad = adivina_numero(int(x),numero_gen)
        else:
            print('Este número no es válido')
