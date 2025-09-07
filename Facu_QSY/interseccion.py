lA = int(input("Largo Vector A: "))
vA = [] * lA

lB = int(input("Largo Vector B: "))
vB = [] * lB

mA = 0

for i in range(lA):
    n = int(input(f"Ingrese el valor {i} para el vector A: "))
    if n > mA: mA = n
    vA.append(n)

for i in range(lB):
    n = int(input(f"Ingrese el valor {i} para el vector B: "))
    vB.append(n)

inter = []
for i in range(lA):
    for k in range(lB):
        if vA[i] == vB[k]: inter.append(vA[i])
            
if mA in vB: print(f"""
                    La interseccion es {str(inter).replace('[','').replace(']','')}
                    
                    El mayor de A: ({mA}) si esta en la inetrseccion
                    """)
else: print(f"""
                    La interseccion es {str(inter).replace('[','').replace(']','')}
                    
                    El mayor de A: ({mA}) si esta en la inetrseccion
                    """)
