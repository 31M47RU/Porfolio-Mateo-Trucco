"""
=========================
    FUNCIONES BASICAS
=========================
"""

import time

def wait(taim=0.5):
    time.sleep(taim)

def write(texto, speed=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        wait(speed)

def wInput(texto, speed=0.03):
    write(texto, speed)
    rta = input('\n--- ')
    return rta

def playAgain():
    write("\n--------------------------------------------", 0.01)
    again = wInput("\n¿Quieres jugar de nuevo? (s/n): ")
    wait()
    if again == "s" or again == "S":
        write("\nOk, vuelve a intentarlo!\n")
        write("--------------------------------------------\n", 0.01)
    else: 
        write("\n¡Gracias por jugar!\n")
        write("--------------------------------------------\n", 0.01)
        return exit()

def encuadrar(texto):
    lineas = texto.split('\n')
    max_longitud = max(len(linea) for linea in lineas)
    ancho_recuadro = max_longitud + 2

    texto_encuadrado = ''

    texto_encuadrado += '┌' + '─' * ancho_recuadro + '┐\n'
    for linea in lineas:
        texto_encuadrado += '│ ' + linea.ljust(max_longitud) + ' │\n'
    texto_encuadrado += '└' + '─' * ancho_recuadro + '┘'

    return texto_encuadrado
