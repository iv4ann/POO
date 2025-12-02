import tkinter as tk
from tkinter import messagebox
from controller.funciones import *

class vistas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coches")
        self.geometry("800x600")

        self.container = tk.Frame(self)
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
        tk.Button(self.container,text="3.-Actualizar",command=self.actualizar_camion).pack(padx=10,pady=10)
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
   
    def eliminar(self):
        self.limpiar()
        tk.Label(self.container,text="Ingrese el ID del auto que desee eliminar").pack()
        self.entry_id_delete = tk.Entry(self.container)
        self.entry_id_delete.pack()
        tk.Button(self.container,text="Borrar",command=self.borrar_auto).pack(padx=10,pady=10)
        tk.Button(self.container,text="Regresar",command=self.autos).pack(padx=10,pady=10)
   
