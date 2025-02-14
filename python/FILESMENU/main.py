import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
import subprocess
import sys

# Ruta del archivo donde se guardará la lista
data_file = "file_list.json"

def load_file_list():
    """Carga la lista de archivos desde el archivo JSON."""
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_file_list():
    """Guarda la lista de archivos en el archivo JSON."""
    with open(data_file, "w") as file:
        json.dump(file_list, file)

def add_file():
    """Permite al usuario seleccionar un archivo y agregarlo a la lista."""
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        if filepath not in file_list:
            file_list.append(filepath)
            save_file_list()
            update_listbox()
        else:
            messagebox.showinfo("Info", "El archivo ya está en la lista.")

def execute_file(filepath):
    """Ejecuta el archivo Python seleccionado en el entorno virtual si es necesario."""
    if os.path.exists(filepath):
        try:
            venv_path = get_venv_path(filepath)
            if venv_path:
                # Si se encuentra un entorno virtual, ejecutamos el archivo dentro de ese entorno
                subprocess.run([os.path.join(venv_path, "Scripts", "python.exe"), filepath], check=True)
            else:
                # Si no se encuentra un entorno virtual, verificamos si es un archivo de consola o GUI
                if is_gui_file(filepath):
                    subprocess.run([sys.executable, filepath], check=True)  # Ejecuta en la misma consola si es GUI
                else:
                    # Ejecutar el archivo en una nueva ventana de consola si es un script de consola
                    subprocess.run([sys.executable, "-i", filepath], creationflags=subprocess.CREATE_NEW_CONSOLE, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error al ejecutar el archivo:\n{e}")
    else:
        messagebox.showerror("Error", "El archivo no existe o ha sido movido.")

def get_venv_path(filepath):
    """Obtiene la ruta del entorno virtual si existe en el directorio del archivo."""
    dir_path = os.path.dirname(filepath)
    venv_path = os.path.join(dir_path, "venv")
    if os.path.isdir(venv_path):
        return venv_path
    return None

def is_gui_file(filepath):
    """Determina si el archivo usa una GUI basada en Tkinter."""
    try:
        with open(filepath, "r") as file:
            content = file.read()
        return "tkinter" in content or "Tk" in content
    except Exception as e:
        print(f"Error leyendo el archivo {filepath}: {e}")
        return False

def on_listbox_double_click(event):
    """Maneja el evento de doble clic en el Listbox."""
    selection = listbox.curselection()
    if selection:
        filepath = file_list[selection[0]]
        execute_file(filepath)

def update_listbox():
    """Actualiza el Listbox con los elementos de la lista de archivos."""
    listbox.delete(0, tk.END)
    for file in file_list:
        listbox.insert(tk.END, os.path.basename(file))

def execute_selected_file():
    """Ejecuta el archivo seleccionado en el Listbox."""
    selection = listbox.curselection()
    if selection:
        filepath = file_list[selection[0]]
        execute_file(filepath)
    else:
        messagebox.showinfo("Info", "Por favor, selecciona un archivo para ejecutar.")

# Cargar lista de archivos
file_list = load_file_list()

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Archivos Python")
root.geometry("500x400")

# Crear widgets
listbox = tk.Listbox(root, width=50, height=20)
listbox.pack(pady=10)
listbox.bind("<Double-1>", on_listbox_double_click)

add_button = tk.Button(root, text="Añadir Archivo", command=add_file)
add_button.pack(pady=5)

execute_button = tk.Button(root, text="Ejecutar Archivo", command=execute_selected_file)
execute_button.pack(pady=5)

# Actualizar Listbox al iniciar
update_listbox()

# Ejecutar la aplicación
root.mainloop()
