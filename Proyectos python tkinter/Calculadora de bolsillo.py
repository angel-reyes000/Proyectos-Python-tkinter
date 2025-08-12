import tkinter as tk

#Calculadora funcional sin teclado y solo clicks.
#Numeros del 0 al 9, operaciones basicas y cambio de signo en valores.

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.resizable(height = False, width = False)
        self.root.config(background="black")

    def Entrada(self):
        self.PrimerValor = tk.StringVar()
        self.entrada = tk.Entry(self.root, width=10, font=("Arial", 35, "bold"), justify="right", textvariable=self.PrimerValor, borderwidth=6, relief="ridge", background="black", foreground="light gray")
        self.entrada.grid(row=0, column=0, columnspan=10, pady=5)
        self.entrada.focus_set()

    def BotonesNumeros(self):
        self.ListaBotones = []
        contador = 7
        for fila in range(3):
            for columna in range(3):
                boton = tk.Button(self.root, text=str(columna + contador), font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
                boton.bind("<Button-1>", lambda event, b=boton: self.PrimerValor.set(str(self.PrimerValor.get()) + str(b.cget("text"))))
                boton.grid(row=fila + 2, column=columna)
            contador-=3
        botoncero = tk.Button(self.root, text=0, font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        botoncero.bind("<Button-1>", lambda event, b=botoncero: self.PrimerValor.set(str(self.PrimerValor.get() + str(b.cget("text")))))
        botoncero.grid(row=5, column=0)

    def BotonesOperaciones(self):
        BotonBorrar = tk.Button(self.root, text="C", font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonBorrar.bind("<Button-1>", lambda event, b=BotonBorrar: self.Operaciones(b.cget("text")))
        BotonBorrar.grid(row=5, column=1)
        BotonComa = tk.Button(self.root, text=".", font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonComa.bind("<Button-1>", lambda event, b=BotonComa: self.PrimerValor.set(str(self.PrimerValor.get() + str(b.cget("text")))))
        BotonComa.grid(row=5, column=2)

        BotonCambiarOperacion = tk.Button(self.root, text="+/-", font=("Arial", 12), width=7, height=7, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonCambiarOperacion.bind("<Button-1>", lambda event, b=BotonCambiarOperacion: self.Operaciones(b.cget("text")))
        BotonCambiarOperacion.grid(row=2, column=3, rowspan=2)
        BotonIgual = tk.Button(self.root, text="=", font=("Arial", 12), width=7, height=7, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonIgual.bind("<Button-1>", lambda event, b=BotonIgual: self.Resultado())
        BotonIgual.grid(row=4, column=3, rowspan=2)

        BotonSuma = tk.Button(self.root, text="+", font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonSuma.bind("<Button-1>", lambda event, b=BotonSuma: self.Operaciones(b.cget("text")))
        BotonSuma.grid(row=1, column=0)
        BotonResta = tk.Button(self.root, text="-", font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonResta.bind("<Button-1>", lambda event, b=BotonResta: self.Operaciones(b.cget("text")))
        BotonResta.grid(row=1, column=1)
        BotonMultiplicacion = tk.Button(self.root, text="*", font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonMultiplicacion.bind("<Button-1>", lambda event, b=BotonMultiplicacion: self.Operaciones(b.cget("text")))
        BotonMultiplicacion.grid(row=1, column=2)
        BotonDivision = tk.Button(self.root, text="/", font=("Arial", 12), width=7, height=3, background="black", foreground="white", borderwidth=2, relief="ridge")
        BotonDivision.bind("<Button-1>", lambda event, b=BotonDivision: self.Operaciones(b.cget("text")))
        BotonDivision.grid(row=1, column=3)

    def VariablesEntradas(self):
        self.SegundoValor = self.PrimerValor.get()
        self.PrimerValor.set("")
        self.entrada.config(textvariable=self.PrimerValor)

    def Operaciones(self, signo, *args):
        self.signo = signo
        if self.signo == "+" or self.signo == "-" or self.signo == "/" or signo == "*":
            self.VariablesEntradas()
            self.sumaresta = self.signo
        elif self.signo == "C":
            self.PrimerValor.set("")
        elif self.signo == "+/-":
            texto = self.PrimerValor.get()
            texto = list(texto)
            if "-" in texto:
                texto.remove("-")
                texto = "".join(texto)
                self.PrimerValor.set(texto)
            else:
                texto.insert(0, "-")
                texto = "".join(texto)
                self.PrimerValor.set(texto)

    def Resultado(self):
        self.signo = self.sumaresta
        try:
            match self.signo:
                case "+":
                    self.resultado = float(self.SegundoValor) + float(self.PrimerValor.get())
                    self.PrimerValor.set(self.resultado)
                case "-":
                    self.resultado = float(self.SegundoValor) - float(self.PrimerValor.get())
                    self.PrimerValor.set(self.resultado)
                case "/":
                    self.resultado = float(self.SegundoValor) / float(self.PrimerValor.get())
                    self.PrimerValor.set(self.resultado)
                case "*":
                    self.resultado = float(self.SegundoValor) * float(self.PrimerValor.get())
                    self.PrimerValor.set(self.resultado)
        except ZeroDivisionError as z:
            self.PrimerValor.set("Error! 0")
        except Exception:
            self.PrimerValor.set("Error!")
    
    def Todo(self):
        self.Entrada()
        self.BotonesNumeros()
        self.BotonesOperaciones()

root = tk.Tk()
c = Calculadora(root)
c.Todo()
root.mainloop()