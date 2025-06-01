import tkinter as tk

# Variables globales
operacion = None
actual1 = ""

def numeros(num):
    """Agrega un número o punto al campo de entrada."""
    actual = numero.get()
    
    # Evita números como 01, 02 y asegura que no haya múltiples puntos decimales
    if actual == "0" and num != ".":
        numero.set(str(num))
    elif num == "." and "." in actual:
        return
    else:
        numero.set(actual + str(num))

def operacion_click(op):
    """Guarda la primera parte de la operación y prepara el campo de entrada para el segundo número."""
    global actual1, operacion
    actual1 = numero.get()
    operacion = op
    numero.set("")

def igual():
    """Realiza la operación y muestra el resultado."""
    global actual1, operacion
    actual2 = numero.get()
    
    if not actual1 or not actual2:
        return
    
    try:
        num1 = float(actual1)
        num2 = float(actual2)

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                resultado = "Error"
            else:
                resultado = num1 / num2
        else:
            return
        
        numero.set(resultado)
    except:
        numero.set("Error")
    
    operacion = None
    actual1 = ""

def borrar():
    """Limpia el campo de entrada."""
    global actual1, operacion
    numero.set("0")
    actual1 = ""
    operacion = None

def cambiar_signo():
    """Cambia el signo del número en la entrada."""
    actual = numero.get()
    if actual and actual != "0":
        if actual[0] == "-":
            numero.set(actual[1:])
        else:
            numero.set("-" + actual)

# Inicio de la ventana
root = tk.Tk()
root.title("Calculadora")

# Variable para la entrada
numero = tk.StringVar(value="0")

# Campo de entrada
entry = tk.Entry(root, width=15, textvariable=numero, font=("Arial", 25, "bold"), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5)
entry.focus_set()

# Botones numéricos
contador = 6
for q in range(1, 4):
    for w in range(3):
        contador += 1
        botones = tk.Button(root, text=str(contador), font=("Arial", 20), width=2,
                            command=lambda i=contador: numeros(i))
        botones.grid(row=q, column=w)
    contador -= 6

botoncero = tk.Button(root, text="0", font=("Arial", 20), width=2, command=lambda: numeros("0"))
botoncero.grid(row=4, column=0)

# Operaciones
botonsuma = tk.Button(root, text="+", font=("Arial", 20), width=2, command=lambda: operacion_click("+"))
botonsuma.grid(row=1, column=4)

botonresta = tk.Button(root, text="-", font=("Arial", 20), width=2, command=lambda: operacion_click("-"))
botonresta.grid(row=2, column=4)

botonmultiplicar = tk.Button(root, text="*", font=("Arial", 20), width=2, command=lambda: operacion_click("*"))
botonmultiplicar.grid(row=3, column=4)

botondividir = tk.Button(root, text="/", font=("Arial", 20), width=2, command=lambda: operacion_click("/"))
botondividir.grid(row=4, column=4)

# Funciones especiales
botonigual = tk.Button(root, text="=", font=("Arial", 20), width=4, command=igual)
botonigual.grid(row=3, column=3)

botonborrar = tk.Button(root, text="C", font=("Arial", 20), width=2, command=borrar)
botonborrar.grid(row=4, column=1)

botonpunto = tk.Button(root, text=".", font=("Arial", 20), width=2, command=lambda: numeros("."))
botonpunto.grid(row=4, column=2)

botoncambiar = tk.Button(root, text="+/-", font=("Arial", 20), width=4, command=cambiar_signo)
botoncambiar.grid(row=4, column=3)

root.mainloop()
