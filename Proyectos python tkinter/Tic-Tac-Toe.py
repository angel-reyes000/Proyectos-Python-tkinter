import tkinter as tk
from tkinter import messagebox
import random

def desactivar(*args):
    global botones
    messagebox.showinfo("Ganaste", "Felicidades Ganaste!")
    for q in botones:
        q.config(state=tk.DISABLED)

def desactivar_compu():
    messagebox.showinfo("Perdiste", "Vuelve a intentarlo!")
    for q in botones:
        q.config(state=tk.DISABLED)

def victorias():
    if b1.cget("state") == tk.DISABLED and b2.cget("state") == tk.DISABLED and b3.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b4.cget("state") == tk.DISABLED and b5.cget("state") == tk.DISABLED and b6.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b7.cget("state") == tk.DISABLED and b8.cget("state") == tk.DISABLED and b9.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b1.cget("state") == tk.DISABLED and b5.cget("state") == tk.DISABLED and b9.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b3.cget("state") == tk.DISABLED and b5.cget("state") == tk.DISABLED and b7.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b1.cget("state") == tk.DISABLED and b4.cget("state") == tk.DISABLED and b7.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b2.cget("state") == tk.DISABLED and b5.cget("state") == tk.DISABLED and b8.cget("state") == tk.DISABLED:
        root.after(0, desactivar)
    elif b3.cget("state") == tk.DISABLED and b6.cget("state") == tk.DISABLED and b9.cget("state") == tk.DISABLED:
        root.after(0, desactivar)

def automatico():
    random.shuffle(botones)
    for w in botones:
        canvas = tk.Canvas(w, width=208, height=225, bg="white")
        if w.cget("state") == tk.NORMAL:
            canvas.create_text(104, 112, text="x", font=("Arial", 100), fill="red")
            botones.remove(w)
            canvas.grid(row=1, column=1)
        break

def boton1():
    canvas = tk.Canvas(b1, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b1.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b1)
    victorias()
    automatico()

def boton2():
    canvas = tk.Canvas(b2, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b2.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b2)
    victorias()
    automatico()

def boton3():
    canvas = tk.Canvas(b3, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b3.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b3)
    victorias()
    automatico()


def boton4():
    canvas = tk.Canvas(b4, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b4.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b4)
    victorias()
    automatico()


def boton5():
    canvas = tk.Canvas(b5, width=208, height=225, bg="white")
    canvas.create_text(104, 112, text="x", font=("Arial", 100), fill="red")
    b5.config(state=tk.NORMAL)
    canvas.grid(row=1, column=1)
    botones.remove(b5)
    victorias()

def boton6():
    canvas = tk.Canvas(b6, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b6.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b6)
    victorias()
    automatico()


def boton7():
    canvas = tk.Canvas(b7, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b7.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b7)
    victorias()
    automatico()


def boton8():
    canvas = tk.Canvas(b8, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b8.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b8)
    victorias()
    automatico()


def boton9():
    canvas = tk.Canvas(b9, width=208, height=225, bg="white")
    canvas.create_oval(60, 60, 150, 150, width=15, outline="green")
    b9.config(state=tk.DISABLED)
    canvas.grid(row=1, column=1)
    botones.remove(b9)
    victorias()
    automatico()

root = tk.Tk()
root.title("Tic Tac Toe")

b1 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton1, foreground="white")
b1.grid(row=0, column=0)

b2 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton2, foreground="white")
b2.grid(row=0, column=1)

b3 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton3, foreground="white")
b3.grid(row=0, column=2)

b4 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton4, foreground="white")
b4.grid(row=1, column=0)

b5 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton5, foreground="white")
b5.grid(row=1, column=1)

b6 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton6, foreground="white")
b6.grid(row=1, column=2)

b7 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton7, foreground="white")
b7.grid(row=2, column=0)

b8 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton8, foreground="white")
b8.grid(row=2, column=1)

b9 = tk.Button(root, text="", width=30, height=15, borderwidth=5, command=boton9, foreground="white")
b9.grid(row=2, column=2)

botones = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
boton5()

root.mainloop()