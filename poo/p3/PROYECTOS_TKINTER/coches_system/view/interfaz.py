import tkinter as tk
from tkinter import messagebox
from controller.funciones import *

class vistas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coches")
        self.geometry("800x600")
        self.configure(bg="#0A3869")
        self.container = tk.Frame(self,bg="#0C0A69")
        self.container.pack(fill="both", expand=True)
        self.menu_principal()
    def limpiar(self):
        for widget in self.container.winfo_children():
            widget.destroy()
    def menu_principal(self):
        self.limpiar()
        tk.Label(self.container,text=".::Menu Principal::.").pack()
        tk.Button(self.container,text="1.-Autos",command=self.autos).pack(padx=10,pady=10)
        tk.Button(self.container,text="2.-Camionetas",command=self.camionetas).pack(padx=10,pady=10)
        tk.Button(self.container,text="3.-Camiones",command=self.camiones).pack(padx=10,pady=10)
        tk.Button(self.container,text="4.-Salir",command=self.salir).pack(padx=10,pady=10)

    def autos(self):
        self.limpiar()
        tk.Label(self.container,text=".::Menu Autos::.").pack()
        tk.Button(self.container,text="1.-Insertar",command=self.insertar).pack(padx=10,pady=10)
        tk.Button(self.container,text="2.-Consultar",command=self.consultar).pack(padx=10,pady=10)
        tk.Button(self.container,text="3.-Actualizar",command=self.actualizar).pack(padx=10,pady=10)
        tk.Button(self.container,text="4.-Eliminar",command=self.eliminar).pack(padx=10,pady=10)
        tk.Button(self.container,text="5.-Regresar",command=self.menu_principal).pack(padx=10,pady=10)
    def camionetas(self):
        self.limpiar()
        tk.Label(self.container,text=".::Menu Camionetas::.").pack()
        tk.Button(self.container,text="1.-Insertar",command=self.insertar_camioneta).pack(padx=10,pady=10)
        tk.Button(self.container,text="2.-Consultar",command=self.consultar_camionetas).pack(padx=10,pady=10)
        tk.Button(self.container,text="3.-Actualizar",command=self.actualizar_camioneta).pack(padx=10,pady=10)
        tk.Button(self.container,text="4.-Eliminar",command=self.eliminar_camioneta).pack(padx=10,pady=10)
        tk.Button(self.container,text="5.-Regresar",command=self.menu_principal).pack(padx=10,pady=10)
    def camiones(self):
        self.limpiar()
        tk.Label(self.container,text=".::Menu Camiones::.").pack()
        tk.Button(self.container,text="1.-Insertar",command=self.insertar_camiones).pack(padx=10,pady=10)
        tk.Button(self.container,text="2.-Consultar",command=self.consultar_camiones).pack(padx=10,pady=10)
        tk.Button(self.container,text="3.-Actualizar",command=self.cambiar_camiones).pack(padx=10,pady=10)
        tk.Button(self.container,text="4.-Eliminar",command=self.eliminar_camion).pack(padx=10,pady=10)
        tk.Button(self.container,text="5.-Regresar",command=self.menu_principal).pack(padx=10,pady=10)
    def salir(self):
        self.quit()
    def insertar(self):
        self.limpiar()
        tk.Label(self.container,text="Ingrese la marca del coche que desea agregar").pack()
        self.entry_marca = tk.Entry(self.container)
        self.entry_marca.pack()
        tk.Label(self.container,text="Ingrese el color del coche que desea agregar").pack()
        self.entry_color = tk.Entry(self.container)
        self.entry_color.pack()
        tk.Label(self.container,text="Ingrese el modelo del coche que desea agregar").pack()
        self.entry_modelo = tk.Entry(self.container)
        self.entry_modelo.pack()
        tk.Label(self.container,text="Ingrese la velocidad del coche que desea agregar").pack()
        self.entry_velocidad = tk.Entry(self.container)
        self.entry_velocidad.pack()
        tk.Label(self.container,text="Ingrese el caballaje del coche que desea agregar").pack()
        self.entry_caballaje = tk.Entry(self.container)
        self.entry_caballaje.pack()
        tk.Label(self.container,text="Ingrese las plazas del coche que desea agregar").pack()
        self.entry_plazas = tk.Entry(self.container)
        self.entry_plazas.pack()
        tk.Button(self.container,text="Guardar",command=self.guardar_auto).pack(padx=10,pady=10)
        tk.Button(self.container,text="Regresar",command=self.autos).pack(padx=10,pady=10)
    def guardar_auto(self):
        marca = self.entry_marca.get()
        color = self.entry_color.get()
        modelo = self.entry_modelo.get()
        velocidad = self.entry_velocidad.get()
        caballaje = self.entry_caballaje.get()
        plazas = self.entry_plazas.get()
        try:
            new_id = insertar_auto_controller(marca, color, modelo, velocidad, caballaje, plazas)
            messagebox.showinfo('OK', f'Auto insertado con ID {new_id}')
            self.autos()
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo insertar el auto: {e}')
    def consultar(self):
        self.limpiar()
        tk.Label(self.container,text="Listado de Autos").pack()
        try:
            rows = consultar_autos_controller()
        except Exception as e:
            messagebox.showerror('Error', f'Error consultando autos: {e}')
            return
        frame = tk.Frame(self.container)
        frame.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        for r in rows:
            listbox.insert('end', f"ID {r['id']} - {r['marca']} {r['modelo']} ({r['color']}) - {r['velocidad']} km/h - {r['caballaje']} HP - {r['plazas']} plazas")
        listbox.pack(fill='both', expand=True)
        scrollbar.config(command=listbox.yview)
        tk.Button(self.container, text='Regresar', command=self.autos).pack(padx=10, pady=10)
    def actualizar(self):
        self.limpiar()
        tk.Label(self.container,text="Ingrese el ID del coche que desea actualizar").pack()
        self.entry_id_update = tk.Entry(self.container)
        self.entry_id_update.pack()
        tk.Label(self.container,text="Nueva marca (opcional)").pack()
        self.entry_up_marca = tk.Entry(self.container)
        self.entry_up_marca.pack()
        tk.Label(self.container,text="Nuevo color (opcional)").pack()
        self.entry_up_color = tk.Entry(self.container)
        self.entry_up_color.pack()
        tk.Label(self.container,text="Nuevo modelo (opcional)").pack()
        self.entry_up_modelo = tk.Entry(self.container)
        self.entry_up_modelo.pack()
        tk.Label(self.container,text="Nueva velocidad (opcional)").pack()
        self.entry_up_velocidad = tk.Entry(self.container)
        self.entry_up_velocidad.pack()
        tk.Label(self.container,text="Nuevo caballaje (opcional)").pack()
        self.entry_up_caballaje = tk.Entry(self.container)
        self.entry_up_caballaje.pack()
        tk.Label(self.container,text="Nuevas plazas (opcional)").pack()
        self.entry_up_plazas = tk.Entry(self.container)
        self.entry_up_plazas.pack()
        tk.Button(self.container, text='Actualizar', command=self.guardar_actualizacion).pack(padx=10, pady=10)
        tk.Button(self.container, text='Regresar', command=self.autos).pack(padx=10, pady=10)
    def guardar_actualizacion(self):
        id_ = self.entry_id_update.get()
        if not id_:
            messagebox.showerror('Error', 'Debe ingresar el ID del auto para actualizar')
            return
        kwargs = {}
        if self.entry_up_marca.get():
            kwargs['marca'] = self.entry_up_marca.get()
        if self.entry_up_color.get():
            kwargs['color'] = self.entry_up_color.get()
        if self.entry_up_modelo.get():
            kwargs['modelo'] = self.entry_up_modelo.get()
        if self.entry_up_velocidad.get():
            kwargs['velocidad'] = self.entry_up_velocidad.get()
        if self.entry_up_caballaje.get():
            kwargs['caballaje'] = self.entry_up_caballaje.get()
        if self.entry_up_plazas.get():
            kwargs['plazas'] = self.entry_up_plazas.get()
        try:
            updated = actualizar_auto_controller(int(id_), **kwargs)
            if updated:
                messagebox.showinfo('OK', f'Auto {id_} actualizado')
            else:
                messagebox.showinfo('Info', 'No se realizaron cambios')
            self.autos()
        except Exception as e:
            messagebox.showerror('Error', f'Error al actualizar: {e}')
    def eliminar(self):
        self.limpiar()
        tk.Label(self.container,text="Ingrese el ID del auto que desee eliminar").pack()
        self.entry_id_delete = tk.Entry(self.container)
        self.entry_id_delete.pack()
        tk.Button(self.container,text="Borrar",command=self.borrar_auto).pack(padx=10,pady=10)
        tk.Button(self.container,text="Regresar",command=self.autos).pack(padx=10,pady=10)
    def borrar_auto(self):
        id_ = self.entry_id_delete.get()
        if not id_:
            messagebox.showerror('Error', 'Debe ingresar un ID')
            return
        try:
            deleted = eliminar_auto_controller(int(id_))
            if deleted:
                messagebox.showinfo('OK', f'Auto {id_} eliminado')
            else:
                messagebox.showinfo('Info', 'No se encontró el ID')
            self.autos()
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar: {e}')
    def guardar_camion(self):
        marca = self.entry_camion_marca.get()
        color = self.entry_camion_color.get()
        modelo = self.entry_camion_modelo.get()
        velocidad = self.entry_camion_vel.get()
        caballaje = self.entry_camion_cab.get()
        plazas = self.entry_camion_plazas.get()
        traccion = self.entry_camion_traccion.get()
        cerrada = self.var_camion_cerrada.get()
        try:
            new_id = insertar_camioneta_controller(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            messagebox.showinfo('OK', f'Camioneta insertada con ID {new_id}')
            self.camiones()
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo insertar la camioneta: {e}')
    def insertar_camiones(self):
        self.limpiar()
        tk.Label(self.container,text="Ingrese la marca del camion que desea agregar").pack()
        self.entry_cam_marca = tk.Entry(self.container)
        self.entry_cam_marca.pack()
        tk.Label(self.container,text="Ingrese el color del camion que desea agregar").pack()
        self.entry_cam_color = tk.Entry(self.container)
        self.entry_cam_color.pack()
        tk.Label(self.container,text="Ingrese el modelo del camion que desea agregar").pack()
        self.entry_cam_modelo = tk.Entry(self.container)
        self.entry_cam_modelo.pack()
        tk.Label(self.container,text="Ingrese la velocidad del camion que desea agregar").pack()
        self.entry_cam_velocidad = tk.Entry(self.container)
        self.entry_cam_velocidad.pack()
        tk.Label(self.container,text="Ingrese el caballaje del camion que desea agregar").pack()
        self.entry_cam_caballaje = tk.Entry(self.container)
        self.entry_cam_caballaje.pack()
        tk.Label(self.container,text="Ingrese las plazas del camion que desea agregar").pack()
        self.entry_cam_plazas = tk.Entry(self.container)
        self.entry_cam_plazas.pack()
        tk.Label(self.container,text="Ingrese los ejes del camion que desea agregar").pack()
        self.entry_cam_eje = tk.Entry(self.container)
        self.entry_cam_eje.pack()
        tk.Label(self.container,text="Ingrese la capacidad de carga del camion que desea agregar").pack()
        self.entry_cam_capacidad = tk.Entry(self.container)
        self.entry_cam_capacidad.pack()
        tk.Button(self.container,text="Guardar",command=self.guardar_camion).pack(padx=10,pady=10)
        tk.Button(self.container,text="Regresar",command=self.camiones).pack(padx=10,pady=10)
    def consultar_camiones(self):
        self.limpiar()
        tk.Label(self.container,text='Listado de Camiones').pack()
        try:
            rows = consultar_camiones_controller()
        except Exception as e:
            messagebox.showerror('Error', f'Error consultando camiones: {e}')
            return
        frame = tk.Frame(self.container)
        frame.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        for r in rows:
            listbox.insert('end', f"ID {r['id']} - {r['marca']} {r['modelo']} ({r['color']}) - {r['velocidad']} km/h - {r['caballaje']} HP - {r['plazas']} plazas - Ejes {r['eje']} - Capacidad {r['capacidadcarga']}")
        listbox.pack(fill='both', expand=True)
        scrollbar.config(command=listbox.yview)
        tk.Button(self.container, text='Regresar', command=self.camiones).pack(padx=10, pady=10)
    def cambiar_camiones(self):
        self.limpiar()
        tk.Label(self.container,text='Ingrese el ID del camion que desea actualizar').pack()
        self.entry_cam_id_update = tk.Entry(self.container)
        self.entry_cam_id_update.pack()
        tk.Label(self.container,text='Nueva marca (opcional)').pack()
        self.entry_cam_up_marca = tk.Entry(self.container)
        self.entry_cam_up_marca.pack()
        tk.Label(self.container,text='Nuevo color (opcional)').pack()
        self.entry_cam_up_color = tk.Entry(self.container)
        self.entry_cam_up_color.pack()
        tk.Label(self.container,text='Nuevo modelo (opcional)').pack()
        self.entry_cam_up_modelo = tk.Entry(self.container)
        self.entry_cam_up_modelo.pack()
        tk.Label(self.container,text='Nueva velocidad (opcional)').pack()
        self.entry_cam_up_vel = tk.Entry(self.container)
        self.entry_cam_up_vel.pack()
        tk.Label(self.container,text='Nuevo caballaje (opcional)').pack()
        self.entry_cam_up_cab = tk.Entry(self.container)
        self.entry_cam_up_cab.pack()
        tk.Label(self.container,text='Nuevas plazas (opcional)').pack()
        self.entry_cam_up_plazas = tk.Entry(self.container)
        self.entry_cam_up_plazas.pack()
        tk.Label(self.container,text='Nuevo eje (opcional)').pack()
        self.entry_cam_up_eje = tk.Entry(self.container)
        self.entry_cam_up_eje.pack()
        tk.Label(self.container,text='Nueva capacidad (opcional)').pack()
        self.entry_cam_up_cap = tk.Entry(self.container)
        self.entry_cam_up_cap.pack()
        tk.Button(self.container, text='Actualizar', command=self.guardar_actualizacion_camion).pack(padx=10, pady=10)
        tk.Button(self.container, text='Regresar', command=self.camiones).pack(padx=10, pady=10)
    def guardar_actualizacion_camion(self):
        id_ = self.entry_cam_id_update.get()
        if not id_:
            messagebox.showerror('Error', 'Debe ingresar el ID del camion para actualizar')
            return
        kwargs = {}
        if self.entry_cam_up_marca.get():
            kwargs['marca'] = self.entry_cam_up_marca.get()
        if self.entry_cam_up_color.get():
            kwargs['color'] = self.entry_cam_up_color.get()
        if self.entry_cam_up_modelo.get():
            kwargs['modelo'] = self.entry_cam_up_modelo.get()
        if self.entry_cam_up_vel.get():
            kwargs['velocidad'] = self.entry_cam_up_vel.get()
        if self.entry_cam_up_cab.get():
            kwargs['caballaje'] = self.entry_cam_up_cab.get()
        if self.entry_cam_up_plazas.get():
            kwargs['plazas'] = self.entry_cam_up_plazas.get()
        if self.entry_cam_up_eje.get():
            kwargs['eje'] = self.entry_cam_up_eje.get()
        if self.entry_cam_up_cap.get():
            kwargs['capacidadcarga'] = self.entry_cam_up_cap.get()
        try:
            updated = actualizar_camion_controller(int(id_), **kwargs)
            if updated:
                messagebox.showinfo('OK', f'Camion {id_} actualizado')
            else:
                messagebox.showinfo('Info', 'No se realizaron cambios')
            self.camiones()
        except Exception as e:
            messagebox.showerror('Error', f'Error al actualizar: {e}')
    def eliminar_camion(self):
        self.limpiar()
        tk.Label(self.container,text='Ingrese el ID del camion que desee eliminar').pack()
        self.entry_cam_id_delete = tk.Entry(self.container)
        self.entry_cam_id_delete.pack()
        tk.Button(self.container,text='Borrar',command=self.borrar_camion).pack(padx=10,pady=10)
        tk.Button(self.container,text='Regresar',command=self.camiones).pack(padx=10,pady=10)
    def borrar_camion(self):
        id_ = self.entry_cam_id_delete.get()
        if not id_:
            messagebox.showerror('Error', 'Debe ingresar un ID')
            return
        try:
            deleted = eliminar_camion_controller(int(id_))
            if deleted:
                messagebox.showinfo('OK', f'Camion {id_} eliminado')
            else:
                messagebox.showinfo('Info', 'No se encontró el ID')
            self.camiones()
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar: {e}')
    def insertar_camioneta(self):
        self.limpiar()
        tk.Label(self.container,text="Ingrese la marca de la camioneta que desea agregar").pack()
        self.entry_camioneta_marca = tk.Entry(self.container)
        self.entry_camioneta_marca.pack()
        tk.Label(self.container,text="Ingrese el color de la camioneta que desea agregar").pack()
        self.entry_camioneta_color = tk.Entry(self.container)
        self.entry_camioneta_color.pack()
        tk.Label(self.container,text="Ingrese el modelo de la camioneta que desea agregar").pack()
        self.entry_camioneta_modelo = tk.Entry(self.container)
        self.entry_camioneta_modelo.pack()
        tk.Label(self.container,text="Ingrese la velocidad de la camioneta que desea agregar").pack()
        self.entry_camioneta_vel = tk.Entry(self.container)
        self.entry_camioneta_vel.pack()
        tk.Label(self.container,text="Ingrese el caballaje de la camioneta que desea agregar").pack()
        self.entry_camioneta_cab = tk.Entry(self.container)
        self.entry_camioneta_cab.pack()
        tk.Label(self.container,text="Ingrese las plazas de la camioneta que desea agregar").pack()
        self.entry_camioneta_plazas = tk.Entry(self.container)
        self.entry_camioneta_plazas.pack()
        tk.Label(self.container,text="Ingrese la traccion de la camioneta que desea agregar").pack()
        self.entry_camioneta_traccion = tk.Entry(self.container)
        self.entry_camioneta_traccion.pack()
        tk.Label(self.container,text="¿La camioneta es cerrada? (marque la casilla)").pack()
        self.var_camioneta_cerrada = tk.IntVar()
        self.check_camioneta_cerrada = tk.Checkbutton(self.container, variable=self.var_camioneta_cerrada)
        self.check_camioneta_cerrada.pack()
        tk.Button(self.container,text="Guardar",command=self.guardar_camioneta).pack(padx=10,pady=10)
        tk.Button(self.container,text="Regresar",command=self.camionetas).pack(padx=10,pady=10)
    def guardar_camioneta(self):
        marca = self.entry_camioneta_marca.get()
        color = self.entry_camioneta_color.get()
        modelo = self.entry_camioneta_modelo.get()
        velocidad = self.entry_camioneta_vel.get()
        caballaje = self.entry_camioneta_cab.get()
        plazas = self.entry_camioneta_plazas.get()
        traccion = self.entry_camioneta_traccion.get()
        cerrada = self.var_camioneta_cerrada.get()
        try:
            new_id = insertar_camioneta_controller(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            messagebox.showinfo('OK', f'Camioneta insertada con ID {new_id}')
            self.camionetas()
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo insertar la camioneta: {e}')
    def consultar_camionetas(self):
        self.limpiar()
        tk.Label(self.container,text='Listado de Camionetas').pack()
        try:
            rows = consultar_camionetas_controller()
        except Exception as e:
            messagebox.showerror('Error', f'Error consultando camionetas: {e}')
            return
        frame = tk.Frame(self.container)
        frame.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
        for r in rows:
            listbox.insert('end', f"ID {r['id']} - {r['marca']} {r['modelo']} ({r['color']}) - {r['velocidad']} km/h - {r['caballaje']} HP - {r['plazas']} plazas - Traccion {r['traccion']} - Cerrada {r['cerrada']}")
        listbox.pack(fill='both', expand=True)
        scrollbar.config(command=listbox.yview)
        tk.Button(self.container, text='Regresar', command=self.camionetas).pack(padx=10, pady=10)
    def actualizar_camioneta(self):
        self.limpiar()
        tk.Label(self.container,text='Ingrese el ID de la camioneta que desea actualizar').pack()
        self.entry_camioneta_id_update = tk.Entry(self.container)
        self.entry_camioneta_id_update.pack()
        
        
        tk.Button(self.container, text='Buscar', command=self.actualizar_camioneta_if).pack(padx=10, pady=10)
        tk.Button(self.container, text='Regresar', command=self.camionetas).pack(padx=10, pady=10)
    def actualizar_camioneta_if(self):
        camioneta_id = self.entry_camioneta_id_update.get().strip()
        if not camioneta_id:
            messagebox.showerror("Error, debe ingresar un ID que exista en la base de datos")
            return
        tk.Label(self.container,text='Nueva marca (opcional)').pack()
        self.entry_camioneta_up_marca = tk.Entry(self.container)
        self.entry_camioneta_up_marca.pack()
        tk.Label(self.container,text='Nuevo color (opcional)').pack()
        self.entry_camioneta_up_color = tk.Entry(self.container)
        self.entry_camioneta_up_color.pack()
        tk.Label(self.container,text='Nuevo modelo (opcional)').pack()
        self.entry_camioneta_up_modelo = tk.Entry(self.container)
        self.entry_camioneta_up_modelo.pack()
        tk.Label(self.container,text='Nueva velocidad (opcional)').pack()
        self.entry_camioneta_up_vel = tk.Entry(self.container)
        self.entry_camioneta_up_vel.pack()
        tk.Label(self.container,text='Nuevo caballaje (opcional)').pack()
        self.entry_camioneta_up_cab = tk.Entry(self.container)
        self.entry_camioneta_up_cab.pack()
        tk.Label(self.container,text='Nuevas plazas (opcional)').pack()
        self.entry_camioneta_up_plazas = tk.Entry(self.container)
        self.entry_camioneta_up_plazas.pack()
        tk.Label(self.container,text='Nueva traccion (opcional)').pack()
        self.entry_camioneta_up_traccion = tk.Entry(self.container)
        self.entry_camioneta_up_traccion.pack()
        tk.Label(self.container,text='Cambiar estado de cerrada (opcional)').pack()
        self.var_camioneta_up_cerrada = tk.IntVar()
        self.check_camioneta_up_cerrada = tk.Checkbutton(self.container, variable=self.var_camioneta_up_cerrada)
        self.check_camioneta_up_cerrada.pack()
        tk.Button(self.container, text='Actualizar', command=self.guardar_actualizacion_camioneta).pack(padx=10, pady=10)
        tk.Button(self.container, text='Regresar', command=self.camionetas).pack(padx=10, pady=10)
    def guardar_actualizacion_camioneta(self):
        id_ = self.entry_camioneta_id_update.get()
        if not id_:
            messagebox.showerror('Error', 'Debe ingresar el ID de la camioneta para actualizar')
            return
        kwargs = {}
        if self.entry_camioneta_up_marca.get():
            kwargs['marca'] = self.entry_camioneta_up_marca.get()
        if self.entry_camioneta_up_color.get():
            kwargs['color'] = self.entry_camioneta_up_color.get()
        if self.entry_camioneta_up_modelo.get():
            kwargs['modelo'] = self.entry_camioneta_up_modelo.get()
        if self.entry_camioneta_up_vel.get():
            kwargs['velocidad'] = self.entry_camioneta_up_vel.get()
        if self.entry_camioneta_up_cab.get():
            kwargs['caballaje'] = self.entry_camioneta_up_cab.get()
        if self.entry_camioneta_up_plazas.get():
            kwargs['plazas'] = self.entry_camioneta_up_plazas.get()
        if self.entry_camioneta_up_traccion.get():
            kwargs['traccion'] = self.entry_camioneta_up_traccion.get()
        if self.var_camioneta_up_cerrada.get() is not None:
            kwargs['cerrada'] = self.var_camioneta_up_cerrada.get()
        try:
            updated = actualizar_camioneta_controller(int(id_), **kwargs)
            if updated:
                messagebox.showinfo('OK', f'Camioneta {id_} actualizada')
            else:
                messagebox.showinfo('Info', 'No se realizaron cambios')
            self.camionetas()
        except Exception as e:
            messagebox.showerror('Error', f'Error al actualizar: {e}')
    def eliminar_camioneta(self):
        self.limpiar()
        tk.Label(self.container,text='Ingrese el ID de la camioneta que desee eliminar').pack()
        self.entry_camioneta_id_delete = tk.Entry(self.container)
        self.entry_camioneta_id_delete.pack()
        tk.Button(self.container,text='Borrar',command=self.borrar_camioneta).pack(padx=10,pady=10)
        tk.Button(self.container,text='Regresar',command=self.camionetas).pack(padx=10,pady=10)
    def borrar_camioneta(self):
        id_ = self.entry_camioneta_id_delete.get()
        if not id_:
            messagebox.showerror('Error', 'Debe ingresar un ID')
            return
        try:
            deleted = eliminar_camioneta_controller(int(id_))
            if deleted:
                messagebox.showinfo('OK', f'Camioneta {id_} eliminada')
            else:
                messagebox.showinfo('Info', 'No se encontró el ID')
            self.camionetas()
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar: {e}')
    def guardar_camion(self):
        marca = self.entry_cam_marca.get()
        color = self.entry_cam_color.get()
        modelo = self.entry_cam_modelo.get()
        velocidad = self.entry_cam_velocidad.get()
        caballaje = self.entry_cam_caballaje.get()
        plazas = self.entry_cam_plazas.get()
        eje=self.entry_cam_eje.get()
        capacidadcarga=self.entry_cam_capacidad.get()
        try:
            new_id = insertar_camion_controller(marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadcarga)
            messagebox.showinfo('OK', f'Auto insertado con ID {new_id}')
            self.autos()
        except Exception as e:
            messagebox.showerror('Error', f'No se pudo insertar el auto: {e}')
