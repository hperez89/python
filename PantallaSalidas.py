#!/usr/bin/python3
from tkinter import *
from tkinter import font
import time

""" entorno grafico """
ventana = Tk()
ventana.title("SPSI")
ventana.configure(background='white')
ventana.minsize(1280, 720)
canvas = Canvas(width=1280, height=720, bg='white')
canvas.pack(expand=YES, fill=BOTH)

imgSPSI = PhotoImage(file = "C:\\Users\\SPSI\\Desktop\\CEREZA Santa Catalina 2019\\img\\spsi.png")
imgSCatalina = PhotoImage(file = "C:\\Users\\SPSI\\Desktop\\CEREZA Santa Catalina 2019\\img\\santa_catalina.png")

im1 = Label(ventana, image=imgSPSI)
im1.place(x=1, y=1)
im2 = Label(ventana, image=imgSCatalina)
im2.place(x=1062, y=1)

canvas.create_line(0, 95, 1280, 95)
canvas.create_line(640, 95, 640, 720)

variedad = Label(ventana,text="Variedad: SWEET HEART", font=("Agency FB", 24), bg="white", fg="black").place(x=140, y=10)
loteproceso = Label(ventana,text="Lote: 103 Proceso: 29", font=("Agency FB", 20), bg="white", fg="black").place(x=140, y=45)
productor = Label(ventana,text="Prod.: ", font=("Agency FB", 20), bg="white", fg="black").place(x=530, y=10)
productortxt = Label(ventana,text="(000000)Productor Ejemplo", font=("Agency FB", 20), bg="white", fg="black").place(x=610, y=10)
exportador = Label(ventana,text="Exp.: ", font=("Agency FB", 20), bg="white", fg="black").place(x=530, y=45)
exportadortxt = Label(ventana,text="(000000)Exportador Ejemplo", font=("Agency FB", 20), bg="white", fg="black").place(x=610, y=45)

salida1 = Label(ventana,text="Salida 1", font=("Agency FB", 36), bg="white", fg="black").place(x=200, y=110)
salida2 = Label(ventana,text="Salida 2", font=("Agency FB", 36), bg="white", fg="black").place(x=200+640, y=110)

embalaje1 = Label(ventana,text="PL5KGM", font=("Agency FB", 36), bg="white", fg="black").place(x=190, y=200)
embalaje2 = Label(ventana,text="COMCAR", font=("Agency FB", 36), bg="white", fg="black").place(x=190+640, y=200)

calibre1 = Label(ventana,text="XLD", font=("Agency FB", 200), bg="white", fg="black").place(x=50, y=310)
calibre2 = Label(ventana,text="PL", font=("Agency FB", 200), bg="white", fg="black").place(x=150+640, y=310)

ventana.mainloop()
