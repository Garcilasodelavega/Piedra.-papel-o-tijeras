import random

def ordenador_decide_jugada():
   #Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    #Test para la función ordenador_decide_jugada.
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print("El ordenador eligió:", eleccion)
    print()

# Función principal
if __name__ == "__main__":
    test_ordenador_decide_jugada()

def usuario_decide_jugada():
    #Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")    
    return eleccion_usuario
