from tkinter import *
from tkinter import ttk
from tkinter import filedialog
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(frm, text="Bienvenido").grid(column=0, row=0)
ttk.Label(frm, text ='el texto a leer:').grid(column=0,row=1)

btn = ttk.Button(frm,text= 'Abrir',command=filedialog.askopenfilename).grid(column=1, row=2)
ttk.Button(frm, text="Cerrar", command=root.destroy).grid(column=1, row=3)


root.mainloop()
