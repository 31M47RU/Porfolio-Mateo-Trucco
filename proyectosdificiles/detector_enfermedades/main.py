"""
-------------------------------------------------------------------------------
DETECTOR DE ENFERMEDADES
-------------------------------------------------------------------------------
Este script es un detector de enfermedades que utiliza un modelo de aprendizaje automático
para predecir la presencia de enfermedadesen pacientes basándose en sus síntomas.
-------------------------------------------------------------------------------
"""

import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Frame")

frame = tk.Frame(root, bg="lightblue", bd=2, relief="groove")
frame.pack(padx=10, pady=10)

label = tk.Checkbutton(frame, text="Este es un label dentro del Frame", bg="lightblue")
label.pack(padx=5, pady=5)

if label:
    label.configure(bg="black")
else:
    label.configure(bg="white")

root.mainloop()
