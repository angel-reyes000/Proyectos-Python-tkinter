import tkinter as tk
from tkinter import messagebox
import random

class JuegoAtrapar:
    def __init__(self, root):
        self.root = root
        self.root.title("Atrapalo")
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="Black")

    def Ganador(self):
        messagebox.showinfo("Ganaste", "Lograste atrapar el boton")

    def Movimientos(self, *args):
        self.x = random.randint(0, 435)
        self.y = random.randint(0, 475)
        self.boton.place(x= self.x, y= self.y)

    def Boton(self):
        self.boton = tk.Button(self.root, text="Atrapame", command=self.Ganador, borderwidth=5)
        self.boton.bind("<Enter>", self.Movimientos)
        self.boton.place(x=0, y=0)

root = tk.Tk()

j = JuegoAtrapar(root)
j.Boton()

root.mainloop()