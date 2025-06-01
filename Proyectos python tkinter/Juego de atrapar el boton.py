import tkinter as tk
import random
from tkinter import messagebox

def mover(*args):
    xx = random.randint(0, 430)
    yy = random.randint(0, 470)
    boton.place(x=xx, y=yy)

def click(*args):
    messagebox.showinfo("Logrado", "Has atrapado el boton!")

root = tk.Tk()

boton = tk.Button(root, text="Atrapame", bg="light blue", border=10, command=click)
boton.place(x=225, y=225)
boton.bind("<Enter>", mover)

root.geometry("500x500")
root.config(bg="light pink")

root.mainloop()

