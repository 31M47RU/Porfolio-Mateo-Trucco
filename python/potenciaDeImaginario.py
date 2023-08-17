import tkinter as tk
def buttonText(num, seg=3):
    calculate_button.config(text=num)
    app.after((int(seg) * 1000), lambda: calculate_button.config(text="Calcular"))

def calculate_result():
    try:
        exp = int(entry_exponent.get())
        mod = exp % 4

        if   mod == 0: buttonText("1")
        elif mod == 1: buttonText("i")
        elif mod == 2: buttonText("-1")
        elif mod == 3: buttonText("-i")
    except ValueError: buttonText("Error")

app = tk.Tk()
app.title("Calculadora de Exponente de i")
app.configure(bg="#F0F0F0")

label_exponent = tk.Label(app, text="Ingrese el exponente", bg="#F0F0F0", font=("Helvetica", 12))
entry_exponent = tk.Entry(app, font=("Helvetica", 12), justify="center")
calculate_button = tk.Button(app, text="Calcular", command=calculate_result, bg="#4CAF50", fg="white", font=("Helvetica", 20), relief="flat", borderwidth=2, padx=15, pady=5, cursor="hand2")

label_exponent.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
entry_exponent.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
calculate_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)

label_exponent.config(highlightthickness=2, highlightbackground="#000000")
entry_exponent.config(highlightthickness=2, highlightbackground="#4CAF50")

app.mainloop()