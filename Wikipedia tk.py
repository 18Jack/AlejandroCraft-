
from tkinter import*
import wikipedia as wiki

def clear():
    my_entry.delete(0,END)
    my_text.delete(0.0,END)

def search():
    wiki.set_lang("es")
    data= wiki.page(my_entry.get())
    my_text.insert(0.0, data.title)
    my_text.insert(1.1, data.content)


root=Tk()
root.title("Wikipedia")
root.geometry("680x615")
root.config(bg="aquamarine")

my_label= LabelFrame(root,text="Buscar en Wikipedia")
my_label.pack(pady=20)

my_entry= Entry(my_label,font=("Helvitica,18"),width=47)
my_entry.pack(pady=20,padx=20)

my_frame= Frame(root)
my_frame.pack(pady=5)

text_scroll= Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
hor_scroll= Scrollbar(my_frame,orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)

my_text= Text(my_frame,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.xview)

#Botones
boton=Frame(root)
boton.pack(pady=10)
buscar= Button(boton,text="Buscar", font=("Helvita",15),command=search)
buscar.grid(row=0, column=0, padx=20)

borrar= Button(boton,text="Borrar", font=("Helvita",15),command=clear)
borrar.grid(row=0, column=1)

cerrar= Button(boton,text="Cerrar", font=("Helvita",15),command=root.destroy)
cerrar.grid(row=0, column=2,padx=20)

root.mainloop()
