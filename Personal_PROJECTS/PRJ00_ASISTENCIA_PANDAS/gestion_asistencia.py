# +++ BIBLIOTECAS +++
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Variable en la que recordaré la última carpeta abierta para la próxima vez que explore en la búsqueda de archivo.
ultima_carpeta = os.path.expanduser("~")

def seleccionar_fichero():
    global ultima_carpeta

    ruta = filedialog.askopenfilename (
        title = "Selecciona el fichero de asistencia",
        initialdir= ultima_carpeta,
        filetypes = [("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
    )

    if ruta:
        entry_fichero.delete(0, tk.END)
        entry_fichero.insert (0, ruta)
        # Guardamos la ruta donde abrimos para la siguiente búsqueda
        ultima_carpeta = os.path.dirname(ruta)

def procesar ():
    file = entry_fichero.get().strip()
    nombre = entry_alumno.get().strip()

    if not file:
        messagebox.showerror ("Error", "Debes seleccionar un fichero de Excel.")
        return
    if not nombre:
        messagebox.showerror ("Error", "Debes introducir el nombre del alumno.")
        return

    try:
        # Crear DataFrame con el fichero indicado.
        asistencia_df = pd.read_excel (file, sheet_name = 0, header = 4)
        asistencia_df = asistencia_df.iloc [:, 2:]
        asistencia_df = asistencia_df.loc [:, :"Dec. Resp."]
        # Crear DataFrame unicamente con los datos del estudiante indicado, normalizamos a minúsculas y buscamos por "contiene"
        patron = nombre.lower()
        asistencia_alumno = asistencia_df [asistencia_df["Estudiante"].str.lower().str.contains(patron, na= False)]
        # Mostrar mensaje de error si no hay datos del alumno y vaciar la tabla si no hay datos 
        if asistencia_alumno.empty:
            messagebox.showinfo("Resultado", f"No se encontraron registros para '{nombre}'")
        
            for i in tree.get_children():
                tree.delete(i)
            return
        # Ordenamos la información por asignatura y fecha para asegurar el orden temporal
        asistencia_alumno = asistencia_alumno.sort_values (["Asignatura", "Fecha"])
        # Nos quedamos unicamente con la última linea de cada asignatura
        asistencia_alumno = asistencia_alumno.groupby ("Asignatura", as_index= False).tail(1)

        # Seleccionar columnas de interés para mostrar
        columnas_interes = ["Estudiante", "Asignatura", "Sin Justificar", "Dec. Resp."]
        asistencia_alumno = asistencia_alumno[columnas_interes]

        # Limpiar la tabla anterior
        for i in tree.get_children():
            tree.delete(i)
        
        #Configurar columnas y cabeceras de la tabla
        tree["columns"] = columnas_interes
        for col in columnas_interes:
            tree.heading(col, text= col)
            if col == "Estudiante":
                tree.column(col, anchor= "w", width= 150)
            elif col == "Asignatura":
                tree.column(col, anchor= "w", width= 150)
            elif col == "Sin Justificar":
                tree.column(col, anchor= "center", width= 60)
            elif col == "Dec. Resp.":
                tree.column(col, anchor= "center", width= 60)

        #Insertar filas 
        for _, fila in asistencia_alumno.iterrows():
            valores = [fila[col] for col in columnas_interes]
            tree.insert ("", "end", values= valores)

    except Exception as e:
        messagebox.showerror ("Error", f"Se produjo un error:\n{e}")

def limpiar():
    for item in tree.get_children():
        tree.delete(item)
    entry_alumno.delete(0, tk.END)

''' ++++ INTERFAZ TKINTER ++++ '''
root = tk.Tk()
root.title ("UIE - INFORMACIÓN ASISTENCIA ESTUDIANTES")

# Estilo de la tabla de información de asistencia
# Cambiar fuente y color global de la tabla de información
style = ttk.Style(root)
style.theme_use ("clam")

style.configure(
    "Treeview",
    font = ("Arial", 12),
    rowheight= 22,
)

style.configure(
    "Treeview.heading",
    font = ("Arial", 12, "bold"),
    foreground = "#FFFFFF",
    background= "#FFFFFF",
)

# Permitir que la columna central (1) se expanda
root.columnconfigure (1, weight= 1)

# Línea de selección de Fichero
tk.Label(root, text= "Fichero Excel: ").grid(row=0, column= 0, padx= 5, pady= 5, sticky= "w")
entry_fichero = tk.Entry(root, width= 60)
entry_fichero.grid (row= 0, column= 1, padx= 5, pady= 5, sticky= "w")

# Botón explorar para buscar el fichero
btn_fichero = tk.Button (root, text="Explorar", command= seleccionar_fichero)
btn_fichero.grid(row= 0, column= 2, padx= 5, pady= 5)

# Línea de Nombre de Estudiante
tk.Label (root, text = "Estudiante: ").grid(row= 1, column= 0, padx= 5, pady= 5, sticky= "w")
entry_alumno = tk.Entry(root, width= 60)
entry_alumno.grid (row= 1, column= 1, padx= 5, pady= 5, columnspan= 2, sticky= "w")

# Botón solicitar información
btn_procesar = tk.Button (root, text= "Buscar...", command= procesar)
btn_procesar.grid (row= 1, column= 2, columnspan= 3, pady= 10)

frame_tabla = ttk.Frame(root)
frame_tabla.grid (row= 3, column= 0, columnspan= 3, padx= 5, pady= 5, sticky= "nsew")

root.rowconfigure (3, weight= 1)
root.columnconfigure (1, weight= 1)

tree = ttk.Treeview(frame_tabla, show= "headings")
tree.pack(fill= "both", expand= True)

# Botón Limpiar todo
btn_limpiar = tk.Button(root, text="Limpiar Todo", command=limpiar)
btn_limpiar.grid(row=4, column=0, padx=5, pady=10, sticky="w")
# Botón Cerrar
btn_cerrar = tk.Button(root, text= "Cerrar", command= root.destroy)
btn_cerrar.grid (row= 4, column= 2, padx= 5, pady= 10, sticky= "e")

# Pulsar Enter ejecutar "Solicitar Información"
root.bind ("<Return>", lambda event: procesar())
root.mainloop()



