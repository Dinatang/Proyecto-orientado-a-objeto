import tkinter as tk
from tkinter import messagebox

# Creamos nuestra clase llamada TodoApp
class TodoApp:
    def __init__(self, root):  # Nota: corregido de _init_ a __init__ para inicialización correcta
        self.root = root
        # Ponemos el título de nuestra interfaz
        self.root.title("Gestor de Tareas de Dina Tanguila")
        # Ponemos el tamaño de nuestra interfaz
        self.root.geometry("600x600")
        # Cambiamos el color de fondo a morado
        self.root.config(bg="purple")

        # Creamos la lista para almacenar las tareas insertadas
        self.tasks = []

        # Agregamos nuestro campo de entrada para agregar nuevas tareas
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=20)
        # Asociamos la tecla Enter para agregar una tarea cuando se presione
        self.entry.bind('<Return>', self.add_task)

        # Creamos un frame para organizar los botones en una fila horizontal
        button_frame = tk.Frame(root, bg="purple")  # Fondo igual al de la ventana principal
        button_frame.pack(pady=10)

        # Creamos el botón "Añadir"
        self.add_button = tk.Button(button_frame, text="Añadir", command=self.add_task, bg="green", fg="white", borderwidth=3, relief="solid")
        self.add_button.pack(side="left", padx=5)  # Ajustamos el padx para reducir el espacio

        # Creamos el botón "Marcar" para marcar tareas como completadas
        self.complete_button = tk.Button(button_frame, text="Marcar", command=self.mark_completed, bg="green", fg="white", borderwidth=3, relief="solid")
        self.complete_button.pack(side="left", padx=5)

        # Creamos el botón "Eliminar" para eliminar tareas seleccionadas
        self.delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_task, bg="green", fg="white", borderwidth=3, relief="solid")
        self.delete_button.pack(side="left", padx=5)

        # Creamos el listbox para mostrar las tareas agregadas
        self.tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=20)
        self.tasks_listbox.pack(pady=10)

        # Asociamos teclas de acceso rápido para facilitar la interacción
        self.root.bind('<c>', self.mark_completed)  # Tecla 'c' para marcar tarea completada
        self.root.bind('<d>', self.delete_task)     # Tecla 'd' para eliminar tarea
        self.root.bind('Delete', self.delete_task)  # Tecla 'Delete' también para eliminar
        self.root.bind('Escape', lambda event: root.quit())  # Tecla 'Escape' para cerrar la aplicación

    # Función para añadir una nueva tarea
    def add_task(self, event=None):
        # Obtenemos el texto ingresado en el campo de entrada
        task = self.entry.get().strip()
        if task:
            # Si la tarea no está vacía, la añadimos a la lista de tareas
            self.tasks.append({'task': task, 'completed': False})
            # Actualizamos el listbox con las tareas
            self.update_task_list()
            # Limpiamos el campo de entrada
            self.entry.delete(0, tk.END)
        else:
            # Mostramos un mensaje de advertencia si el campo está vacío
            messagebox.showwarning("Mensaje de alerta", "Ingresa una tarea para poder agregar")

    # Función para marcar una tarea como completada
    def mark_completed(self, event=None):
        # Obtenemos el índice de la tarea seleccionada en el listbox
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            # Si hay una tarea seleccionada, marcamos la tarea como completada
            task_index = selected_task_index[0]
            self.tasks[task_index]['completed'] = True
            # Actualizamos el listbox con las tareas
            self.update_task_list()
        else:
            # Mostramos un mensaje de advertencia si no hay tarea seleccionada
            messagebox.showwarning("Alerta", "Selecciona una tarea para marcar como completada")

    # Función para eliminar una tarea
    def delete_task(self, event=None):
        # Obtenemos el índice de la tarea seleccionada en el listbox
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            # Si hay una tarea seleccionada, la eliminamos de la lista
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            # Actualizamos el listbox con las tareas restantes
            self.update_task_list()
        else:
            # Mostramos un mensaje de advertencia si no hay tarea seleccionada
            messagebox.showwarning("Alerta", "Selecciona una tarea para eliminar")

    # Función para actualizar el listbox con las tareas ingresadas
    def update_task_list(self):
        # Limpiamos el listbox antes de actualizarlo
        self.tasks_listbox.delete(0, tk.END)
        # Recorremos la lista de tareas y las mostramos en el listbox
        for task in self.tasks:
            display_text = task['task']
            # Si la tarea está completada, agregamos "(Completada)" al final del texto
            if task['completed']:
                display_text += " (Completada)"
            # Insertamos la tarea en el listbox
            self.tasks_listbox.insert(tk.END, display_text)

# Este bloque inicia la aplicación
if __name__ == "__main__":  # Nota: corregido de _name_ a __name__ para que funcione correctamente
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
