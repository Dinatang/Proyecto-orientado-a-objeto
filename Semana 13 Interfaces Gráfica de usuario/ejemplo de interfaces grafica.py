import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Aplicación GUI - Gestión de Datos")  # Establecer el título de la ventana

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()  # Obtener el texto ingresado en el campo de texto
    if dato:  # Verificar si el campo no está vacío
        lista.insert(tk.END, dato)  # Agregar el dato al final de la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto una vez agregado el dato
    else:
        # Mostrar advertencia si no se ingresó ningún dato
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

# Función para limpiar la lista de datos
def limpiar_lista():
    lista.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Etiqueta para guiar al usuario a ingresar datos
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=10)  # Añadir la etiqueta a la ventana con margen vertical

# Campo de texto donde el usuario ingresará el dato
entry = tk.Entry(root, width=40)  # El campo tiene un ancho de 40 caracteres
entry.pack(pady=10)  # Añadir el campo de texto con margen vertical

# Botón para agregar el dato a la lista
btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)  # Añadir el botón a la ventana con margen vertical

# Botón para limpiar la lista de datos
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)  # Añadir el botón a la ventana con margen vertical

# Lista donde se mostrarán los datos agregados
lista = tk.Listbox(root, width=50, height=10)  # La lista tiene un ancho de 50 y altura de 10 elementos visibles
lista.pack(pady=10)  # Añadir la lista a la ventana con margen vertical

# Iniciar el loop principal de la ventana para que la interfaz sea interactiva
root.mainloop()
