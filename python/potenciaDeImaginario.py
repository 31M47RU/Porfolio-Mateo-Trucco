import tkinter as tk
from tkinter import messagebox

def buttonText(num, seg=3):
    calculate_button.config(text=num)
    app.after((int(seg) * 1000), lambda: calculate_button.config(text="Calcular"))

def calculate_result():
    exp = entry_exponent.get()

    try:
        mod = int(exp) % 4

        if   mod == 0:
            buttonText("1")
        elif mod == 1:
            buttonText("i")
        elif mod == 2:
            buttonText("-1")
        elif mod == 3:
            buttonText("-i")

    except ValueError:
        buttonText("Error")

app = tk.Tk()
app.title("Calculadora de Exponente de i")
app.configure(bg="#F0F0F0")

label_exponent = tk.Label(app, text="Ingrese el exponente", bg="#F0F0F0", font=("Helvetica", 12))
entry_exponent = tk.Entry(app, font=("Helvetica", 12), justify="center")
calculate_button = tk.Button(app, text="Calcular", command=calculate_result, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat", borderwidth=2, padx=15, pady=5, cursor="hand2")

label_exponent.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
entry_exponent.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
calculate_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)

entry_exponent.config(highlightthickness=2, highlightbackground="#4CAF50")

app.mainloop()


# import time

# def slip(taim):
#     time.sleep(taim)

# ask1 = input("\nQuerés el resultado del exponente de i? [Si] [No]:\n--- ")
# slip(0.5)

# while True:
#     try:
#         if ask1 == "si" or ask1 == "Si":
#             exp = input("\nIngrese el exponente\n--- ")
#             mod = int(exp) % 4
#             slip(0.5)

#             if   mod == 0: print(f"\nexponente: | {mod} |\n\nR E S U L T A D O: || 1 ||")
#             elif mod == 1: print(f"\nexponente: | {mod} |\n\nR E S U L T A D O: || i ||")
#             elif mod == 2: print(f"\nexponente: | {mod} |\n\nR E S U L T A D O: || -1 ||")
#             elif mod == 3: print(f"\nexponente: | {mod} |\n\nR E S U L T A D O: || -i ||")

#         elif ask1 == "no" or ask1 == "No":
#             exp = input("\nIngrese el exponente\n--- ")
#             mod = int(exp) % 4
#             slip(0.5)

#             if   mod == 0: print(f"\nR E S U L T A D O: || 1 ||")
#             elif mod == 1: print(f"\nR E S U L T A D O: || i ||")
#             elif mod == 2: print(f"\nR E S U L T A D O: || -1 ||")
#             elif mod == 3: print(f"\nR E S U L T A D O: || -i ||")
#         else: ask1 = "si"

#     except ValueError as er:
#         slip(0.5), print("\n\n|| ERROR ||\n\n* Pusiste letras\n* Pusiste las I\n* Sos medio pichiruchi\n"), slip(0.5)