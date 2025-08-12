import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="Black")
        icono = tk.PhotoImage(file=r"C:\Users\Luis Reyes\Downloads\fotoiconcalculadora.png")
        self.root.iconphoto(False, icono)

    def entradas(self):
        self.entry1 = tk.Entry(self.root, width=10, font=("Arial", 15, "bold"), borderwidth=4)
        self.entry1.grid(row=1, column=0)
        self.entry1.focus_set()

        self.entry2 = tk.Entry(self.root, width=10, font=("Arial", 15, "bold"), borderwidth=4)
        self.entry2.grid(row=1, column=2)

    def radiobotones(self):
        self.valor = tk.IntVar()
        self.valor.set(1)

        radiobotonsuma = tk.Radiobutton(self.root, text="+", variable=self.valor, value=1, font=("Arial", 15, "bold"), bg="black", foreground="gold")
        radiobotonsuma.grid(row=0, column=1)
        
        radiobotonresta = tk.Radiobutton(self.root, text="-", variable=self.valor, value=2, font=("Arial", 15, "bold"), bg="black", foreground="gold")
        radiobotonresta.grid(row=1, column=1)

        radiobotonmultiplicacion = tk.Radiobutton(self.root, text="*", variable=self.valor, value=3, font=("Arial", 15, "bold"), bg="black", foreground="gold")
        radiobotonmultiplicacion.grid(row=2, column=1)

        radiobotondivision = tk.Radiobutton(self.root, text="/", variable=self.valor, value=4, font=("Arial", 15, "bold"), bg="black", foreground="gold")
        radiobotondivision.grid(row=3, column=1)

    def info(self, operacion, signo, resultado):
        messagebox.showinfo("Resultado", f"{operacion} de {self.entry1.get()} {signo} {self.entry2.get()} = {resultado}")

    def operaciones(self, *args):
        try:
            if self.valor.get() == 1:
                suma = float(self.entry1.get()) + float(self.entry2.get())
                self.info("Suma", "+", suma)
            elif self.valor.get() == 2:
                resta = float(self.entry1.get()) - float(self.entry2.get())
                self.info("Resta", "-", resta)
            elif self.valor.get() == 3:
                multiplicacion = float(self.entry1.get()) * float(self.entry2.get())
                self.info("Multiplicacion", "x", multiplicacion)
            else:
                division = float(self.entry1.get()) / float(self.entry2.get())
                self.info("Division", "/", division)
        except ValueError:
            messagebox.showerror("Error", "Solo numeros")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")

    def botonresultados(self):
        boton = tk.Button(self.root, text="Evaluar", font=("Arial", 12, "bold"), command=self.operaciones, background="black", foreground="gold", borderwidth=10)
        self.root.bind("<Return>", self.operaciones)
        boton.grid(row=4, column=1)

    def todo(self):
        self.entradas()
        self.radiobotones()
        self.botonresultados()

root = tk.Tk()
cal = Calculadora(root)
cal.todo()
root.mainloop()