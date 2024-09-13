import tkinter as tk  # Importamos la librería Tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importamos messagebox para mostrar mensajes emergentes

# Definir la clase de la aplicación
class App:
    def __init__(self, app):
        """
        Constructor de la clase App, donde se configura la interfaz gráfica.
        Se definen todos los componentes de la ventana principal.
        """
        # Guardamos la referencia de la ventana principal
        self.app = app
        # Título de la ventana
        self.app.title("Aplicación GUI - Gestión de Datos")
        # Tamaño de la ventana principal
        self.app.geometry('400x400')

        # Etiqueta que le dice al usuario qué hacer (ingresar un dato)
        self.label = tk.Label(self.app, text="Ingrese un dato:")
        self.label.pack(pady=10)  # Añadimos la etiqueta con un margen vertical de 10 píxeles

        # Campo de texto donde el usuario ingresará un dato
        self.entry = tk.Entry(self.app, width=40)  # El campo tiene un ancho de 40 caracteres
        self.entry.pack(pady=10)  # Añadimos el campo de texto con margen vertical

        # Botón para agregar el dato a la lista
        self.btn_agregar = tk.Button(self.app, text="Agregar", command=self.agregar_dato)
        self.btn_agregar.pack(pady=5)  # Añadimos el botón con un margen vertical de 5 píxeles

        # Botón para limpiar la lista de datos
        self.btn_limpiar = tk.Button(self.app, text="Limpiar", command=self.limpiar_lista)
        self.btn_limpiar.pack(pady=5)  # Añadimos el botón con un margen vertical de 5 píxeles

        # Lista donde se mostrarán los datos que el usuario agregue
        self.lista = tk.Listbox(self.app, width=50, height=10)  # Lista de ancho 50 y altura 10 elementos
        self.lista.pack(pady=10)  # Añadimos la lista con margen vertical de 10 píxeles

        # Botón para mostrar un mensaje de prueba
        self.btn_mensaje = tk.Button(self.app, text="Mostrar mensaje", command=self.mostrar_mensaje)
        self.btn_mensaje.pack(pady=20)  # Añadimos el botón con margen vertical de 20 píxeles

    # Función que se ejecuta cuando el usuario hace clic en el botón "Agregar"
    def agregar_dato(self):
        """
        Obtiene el dato del campo de texto y lo añade a la lista si no está vacío.
        Si el campo está vacío, muestra una advertencia.
        """
        dato = self.entry.get()  # Obtener el texto ingresado en el campo de texto
        if dato:  # Verificamos si el campo no está vacío
            self.lista.insert(tk.END, dato)  # Añadimos el dato al final de la lista
            self.entry.delete(0, tk.END)  # Limpiamos el campo de texto
        else:
            # Mostrar advertencia si el campo de texto está vacío
            messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

    # Función que se ejecuta cuando el usuario hace clic en el botón "Limpiar"
    def limpiar_lista(self):
        """
        Elimina todos los elementos de la lista.
        """
        self.lista.delete(0, tk.END)  # Borrar todos los elementos de la lista

    # Función que se ejecuta cuando el usuario hace clic en el botón "Mostrar mensaje"
    def mostrar_mensaje(self):
        """
        Muestra un mensaje emergente de prueba.
        """
        messagebox.showinfo("Mensaje", "Hola, esto es un mensaje de prueba.")

# Crear la ventana principal de la aplicación
app = tk.Tk()

# Crear una instancia de la clase App y pasar la ventana 'app' como parámetro
mi_app = App(app)

# Iniciar el bucle principal de la interfaz gráfica
app.mainloop()
