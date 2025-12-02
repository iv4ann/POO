import tkinter as tk
from tkinter import messagebox
from model.operaciones import operaciones   

class Vistas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Notas")
        self.geometry("600x400")

        # Usuario actual, se asigna despues del login
        self.usuario_id = None

        # Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Mostrar menú principal al inicio
        self.mostrar_menu_principal()
        self.id_usuario=operaciones.login_usuario
    def limpiar(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def mostrar_menu_principal(self):
        self.limpiar()
        tk.Label(self.container, text=".::Menu Principal::.").pack(pady=10)
        tk.Button(self.container, text="1.-Registro", command=self.mostrar_registro).pack(pady=10)
        tk.Button(self.container, text="2.-Login", command=self.mostrar_login).pack(pady=10)
        tk.Button(self.container, text="3.-Salir", command=self.quit).pack(pady=10)

    
    def mostrar_registro(self):
        self.limpiar()
        tk.Label(self.container, text="Cual es tu nombre?").pack()
        self.nombre = tk.Entry(self.container)
        self.nombre.pack()
        tk.Label(self.container, text="Cuales son tus apellidos").pack()
        self.apellidos = tk.Entry(self.container)
        self.apellidos.pack()
        tk.Label(self.container, text="Ingresa tu email").pack()
        self.email = tk.Entry(self.container)
        self.email.pack()
        tk.Label(self.container, text="Ingresa tu contrasena").pack()
        self.password = tk.Entry(self.container, show="*")
        self.password.pack()

        tk.Button(self.container, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self.container, text="Volver", command=self.mostrar_menu_principal).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre.get()
        apellidos = self.apellidos.get()
        email = self.email.get()
        password = self.password.get()

        if nombre and apellidos and email and password:
            if operaciones.registrar_usuario(nombre, apellidos, email, password):
                messagebox.showinfo("Registro", f"Usuario {nombre} registrado correctamente")
                self.mostrar_menu_principal()
            else:
                messagebox.showerror("Error", "No se pudo registrar el usuario")
        else:
            messagebox.showwarning("Error", "Completa todos los campos")

    
    def mostrar_login(self):
        self.limpiar()
        tk.Label(self.container, text=".::Login::.").pack()
        tk.Label(self.container, text="Ingresa tu email").pack()
        self.login_email = tk.Entry(self.container)
        self.login_email.pack()
        tk.Label(self.container, text="Ingresa tu contrasena").pack()
        self.login_password = tk.Entry(self.container, show="*")
        self.login_password.pack()

        tk.Button(self.container, text="Entrar", command=self.login_usuario).pack(pady=10)
        tk.Button(self.container, text="Volver", command=self.mostrar_menu_principal).pack(pady=10)

    def login_usuario(self):
        email = self.login_email.get()
        password = self.login_password.get()
        resultado = operaciones.login_usuario(email, password)
        if resultado:
            self.usuario_id, self.usuario_nombre = resultado
            messagebox.showinfo("Login", f"{self.usuario_nombre}, has iniciado sesion correctamente")
            self.mostrar_menu_notas()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

    
    def mostrar_menu_notas(self):
        self.limpiar()
        tk.Label(self.container,text=f"Bienvenido {self.usuario_nombre} has iniciado sesion correctamente").pack()
        tk.Label(self.container, text=".::Menu Notas::.").pack()
        tk.Button(self.container, text="Crear", command=self.crear_nota).pack(pady=10)
        tk.Button(self.container, text="Mostrar", command=self.mostrar_nota).pack(pady=10)
        tk.Button(self.container, text="Cambiar", command=self.cambiar_nota).pack(pady=10)
        tk.Button(self.container, text="Eliminar", command=self.eliminar_nota).pack(pady=10)
        tk.Button(self.container, text="Regresar", command=self.mostrar_menu_principal).pack(pady=10)

    
    def crear_nota(self):
        self.limpiar()
        tk.Label(self.container,text=".::Crear Nota::.").pack()
        tk.Label(self.container,text="Titulo").pack()
        self.titulo = tk.Entry(self.container)
        self.titulo.pack()
        tk.Label(self.container,text="Descripcion").pack()
        self.descripcion = tk.Entry(self.container)
        self.descripcion.pack()
        tk.Button(self.container,text="Guardar",command=self.guardar_nota).pack(pady=10,padx=10)
        tk.Button(self.container,text="Volver",command=self.mostrar_menu_notas).pack(pady=10,padx=10)

    def guardar_nota(self):
        titulo = self.titulo.get()
        descripcion = self.descripcion.get()
        if titulo and descripcion and self.usuario_id:
            operaciones.guardar_nota(self.usuario_id, titulo, descripcion)
            messagebox.showinfo("Éxito", "Nota guardada correctamente")
        else:
            messagebox.showwarning("Error", "Completa todos los campos o inicia sesión")

    def mostrar_nota(self):
        self.limpiar()
        tk.Label(self.container, text=f"{self.usuario_nombre}, tus notas son:").pack()
        notas = operaciones.obtener_notas(self.usuario_id)
        for nota in notas:
            tk.Label(self.container,text=f"ID:{nota[0]}  Título:{nota[1]}  Descripción:{nota[2]}  Fecha:{nota[3]}").pack()
        tk.Button(self.container, text="Volver", command=self.mostrar_menu_notas).pack(pady=10, padx=10)

    def cambiar_nota(self):
        self.limpiar()
        tk.Label(self.container,text=f"{self.usuario_nombre}, ingresa la nota que quieras cambiar").pack()
        tk.Label(self.container,text="ID de la nota a cambiar:").pack()
        self.nota_id = tk.Entry(self.container)
        self.nota_id.pack()
        tk.Label(self.container,text="Nuevo Titulo").pack()
        self.nuevo_titulo = tk.Entry(self.container)
        self.nuevo_titulo.pack()
        tk.Label(self.container,text="Nueva Descripcion").pack()
        self.nueva_descripcion = tk.Entry(self.container)
        self.nueva_descripcion.pack()
        tk.Button(self.container,text="Guardar",command=self.actualizar_nota).pack(pady=10,padx=10)
        tk.Button(self.container,text="Volver",command=self.mostrar_menu_notas).pack(pady=10,padx=10)

    def actualizar_nota(self):
        nota_id = self.nota_id.get()
        titulo = self.nuevo_titulo.get()
        descripcion = self.nueva_descripcion.get()
        if nota_id and titulo and descripcion and self.usuario_id:
            operaciones.actualizar_nota(self.usuario_id, nota_id, titulo, descripcion)
            messagebox.showinfo("Éxito", "Nota actualizada correctamente")
        else:
            messagebox.showwarning("Error", "Completa todos los campos")

    def eliminar_nota(self):
        self.limpiar()
        tk.Label(self.container,text="ID de la nota a eliminar:").pack()
        self.nota_id_eliminar = tk.Entry(self.container)
        self.nota_id_eliminar.pack()
        tk.Button(self.container,text="Eliminar",command=self.borrar_nota).pack(pady=10,padx=10)
        tk.Button(self.container,text="Volver",command=self.mostrar_menu_notas).pack(pady=10,padx=10)
        

    def borrar_nota(self):
        nota_id = self.nota_id_eliminar.get()
        if nota_id and self.usuario_id:
            operaciones.eliminar_nota(self.usuario_id, nota_id)
            messagebox.showinfo("Éxito", "Nota eliminada correctamente")
        else:
            messagebox.showwarning("Error", "Ingresa el ID de la nota")

    def salir(self):
        self.quit()