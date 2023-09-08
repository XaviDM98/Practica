import pymongo
from tkinter import *

ventana=Tk()
ventana.minsize(500,500)
ventana.maxsize(500,500)
ventana.title("tkinter")
ventana.config(bg="lightblue")

nombrev=StringVar()
apellidov=StringVar()
edadv=StringVar()
cedulav=StringVar()
telefonov=StringVar()

def sub():
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['gui']
    collection=db["priyansu"]
    dic={
        'nombre': nombrev.get(),    
        'apellido': apellidov.get(),
        'edad': edadv.get(),
        'cedula': cedulav.get(),
        'telefono': telefonov.get()

    }
    collection.insert_one(dic)

head=Label(text="Veterinaria Clínica Salud Animal", font=("Roboto Mono",15),bg="cyan", fg="black")
head.place(x=125, y=10) 

nombre=Label(text="Nombre: ", font=("Roboto Mono", 12), bg="lightblue", fg="black")
nombre.place(x=20, y=50)
e=Entry(font=("Roboto Mono", 12), text=nombrev,borderwidth=1, width=50)
e.place(x=20, y=75)

apellido=Label(text="Apellido: ", font=("Roboto Mono", 12), bg="lightblue", fg="black")
apellido.place(x=20, y=100)
e=Entry(font=("Roboto Mono", 12), text=apellidov, borderwidth=1, width=50)
e.place(x=20, y=125)

edad=Label(text="Edad: ", font=("Roboto Mono", 12), bg="lightblue", fg="black")
edad.place(x=20, y=150)
e=Entry(font=("Roboto Mono", 12), text=edadv, borderwidth=1, width=50)
e.place(x=20, y=175)

cedula=Label(text="Cédula: ", font=("Roboto Mono", 12), bg="lightblue", fg="black")
cedula.place(x=20, y=200)
e=Entry(font=("Roboto Mono", 12), text=cedulav, borderwidth=1, width=50)
e.place(x=20, y=225)

telefono=Label(text="Teléfono: ", font=("Roboto Mono", 12), bg="lightblue", fg="black")
telefono.place(x=20, y=250)
e=Entry(font=("Roboto Mono", 12), text=telefonov, borderwidth=1, width=50)
e.place(x=20, y=275)


boton=Button(text="Ingresar", font=("Roboto Mono",12), command=sub)
boton.place(x=350, y=350)

ventana.mainloop()
