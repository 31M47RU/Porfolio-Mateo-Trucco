import tkinter as tk
from tkinter import ttk, messagebox

def calcular_precio():
    try:
        precio_original = float(entry_precio.get())
        porcentaje_impuestos = float(entry_impuesto.get())

        precio_final = precio_original * (1 + porcentaje_impuestos / 100)

        label_resultado.config(text=f"Precio final: ${precio_final:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Impuestos")
ventana.geometry("400x300")
ventana.resizable(False, False)
ventana.config(bg="#2c3e50")

# Títulos
titulo = tk.Label(ventana, text="Calculadora de Impuestos", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
titulo.pack(pady=10)

# Entrada para el precio original
frame_precio = tk.Frame(ventana, bg="#2c3e50")
frame_precio.pack(pady=10)
label_precio = tk.Label(frame_precio, text="Precio original ($):", font=("Arial", 12), bg="#2c3e50", fg="white")
label_precio.pack(side="left", padx=5)
entry_precio = ttk.Entry(frame_precio, font=("Arial", 12))
entry_precio.pack(side="left")

# Entrada para el porcentaje de impuestos
frame_impuesto = tk.Frame(ventana, bg="#2c3e50")
frame_impuesto.pack(pady=10)
label_impuesto = tk.Label(frame_impuesto, text="Impuestos (%):", font=("Arial", 12), bg="#2c3e50", fg="white")
label_impuesto.pack(side="left", padx=5)
entry_impuesto = ttk.Entry(frame_impuesto, font=("Arial", 12))
entry_impuesto.pack(side="left")

# Botón para calcular
boton_calcular = ttk.Button(ventana, text="Calcular", command=calcular_precio)
boton_calcular.pack(pady=20)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#1abc9c")
label_resultado.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
