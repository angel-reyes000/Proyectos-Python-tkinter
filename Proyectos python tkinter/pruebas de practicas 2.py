import tkinter as tk

def numeros():
    global botones
    global actual1
    actual1 = numero.get()
    numero.set(str(actual1) + str(b1.cget("text")))

def numeros2():
    global actual2
    actual2 = numero2.get()
    numero2.set(str(actual2) + str(1))

def suma():
    b1.config(command=numeros2)
    entry.config(textvariable=numero2)
    entry.delete(0, tk.END)

def igual():
    valor1 = numero.get()
    valor2 = numero2.get()
    resultado.set(int(valor1) + int(valor2))
    entry.config(textvariable=resultado)

#Inicio de root
root = tk.Tk()
root.title("Calculadora")

numero = tk.StringVar()
numero2 = tk.StringVar()
resultado = tk.IntVar()

entry = tk.Entry(root, width=15, textvariable=numero, font=("Arial", 25, "bold"), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5)
entry.focus_set()

#Numeros
contador=6
b1 = tk.Button(root, text=1, font=("Arial", 20), width=1, command=numeros)
b1.grid(row=1, column=1)

b2 = tk.Button(root, text=2, font=("Arial", 20), width=2, command=numeros)
b2.grid(row=1, column=2)

botoncero = tk.Button(root, text="0", font=("Arial", 20), width=2, command=lambda i = "0": numeros(i))
botoncero.grid(row=4, column=0)

for q in range(2):
    labels = tk.Label(root, width=8, bg="red")
    labels.grid(row=1+q, column=3)

botonsuma = tk.Button(root, text="+", font=("Arial", 20), width=2, command=suma)
botonsuma.grid(row=1, column=4)

botonresta = tk.Button(root, text="-", font=("Arial", 20), width=2)
botonresta.grid(row=2, column=4)

botonigual = tk.Button(root, text="=", font=("Arial", 20), width=4, command=igual)
botonigual.grid(row=3, column=3)

botonmultiplicar = tk.Button(root, text="*", font=("Arial", 20), width=2)
botonmultiplicar.grid(row=3, column=4)

botones = [b1, b2]

root.mainloop()