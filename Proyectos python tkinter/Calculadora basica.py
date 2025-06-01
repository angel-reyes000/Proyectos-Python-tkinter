import tkinter as tk
from tkinter import messagebox

def operaciones():
    try:
        if entry1.get().isdigit() or float(entry1.get()) and entry2.get().isdigit() or float(entry2.get()): 
            if valor.get() == 1:
                messagebox.showinfo("Suma", f"Resultado: {float(entry1.get()) + float(entry2.get())}")
            elif valor.get() == 2:
                messagebox.showinfo("Resta",f"Resultado: {float(entry1.get()) - float(entry2.get())}")
            elif valor.get() == 3:
                messagebox.showinfo("Multiplicacion", f"Resultado: {float(entry1.get()) * float(entry2.get())}")
            else:
                messagebox.showinfo("Division", f"Resultado: {float(entry1.get()) / float(entry2.get())}")
    except ValueError:
        messagebox.showerror("Error", "Valido solo numeros\nSin espacios en blanco")
        if entry1.get() == str:
                entry1.focus_set()
        else:
            entry2.focus_set()
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero")
        if entry1.get() == str:
                entry1.focus_set()
        else:
            entry2.focus_set()

root = tk.Tk()
root.title("Calculadora")
root.config(bg="light gray")

entry1 = tk.Entry(root, width=20, takefocus=1)
entry1.grid(row=1, column=1)
entry1.focus_set()

entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=3)

valor = tk.IntVar()
valor.set(1)

suma = tk.Radiobutton(root, text="+", variable=valor, value=1, width=2, bg="light gray")
suma.grid(row=0, column=2)

resta = tk.Radiobutton(root, text="-", variable=valor, value=2, width=2, bg="light gray")
resta.grid(row=1, column=2)

multiplicar = tk.Radiobutton(root, text="*", variable=valor, value=3, width=2, bg="light gray")
multiplicar.grid(row=2, column=2)

dividir = tk.Radiobutton(root, text="/", variable=valor, value=4, width=2, bg="light gray")
dividir.grid(row=3, column=2)

boton = tk.Button(root, text="Evaluar", command=operaciones)
boton.grid(row = 5, column= 2)

root.mainloop()

l = [2,4,51,1]
l = sorted(l)
print(l)
