"""
!------------------------------------------------------------------------------------------
*** Trabajo Práctico N°3 ***
!------------------------------------------------------------------------------------------
"""



"""
!------------------------------------------------------------------------------------------
*** PUNTO 1: ***
TODO: | Dado un vector con N números, determinar la cantidad de pares y sumarlos,       |
TODO: | también contar la cantidad de impares y multiplicarlos, mostrar los resultados. |
!------------------------------------------------------------------------------------------
"""
class PUNTO1():
    @staticmethod
    
    def ejecutar():
        while True:
            try:
                n = int(input("\n|||   PUNTO 1   |||\n\nIngrese el tamaño de la lista:\n---  "))
                if n < 0: break
                
                pares = 0
                impares = 0 
                
                sumPares = 0
                mulImpares = 1

                vector = []
                
                for i in range(n):
                    num = int(input(f"\n· Ingrese el numero {i} del vector:\n---  "))
                    vector.append(num)
                    
                    if num % 2 == 0: pares += 1; sumPares += num 
                    else: impares += 1; mulImpares *= num
                
                print(f"""
------------------------------------------------------------------------------------------
· Vector Original
| {str(vector).replace("[", "").replace("]", "")} |

·  La suma de los {pares} numeros pares es | {sumPares} |

·  La multiplicacion de los {impares} numeros impares es | {mulImpares} |
------------------------------------------------------------------------------------------
                    """)
            except ValueError: print("\n\n||| ERROR |||\nPONEME UN NUMERO PORFAAA\n\n")



"""
!------------------------------------------------------------------------------------------
*** PUNTO 2 ***
TODO: | Dada una lista de N números, generar un vector con los números que sean capicúas. |
!------------------------------------------------------------------------------------------
"""

class PUNTO2():
    @staticmethod

    def ejecutar():
        def RevesNumero(aux):
            #* cantidad de digitos, ultdigit * (10 ^ digitos - 1), dgt -= 1
            dgt = 0
            num = aux
            nRev = 0
            while aux > 0:
                if aux % 10:
                    dgt += 1
                    aux //= 10
            while (dgt) > 0: #*  65
                ultDgt = num % 10
                nRev += ultDgt * (10**(dgt-1))
                num //= 10
                dgt -= 1
            return nRev

        while True:
            try:
                n = int(input("\n|||   PUNTO 2   |||\n\nIngrese el tamaño de la lista:\n---  "))
                if n < 0: break
                
                vector = []
                
                for i in range(n):
                    num = int(input(f"· Ingrese el numero {i} de la lista:\n---  "))
                    if RevesNumero(num) == num: vector.append(num)
                print(f"""
------------------------------------------------------------------------------------------
· De los numeros que me pasaste, estos son capicua:
| {str(vector).replace("[", "").replace("]", "")} |
------------------------------------------------------------------------------------------
                    """)    
            except ValueError: print("\n\n||| ERROR |||\nPONEME UN NUMERO PORFAAA\n\n")



"""
!------------------------------------------------------------------------------------------
*** PUNTO 3 ***
TODO: | Obtener los k primeros términos de la sucesión de Fibonacci                     |
!------------------------------------------------------------------------------------------
"""

class PUNTO3():
    def ejecutar():
        # numero actual + anterior
        try:
            k = int(input("\nIngrese la cantidad de terminos de la sucesion de Fibonacci:\n---  ")) - 2
            def Fibonacci(n):
                n0 = 0
                n1 = 1
                vector = [0, 1]
                for i in range(n):
                    vector.append(n0+n1)
                    nA0 = n0
                    nA1 = n1
                    n0 = nA1
                    n1 = nA0 + nA1
                return vector

            print("-" * 90)
            for i in range(k):
                print(Fibonacci(k)[i])
            print("-" * 90)
                    
                      
        except ValueError: print("\n\n||| ERROR |||\nPONEME UN NUMERO PORFAAA\n\n")



