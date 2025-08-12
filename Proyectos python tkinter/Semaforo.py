import tkinter as tk
from tkinter import Canvas

# Semaforo que funciona en base a la tupla de tuplas. True:Encendido, False:Apagado.
# No importa si tiene menos o mas tuplas o estan revueltas las tupals dentro de la tupla. 

class Semaforo:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="black")
        self.canvas = tk.Canvas(self.root, width=250, height=680, bg="gray")
        self.canvas.grid(row=0, column=0)
        self.indice = 0
        self.fases =   ((True,  False, False),
                        (True,  True,  False),
                        (False, False, True),
                        (False, True,  False))
    
    def Configurar(self, circulo, color):
        self.canvas.itemconfig(circulo, fill=color)

    def Desconfigurar(self, circulo):
        self.canvas.itemconfig(circulo, fill="gray")

    def Colores(self, *args):
        for _ in self.fases[self.indice]:
            if self.fases[self.indice] == (True,  False, False):
                self.Configurar(self.PrimerCirculo, "red")
                self.Desconfigurar(self.SegundoCirculo)
                self.Desconfigurar(self.TercerCirculo)
            elif self.fases[self.indice] == (True,  True,  False):
                self.Configurar(self.PrimerCirculo, "red")
                self.Configurar(self.SegundoCirculo, "yellow")
                self.Desconfigurar(self.TercerCirculo)
            elif self.fases[self.indice] == (False, False, True):
                self.Desconfigurar(self.PrimerCirculo)
                self.Desconfigurar(self.SegundoCirculo)
                self.Configurar(self.TercerCirculo, "green")
            else:
                self.Desconfigurar(self.PrimerCirculo)
                self.Configurar(self.SegundoCirculo, "yellow")
                self.Desconfigurar(self.TercerCirculo)
        if self.indice < len(self.fases) - 1:
            self.indice+=1
        else:
            self.indice = 0

    def Salir(self):
        self.root.destroy()

    def Circulos(self):
        self.PrimerCirculo = self.canvas.create_oval(30, 20, 220, 220, outline="black", width=4)
        self.SegundoCirculo = self.canvas.create_oval(30, 240, 220, 440, outline="black", width=4)
        self.TercerCirculo = self.canvas.create_oval(30, 460, 220, 660, outline="black", width=4)

    def Botones(self):
        self.BotonNext = tk.Button(self.root, text="Next", borderwidth=5, font=("Arial", 12, "bold"), command=self.Colores)
        self.BotonNext.grid(row=1, column=0, pady=10)

        self.BotonSalir = tk.Button(self.root, text="Quit", borderwidth=5, font=("Arial", 12, "bold"), command = self.Salir)
        self.BotonSalir.grid(row=2, column=0)

        self.Etiqueta = tk.Label(self.root, height=1, width=35, bg="black")
        self.Etiqueta.grid(row=3, column=0)

    def Todo(self):
        self.Circulos()
        self.Botones()

root = tk.Tk()
s = Semaforo(root)
s.Todo()
root.mainloop()
