import os

def combine_files(folder_path="all/", output_file="compilado.py"):
    combined_content = ""

    # Recorre todos los archivos en la carpeta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Lee el contenido del archivo y guarda en una variable con el nombre del archivo
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            variable_name = os.path.splitext(filename)[0]  # Usa el nombre del archivo sin extensión como variable

            # Encierra el contenido entre comillas y agrega la variable al contenido combinado
            combined_content += f"{variable_name} = '''{file_content}'''\n"

    # Escribe el contenido combinado en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(combined_content)

if __name__ == "__main__":
    combine_files()

    # Después de combinar los archivos, evalúa el contenido
    # import compilado
