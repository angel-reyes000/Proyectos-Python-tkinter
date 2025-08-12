import tkinter as tk
from tkinter import messagebox
import random

class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en raya")
        self.root.resizable(width=False, height=False)
        self.contador = 0

    def HacerNada(self, event=None):
        return "break"

    def Verificacion(self, uno, dos, tres, boleano):
        if self.ListaBotones[uno].cget("text") == boleano and self.ListaBotones[dos].cget("text") == boleano and self.ListaBotones[tres].cget("text") == boleano:
            if boleano == True:
                messagebox.showinfo("Ganaste!!", "Felicidades has ganado!!")
            elif boleano == False:
                messagebox.showinfo("Perdiste:(", "Vuelve a intentarlo...")
            for q in self.ListaBotones:
                q.unbind("<Button-1>")
            self.root.bind("<Enter>", self.HacerNada())

    def Perdedor(self, *args):
        self.Verificacion(0, 1, 2, False) #Primera linea
        self.Verificacion(3, 4, 5, False) #Segunda linea
        self.Verificacion(6, 7, 8, False) #Tercera linea

        self.Verificacion(0, 3, 6, False)
        self.Verificacion(1, 4, 7, False)
        self.Verificacion(2, 5, 8, False)

        self.Verificacion(0, 4, 8, False)
        self.Verificacion(2, 4, 6, False)

    def Ganador(self, *args):
        self.Verificacion(0, 1, 2, True) #Primera linea
        self.Verificacion(3, 4, 5, True) #Segunda linea
        self.Verificacion(6, 7, 8, True) #Tercera linea

        self.Verificacion(0, 3, 6, True)
        self.Verificacion(1, 4, 7, True)
        self.Verificacion(2, 5, 8, True)

        self.Verificacion(0, 4, 8, True)
        self.Verificacion(2, 4, 6, True)

    def Equis(self):
        VariableRandom = random.randrange(0, 9) 
        boton = self.ListaBotones[VariableRandom]
        for q in range(100):
            if boton.cget("state") != tk.DISABLED:
                canvas = tk.Canvas(boton, width=138, height=135, bg="white")
                canvas.pack()
                canvas.create_line(40, 30, 98, 95, fill="black", width=15)
                canvas.create_line(40, 95, 98, 30, fill="black", width=15)
                boton.config(state=tk.DISABLED, text=0)
                boton.unbind("<Button-1>")
                break
            else:
                OtroRandom = random.randrange(0, 9) 
                boton = self.ListaBotones[OtroRandom]
        self.Perdedor()

    def Circulo(self, boton):
        canvas = tk.Canvas(boton, width=138, height=135, bg="white")
        canvas.pack()
        canvas.create_oval(22, 20, 122, 120, outline="black", width=15)
        boton.unbind("<Button-1>")
        boton.config(state=tk.DISABLED, text=1)
        self.Equis()
        self.Ganador()

    def Botones(self):
        self.ListaBotones = []
        for fila in range(3):
            for columna in range(3):
                boton = tk.Button(self.root, width=20, height=9, border=8, state = tk.ACTIVE, fg="white")
                boton.grid(row=fila, column=columna)
                self.ListaBotones.append(boton)

        for boton in self.ListaBotones:
            boton.bind("<Button-1>", lambda event, b=boton: self.Circulo(b))

        self.ListaBotones[4].bind("<Button-1>", self.BotonCentro(4))

    def BotonCentro(self, indice):
        canvas = tk.Canvas(self.ListaBotones[indice], width=138, height=135, bg="white")
        canvas.pack()
        canvas.create_line(40, 30, 98, 95, fill="black", width=15)
        canvas.create_line(40, 95, 98, 30, fill="black", width=15)
        self.ListaBotones[indice].config(state=tk.DISABLED, text=0)
        self.ListaBotones[indice].unbind("<Button-1>")

root = tk.Tk()
t = TresEnRaya(root)
t.Botones()
root.mainloop()
