import tkinter as tk
from tkinter import messagebox
import random

#Clickear el numero mayor en orden descendente hasta que todos los botones esten en gris.
#El contador comienza al precionar el primer boton con el numero mayor.

class Clicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker")
        self.root.configure(bg="black")
        self.ValorContador = 0

    def BloquearClicks(self, event=None):
        return "break"

    def Botones(self, *args):
        self.ListaBotones = []
        for fila in range(5):
            for columna in range(5):
                self.NumeroRandom = tk.IntVar()
                self.NumeroRandom.set(random.randint(1, 999))
                self.boton = tk.Button(self.root, text=self.NumeroRandom.get(), width=15, height=2, borderwidth=6)
                self.boton.bind("<Button-1>", self.BloquearClicks)
                self.boton.grid(row=fila, column=columna)
                self.ListaBotones.append(self.boton)

    def Desactivar(self):
        self.ListaBotones[self.index].config(state=tk.DISABLED)
        del self.ListaBotones[self.index]
        self.NumeroMenor()
        if self.etiqueta.cget("text") == 0:
            self.etiqueta.after(1000, self.AumentoContador)

    def NumeroMenor(self, *args):
        self.numero = 0
        maximo = 0
        self.index = 0
        for boton in self.ListaBotones:
            if boton.cget("text") > maximo:
                maximo = boton.cget("text")
                indice = self.ListaBotones[self.numero]
                self.index = self.numero
            self.numero+=1
        try:
            if indice == self.ListaBotones[self.index]:
                self.ListaBotones[self.index].unbind("<Button-1>")
                self.ListaBotones[self.index].config(command=self.Desactivar)
        except:
            self.etiqueta.after_cancel(self.aumento)
            messagebox.showinfo("Ganaste!!!", "Felicidades has ganado!") 

    def AumentoContador(self, Event=None):
        self.ValorContador+=1
        self.etiqueta.config(text=self.ValorContador)
        self.aumento = self.etiqueta.after(1000, self.AumentoContador)

    def Contador(self):
        self.etiqueta = tk.Label(self.root, text=self.ValorContador, font=("Arial", 12, "bold"), bg="black", fg="white")
        self.etiqueta.grid(row=5, column=2)

    def Todo(self):
        self.Botones()
        self.Contador()
        self.NumeroMenor()

root = tk.Tk()
c = Clicker(root)
c.Todo()
root.mainloop()
