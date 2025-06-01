import tkinter as tk

fases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

def salir():
    root.destroy()

def colores():
    global contador
    contador+=1
    match contador:
        case 1:
            canvas.itemconfig(c1, fill = "red")
            canvas.itemconfig(c2, fill = "gray")
        case 2:
            canvas.itemconfig(c2, fill = "yellow")
        case 3:
            canvas.itemconfig(c3, fill = "green")
            canvas.itemconfig(c2, fill = "gray")
            canvas.itemconfig(c1, fill = "gray")
        case 4:
            canvas.itemconfig(c3, fill="gray")
            canvas.itemconfig(c2, fill="yellow")
    if contador == 4:
        contador = 0

contador = 0

root = tk.Tk()

canvas = tk.Canvas(width=250, height=605, bg="gray")
canvas.pack()

c1 = canvas.create_oval(225, 200, 30, 10, width=4)
c2 = canvas.create_oval(225, 400, 30, 210, width=4)
c3 = canvas.create_oval(225, 600, 30, 410, width=4)

boton1 = tk.Button(root, text="Next", command=colores)
boton1.pack()
boton2 = tk.Button(root, text="Quit", command=salir)
boton2.pack()

root.mainloop()

for q in range(1, 10):
        print("b"+str(q)+".cget('status') == tk.DISABLED or", end=" ")

def otra_forma():
    fases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

    def salir():
        root.destroy()

    def colores():
        global contador
        contador+=1
        for q in fases:
            if q == (True, False, False) and contador == 1:
                canvas.itemconfig(c1, fill = "red")
            elif q == (True, True, False) and contador == 2:
                canvas.itemconfig(c2, fill = "yellow")
            elif q == (False, False, True) and contador == 3:
                canvas.itemconfig(c3, fill = "green")
                canvas.itemconfig(c2, fill = "gray")
                canvas.itemconfig(c1, fill = "gray")
            elif q == (False, True, False) and contador == 4:
                canvas.itemconfig(c2, fill = "yellow")
                canvas.itemconfig(c3, fill = "gray")
                contador-=4

    contador = 0

    root = tk.Tk()

    canvas = tk.Canvas(width=250, height=605, bg="gray")
    canvas.pack()

    c1 = canvas.create_oval(225, 200, 30, 10, width=4)
    c2 = canvas.create_oval(225, 400, 30, 210, width=4)
    c3 = canvas.create_oval(225, 600, 30, 410, width=4)

    boton1 = tk.Button(root, text="Next", command=colores)
    boton1.pack()
    boton2 = tk.Button(root, text="Quit", command=salir)
    boton2.pack()

    root.mainloop()