import tkinter as tk
import random

def detener():
    label.after_cancel(labelid)
            
def tiempo():
    global contador
    contador+=1
    label.config(text=contador)
    if len(lista)>0:
        label.after(1000, tiempo)
    else:
        detener()    

def menor_mayor(*args):
    global lista
    minimo = 1000
    for q in lista:
        if q.cget("text") < minimo:
            minimo = q.cget("text")
    for w in lista:
        if w.cget("text") == minimo:
            w.config(state=tk.DISABLED)
            if w.cget("text") == minimo:
                w.config(state=tk.DISABLED)
                lista.remove(w)
                

contador = 0

root = tk.Tk()

b1 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b1.bind("<Button-1>", menor_mayor)
b1.grid(row=0, column=0)

b2 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b2.bind("<Button-1>", menor_mayor)
b2.grid(row=0, column=1)

b3 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b3.bind("<Button-1>", menor_mayor)
b3.grid(row=0, column=2)

b4 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b4.bind("<Button-1>", menor_mayor)
b4.grid(row=0, column=3)

b5 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b5.bind("<Button-1>", menor_mayor)
b5.grid(row=0, column=4)

b6 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b6.bind("Button-1", menor_mayor)
b6.grid(row=1, column=0)

b7 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b7.bind("Button-1", menor_mayor)
b7.grid(row=1, column=1)

b8 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b8.bind("Button-1", menor_mayor)
b8.grid(row=1, column=2)

b9 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b9.bind("Button-1", menor_mayor)
b9.grid(row=1, column=3)

b10 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b10.bind("<Button-1>", menor_mayor)
b10.grid(row=1, column=4)

b11 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b11.bind("<Button-1>", menor_mayor)
b11.grid(row=2, column=0)

b12 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b12.bind("<Button-1>", menor_mayor)
b12.grid(row=2, column=1)

b13 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b13.bind("<Button-1>", menor_mayor)
b13.grid(row=2, column=2)

b14 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b14.bind("<Button-1>", menor_mayor)
b14.grid(row=2, column=3)

b15 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b15.bind("<Button-1>", menor_mayor)
b15.grid(row=2, column=4)

b16 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b16.bind("<Button-1>", menor_mayor)
b16.grid(row=3, column=0)

b17 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b17.bind("<Button-1>", menor_mayor)
b17.grid(row=3, column=1)

b18 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b18.bind("<Button-1>", menor_mayor)
b18.grid(row=3, column=2)

b19 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b19.bind("<Button-1>", menor_mayor)
b19.grid(row=3, column=3)

b20 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b20.bind("<Button-1>", menor_mayor)
b20.grid(row=3, column=4)

b21 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b21.bind("<Button-1>", menor_mayor)
b21.grid(row=4, column=0)

b22 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b22.bind("<Button-1>", menor_mayor)
b22.grid(row=4, column=1)

b23 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b23.bind("<Button-1>", menor_mayor)
b23.grid(row=4, column=2)

b24 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b24.bind("<Button-1>", menor_mayor)
b24.grid(row=4, column=3)

b25 = tk.Button(root, text=random.randint(1,999), width=20, height=2, font=("Arial", "10"), state=tk.NORMAL)
b25.bind("<Button-1>", menor_mayor)
b25.grid(row=4, column=4)

lista = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25]

label = tk.Label(root, text=contador)
label.grid(row=5, column=2)

if len(lista) > 0:
    labelid = label.after(1000, tiempo)
else:
    detener()

root.mainloop()


#l = [x for x in range(0, 26)]
#for q in l:
#    print("b"+str(q)+".cget('text')", end=", ")

#for q in range(1,25):
#    print("b"+str(q), end=", ")