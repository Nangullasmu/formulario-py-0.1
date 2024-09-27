import tkinter as tk
from tkinter import messagebox
import re

def lc():
    tbN.delete(0,tk.END)
    tbA.delete(0,tk.END)
    tbE.delete(0,tk.END)
    tbS.delete(0,tk.END)
    tbT.delete(0,tk.END)
    gen.set(0)

def bf():
    lc()
    
def gv():
    nom=tbN.get()
    ape=tbA.get()
    eda=tbE.get()
    est=tbS.get()
    tel=tbT.get()

    Gen=""
    if gen.get()==1:
        Gen="Hombre"
    elif gen.get==2:
        Gen="Mujer"
        
    if(ev(eda) and dv(est) and ev10(tel) and tv(nom) and tv(ape)):        
        d="Nombre: "+nom+"\n"+"Apellido: "+ape+"\n"+"Edad: "+eda+"\n"+"Estatura: "+est+"\n"+"Telefono: "+tel+"\n"+"Genero: "+Gen+"\n"
        with open("C:/Users/perez/OneDrive/Documentos/tareas semestre 3/Programacion Avanzada/python/datosformulario.txt","a") as arc:
            arc.write(d+"\n\n")
        messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n"+d)
        lc()
    else:
        messagebox.showerror("Error", "verifica los datos ingresados")

def ev(raiz):
    try:
        int(raiz)
        return True
    except ValueError:
        return False

def dv(raiz):
    try:
        float(raiz)
        return True
    except ValueError:
        return False

def ev10(raiz):
    return raiz.isdigit() and len(raiz)==10

def tv(raiz):
    return bool(re.match("^[a-zA-Z\s]+$", raiz))
    
raiz=tk.Tk()
raiz.geometry("520x500")
raiz.title("Formulario")
gen=tk.IntVar()

lbN=tk.Label(raiz, text="Nombre: ")
lbN.pack()
tbN=tk.Entry()
tbN.pack()

lbA=tk.Label(raiz, text="Apellido: ")
lbA.pack()
tbA=tk.Entry()
tbA.pack()

lbE=tk.Label(raiz, text="Edad: ")
lbE.pack()
tbE=tk.Entry()
tbE.pack()

lbS=tk.Label(raiz, text="Estatura: ")
lbS.pack()
tbS=tk.Entry()
tbS.pack()

lbT=tk.Label(raiz, text="Telefono: ")
lbT.pack()
tbT=tk.Entry()
tbT.pack()

lbG=tk.Label(raiz, text="Genero")
lbG.pack()
rbH=tk.Radiobutton(raiz, text="Hombre", variable=gen, value=1)
rbH.pack()
rbM=tk.Radiobutton(raiz, text="Mujer", variable=gen, value=2)
rbM.pack()

btnb=tk.Button(raiz, text="Borrar valores", command=bf)
btnb.pack()

btng=tk.Button(raiz, text="Guardar", command=gv)
btng.pack()

raiz.mainloop()
