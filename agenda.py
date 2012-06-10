#!/usr/bin/env python
# _*_ encoding: utf-8 _*_



from Tkinter import *


def add_user():
	f=open('I:\Users\GQ\Documents\GitHub\Agenda\contactos.txt', 'a')
	f.write('Hola que tal')

	top = Tk()
	
	top.minsize(220,220)
	L1 = Label(top, text="Nombre:")
	E1 = Entry(top, bd =5)
	L1.pack(side = TOP)
	E1.pack(side =  TOP)
	
	
	L2 = Label(top, text="Apellido:")
	E2 = Entry(top, bd =5)
	L2.pack(side = TOP)
	E2.pack(side =  TOP)
	
	
	L3 = Label(top, text="Telefono:")
	E3 = Entry(top, bd =5)
	L3.pack(side = TOP)
	E3.pack(side =  TOP)
	
	
	button_add = Button(top, text="Aceptar")
	button_add.pack( side = BOTTOM)
	
	
	
	f.close()
	top.mainloop()
	


ventana = Tk()
ventana.minsize(200,200)
cuadro = Frame(ventana, width =200, height =200, bg="red")
frame = Frame()

button1=Button(frame, text="AÑADIR CONTACTOS", command=add_user)
button1.pack(side=TOP)
button2=Button(frame, text="BUSCAR CONTACTOS")
button2.pack(side=TOP)
button3=Button(frame, text="ELIMINAR CONTACTOS")
button3.pack(side=TOP)
button4=Button(frame, text="MOSTRAR TODOS")
button4.pack(side=TOP)
frame.pack()
frame.mainloop()