from tkinter import *

ventana = Tk()
ventana.title("Calculadora Python")
ventana.geometry("365x345")
ventana.resizable(False,False)
ventana.configure(background="gray")


#Declarar Funciones
operacion = ""
resultado = StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,END)


def click(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0,operacion)

def calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado = "Error"
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0,resultado)


#Display de los resultados
pantalla = Entry(ventana,font=("arial", 20, "bold"), borderwidth=2)
pantalla.grid(row=0, column=0, columnspan=3,pady=10,padx=5)

#Boton de reiniciar operaciones
boton_reset = Button(ventana,text="AC", width=5, height=2, command=lambda:borrar())
boton_reset.grid(row=0,column=3,pady=10)

#Definimos el ancho y alto de los botones
ancho = 5
alto = 2

#Botones de la fila 1,  numeros del 1 al 4
boton7 = Button(ventana, text="7", width=ancho, height=alto, command=lambda:click("7"))
boton7.grid(row=1,column=0,padx=5, pady=10)

boton8 = Button(ventana, text="8", width=ancho, height=alto, command=lambda:click("8"))
boton8.grid(row=1,column=1,padx=5, pady=10)

boton9 = Button(ventana, text="9", width=ancho, height=alto, command=lambda:click("9"))
boton9.grid(row=1,column=2,padx=5, pady=10)

botonmult = Button(ventana, text="X", width=ancho, height=alto, command=lambda:click("*"))
botonmult.grid(row=1,column=3,padx=5, pady=10)


#Botones de la fila 2, numeros del 5 al 8
boton4 = Button(ventana, text="4", width=ancho, height=alto, command=lambda:click("4"))
boton4.grid(row=2,column=0,padx=5, pady=10)

boton5 = Button(ventana, text="5", width=ancho, height=alto, command=lambda:click("5"))
boton5.grid(row=2,column=1,padx=5, pady=10)

boton6 = Button(ventana, text="6", width=ancho, height=alto, command=lambda:click("6"))
boton6.grid(row=2,column=2,padx=5, pady=10)

botonmenos = Button(ventana, text="-", width=ancho, height=alto, command=lambda:click("-"))
botonmenos.grid(row=2,column=3,padx=5, pady=10)

#Botones de la fila 3; 9,0, . , +
boton1 = Button(ventana, text="1", width=ancho, height=alto, command=lambda:click("1"))
boton1.grid(row=3,column=0,padx=5, pady=10)

boton2 = Button(ventana, text="2", width=ancho, height=alto, command=lambda:click("2"))
boton2.grid(row=3,column=1,padx=5, pady=10)

boton3 = Button(ventana, text="3", width=ancho, height=alto, command=lambda:click("3"))
boton3.grid(row=3,column=2,padx=5, pady=10)

botonmas = Button(ventana, text="+", width=ancho, height=alto, command=lambda:click("+"))
botonmas.grid(row=3,column=3,padx=5, pady=10)

#Botones de la fila 4; -, X, / , =
botondiv = Button(ventana, text="/", width=ancho, height=alto, command=lambda:click("/"))
botondiv.grid(row=4,column=0,padx=5, pady=10)

boton0 = Button(ventana, text="0", width=ancho, height=alto, command=lambda:click("0"))
boton0.grid(row=4,column=1,padx=5, pady=10)

botonpunto = Button(ventana, text=".", width=ancho, height=alto, command=lambda:click("."))
botonpunto.grid(row=4,column=2,padx=5, pady=10)

botonigual = Button(ventana, text="=", width=ancho, height=alto, command=lambda:calcular())
botonigual.grid(row=4,column=3,padx=5, pady=10)


ventana.mainloop()

