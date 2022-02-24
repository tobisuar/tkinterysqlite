from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from turtle import title
import personas

class FormularioPersonas:
    def __init__(self):
        self.personas1=personas.Personas()
        self.ventana1 = tk.Tk()
        self.ventana1=title("Mantenimiento de Personal")
        self.cuaderno1 = ttk.Entrada(self.ventana1)
        self.carga_personas()
        self.consulta_por_legajo()
        self.listado_completo()
        self.cuaderno1.grid(column = 0, row=0,padx = 10, pady= 10)
        self.ventana1.mainloop()
    
    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add (self.pagina1,text = "Carga de Personas")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text= "Personas")
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)
        self.label1=ttk.Label(self.labelframe1,text="Apellido")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1,row=0,padx=4,pady=4)