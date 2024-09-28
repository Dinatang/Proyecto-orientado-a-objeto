import tkinter as tk
from tkinter import messagebox, Listbox
import pickle

# Función para añadir una nueva tarea
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea and tarea not in lista_tareas.get(0, tk.END):  # Evitar duplicados
        lista_tareas.insert(tk.END, tarea)  # Añadir la tarea a la lista
        entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, escribe una tarea válida o evita duplicados.")

# Función para marcar una tarea como completada
def completar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(tk.END, tarea + " (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

# Función para añadir tarea al presionar Enter
def enter_presionado(event):
    agregar_tarea()

# Función para guardar las tareas en un archivo
def guardar_tareas():
    with open("tareas.pkl", "wb") as archivo:
        pickle.dump(lista_tareas.get(0, tk.END), archivo)

# Función para cargar las tareas desde un archivo
def cargar_tareas():
    try:
        with open("tareas.pkl", "rb") as archivo:
            tareas = pickle.load(archivo)
            for tarea in tareas:
                lista_tareas.insert(tk.END, tarea)
    except FileNotFoundError:
        print("No se encontró el archivo de tareas guardadas.")
    except Exception as e:
        print(f"Ocurrió un error al cargar las tareas: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.grid(row=0, column=0, padx=10, pady=10)
entrada_tarea.bind("<Return>", enter_presionado)

# Botón para añadir tarea
boton_añadir = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_añadir.grid(row=0, column=1, padx=10, pady=10)

# Listbox para mostrar las tareas
lista_tareas = Listbox(ventana, width=50, height=10)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar como completada
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
boton_completar.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

# Botón para guardar las tareas
boton_guardar = tk.Button(ventana, text="Guardar Tareas", command=guardar_tareas)
boton_guardar.grid(row=3, column=0, padx=10, pady=10)

# Botón para cargar las tareas
boton_cargar = tk.Button(ventana, text="Cargar Tareas", command=cargar_tareas)
boton_cargar.grid(row=3, column=1, padx=10, pady=10)

# Cargar las tareas guardadas al iniciar la aplicación
cargar_tareas()

# Iniciar el loop de la aplicación
ventana.mainloop()