"""
!------------------------------------------------------------------------------------------
*** PUNTO 4 ***
TODO: | Dado dos vectores A y B que contienen cada uno un número natural positivo, se   |
TODO: | pide componer un nuevo número                                                   |
!------------------------------------------------------------------------------------------
"""

class PUNTO4():
    def ejecutar():
        try:
            vA = [int(input("\nIngrese un numero para el primer vector:\n---  "))]
            vB = [int(input("\nIngrese un numero para el segundo vector:\n---  "))]

            nAB = str(vA[0]) + str(vB[0])
            
            print(f"\nEl Numero compuesto por estos dos es:\n| {nAB} |\n")
        except ValueError: print("\n\n||| ERROR |||\nPONEME UN NUMERO PORFAAA\n\n")



"""
!------------------------------------------------------------------------------------------
*** PUNTO 5 ***
TODO: | Dados dos vectores de números A y B, indicar si el mayor de A se encuentra en B |
!------------------------------------------------------------------------------------------
"""

class PUNTO5():
    def ejecutar():
        try:
            lA = int(input("Ingese el largo del vector A:\n---  "))
            lB = int(input("Ingese el largo del vector B:\n---  "))
            vA, vB = [], []

            mA = 0
            mB = 0
            
            for i in range(lA):
                n = int(input(f"Ingrese el numero {i} del vector A:\n---  "))
                vA.append(n)
                if n > mA: mA = n
                
            for i in range(lB):
                n = vB.append(int(input(f"Ingrese el numero {i} del vector B:\n---  ")))
            
            if mA in vB: print(f"\nEl numero mayor de A: | {mA} |, se encuentra en B: | {str(vB).replace('[','').replace(']','')} |")
            else: print(f"\nEl numero mayor de A: | {mA} |, NO se encuentra en B: | {str(vB).replace('[','').replace(']','')} |")
            
        except ValueError: print("\n\n||| ERROR |||\nPONEME UN NUMERO PORFAAA\n\n")



"""
!------------------------------------------------------------------------------------------
*** PUNTO 5 ***
TODO: | Dados 3 dígitos, generar y mostrar el mayor número natural que puede escribirse |
TODO: | con ellos.                                                                      |
!------------------------------------------------------------------------------------------
"""

class PUNTO6():
    def ejecutar():
        try:
            d1 = int(input("\nIngrese el primer digito:\n---  "))
            d2 = int(input("\nIngrese el segundo digito:\n---  "))
            d3 = int(input("\nIngrese el tercer digito:\n---  "))
            
            def sum(d1,d2,d3):
                total = (d1*100)+(d2*10)+(d3)
                print(f"\nEl mayor numero natural que se puede formar con estos numeros: {d3,d1,d2}, es\n| {total} |\n")
            
            if d1>d2>d3:   sum(d1,d2,d3)            
            elif d1>d3>d2: sum(d1,d3,d2)
            elif d2>d1>d3: sum(d2,d1,d3)
            elif d2>d3>d1: sum(d2,d3,d1)
            elif d3>d1>d2: sum(d3,d1,d2)
            elif d3>d2>d1: sum(d3,d2,d1)
            else: print("easter egg bro")
            
        except ValueError: print("\n\n||| ERROR |||\nPONEME UN NUMERO PORFAAA\n\n")






def SelectorPunto():
    puntos_disponibles = {nombre: clase for nombre, clase in globals().items() if nombre.startswith("PUNTO") and hasattr(clase, "ejecutar")}
    nombres_ordenados = sorted(puntos_disponibles.keys())

    print("-" * 90)
    print("\nSeleccione el punto para ejecutar:")
    for i, nombre in enumerate(nombres_ordenados, start=1):
        print(f"{i} - {nombre}")
    print("-" * 90)

    opcion = input("\nIngrese el número del punto:\n---  ")
    try:
        indice = int(opcion) - 1
        nombre_clase = nombres_ordenados[indice]
        puntos_disponibles[nombre_clase].ejecutar()
    except (IndexError, ValueError):
        print("\n\n||| INVALIDO |||\n\n")

if __name__ == "__main__":
    SelectorPunto()