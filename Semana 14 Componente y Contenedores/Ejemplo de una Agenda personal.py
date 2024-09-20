# Una Aplicación de Agenda Personal
import tkinter as tk  # Importa la librería tkinter para crear la GUI
from tkinter import messagebox, ttk  # Importa componentes de tkinter
import pickle  # Importa la librería pickle para guardar y cargar eventos

# Ruta del archivo donde se guardarán los eventos
ARCHIVO_EVENTOS = "eventos.pickle"


# Función para agregar un evento
def agregar_evento():
    # Obtiene los valores de fecha, hora y descripción desde las entradas
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Verifica que todos los campos estén llenos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
        return

    # Inserta el nuevo evento en el TreeView
    tree.insert("", tk.END, values=(fecha, hora, descripcion))

    # Limpia los campos de entrada
    entrada_fecha.delete(0, tk.END)
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)

    # Guarda los eventos en el archivo
    guardar_eventos()


# Función para eliminar el evento seleccionado
def eliminar_evento():
    # Obtiene el evento seleccionado
    selected_item = tree.selection()

    # Verifica si hay un evento seleccionado
    if not selected_item:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")
        return

    # Confirma la eliminación del evento
    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
    if respuesta:
        tree.delete(selected_item)  # Elimina el evento del TreeView
        # Guarda los eventos en el archivo
        guardar_eventos()


# Función para guardar los eventos en un archivo
def guardar_eventos():
    eventos = []  # Lista para almacenar los eventos
    # Itera sobre los eventos en el TreeView
    for item in tree.get_children():
        eventos.append(tree.item(item, "values"))  # Agrega los eventos a la lista
    # Guarda la lista de eventos en un archivo usando pickle
    with open(ARCHIVO_EVENTOS, "wb") as archivo:
        pickle.dump(eventos, archivo)


# Función para cargar los eventos desde un archivo
def cargar_eventos():
    try:
        # Intenta abrir el archivo y cargar los eventos
        with open(ARCHIVO_EVENTOS, "rb") as archivo:
            eventos = pickle.load(archivo)  # Carga la lista de eventos
            # Inserta cada evento en el TreeView
            for evento in eventos:
                tree.insert("", tk.END, values=evento)
    except FileNotFoundError:
        pass  # Si el archivo no existe, no hace nada


# Crear la ventana principal
root = tk.Tk()  # Inicializa la ventana principal
root.title("Agenda Personal Universitaria")  # Establece el título de la ventana
root.geometry("600x400")  # Define el tamaño de la ventana
root.configure(bg="#FFB6C1")  # Establece el color de fondo rosado

# Estilo para los componentes del TreeView
estilo = ttk.Style()  # Crea un nuevo estilo
estilo.configure("Treeview",
                 font=("Comic Sans MS", 10),  # Fuente para el TreeView
                 background="#FFB6C1",  # Color de fondo para el TreeView
                 fieldbackground="#FFB6C1"  # Color de fondo de las celdas
                 )
estilo.configure("Treeview.Heading",
                 font=("Comic Sans MS", 12, "bold")  # Fuente para los encabezados
                 )
estilo.configure("Treeview.Cell",
                 anchor='center',  # Centra el texto en las celdas
                 )

# Crear y organizar los frames para la interfaz
frame_lista = tk.Frame(root, bg="#FFB6C1")  # Frame para la lista de eventos
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

frame_entrada = tk.Frame(root, bg="#FFB6C1")  # Frame para campos de entrada
frame_entrada.pack(pady=10, padx=10, fill=tk.X)

frame_acciones = tk.Frame(root, bg="#FFB6C1")  # Frame para botones de acción
frame_acciones.pack(pady=10, padx=10, fill=tk.X)

# Crear el TreeView para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")  # Crea el TreeView
tree.heading("Fecha", text="Fecha")  # Establece el encabezado de la columna de fecha
tree.heading("Hora", text="Hora")  # Establece el encabezado de la columna de hora
tree.heading("Descripción", text="Descripción del Evento")  # Establece el encabezado de la columna de descripción
tree.column("Fecha", anchor='center')  # Centra el texto en la columna de fecha
tree.column("Hora", anchor='center')  # Centra el texto en la columna de hora
tree.column("Descripción", anchor='center')  # Centra el texto en la columna de descripción
tree.pack(fill=tk.BOTH, expand=True)  # Muestra el TreeView

# Crear campos de entrada con etiquetas centradas
etiqueta_fecha = tk.Label(frame_entrada, text="Fecha (dd-mm-aaaa):", bg="#FFB6C1", fg="black",
                          font=("Comic Sans MS", 10, "bold"))  # Etiqueta para la fecha
etiqueta_fecha.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)  # Coloca la etiqueta en la cuadrícula
entrada_fecha = tk.Entry(frame_entrada)  # Campo de entrada para la fecha
entrada_fecha.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)  # Coloca el campo en la cuadrícula

etiqueta_hora = tk.Label(frame_entrada, text="Hora (HH:MM):", bg="#FFB6C1", fg="black",
                         font=("Comic Sans MS", 10, "bold"))  # Etiqueta para la hora
etiqueta_hora.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)  # Coloca la etiqueta en la cuadrícula
entrada_hora = tk.Entry(frame_entrada)  # Campo de entrada para la hora
entrada_hora.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)  # Coloca el campo en la cuadrícula

etiqueta_descripcion = tk.Label(frame_entrada, text="Descripción del Evento:", bg="#FFB6C1", fg="black",
                                font=("Comic Sans MS", 10, "bold"))  # Etiqueta para la descripción
etiqueta_descripcion.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)  # Coloca la etiqueta en la cuadrícula
entrada_descripcion = tk.Entry(frame_entrada)  # Campo de entrada para la descripción
entrada_descripcion.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)  # Coloca el campo en la cuadrícula

# Crear botones con estilo
boton_agregar = tk.Button(frame_acciones, text="Agregar Evento", command=agregar_evento, bg="#4CAF50", fg="white",
                          borderwidth=2, relief="solid")  # Botón para agregar eventos
boton_agregar.pack(side=tk.LEFT, padx=10)  # Coloca el botón en la cuadrícula

boton_eliminar = tk.Button(frame_acciones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="#FF9800",
                           fg="white", borderwidth=2, relief="solid")  # Botón para eliminar eventos
boton_eliminar.pack(side=tk.LEFT, padx=10)  # Coloca el botón en la cuadrícula

boton_salir = tk.Button(frame_acciones, text="Salir", command=root.quit, bg="red", fg="white", borderwidth=2,
                        relief="solid")  # Botón para salir
boton_salir.pack(side=tk.RIGHT, padx=10)  # Coloca el botón en la cuadrícula

# Cargar eventos al iniciar la aplicación
cargar_eventos()  # Llama a la función para cargar eventos desde el archivo

# Ejecutar el bucle principal
root.mainloop()  # Inicia el bucle de la aplicación
