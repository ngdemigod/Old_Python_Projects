from tkinter import *

window=Tk()

def kg_to_grams():
    grams=float(e1_value.get())*1000
    g1.delete("1.0",END)
    g1.insert(END,grams)
    
    pounds=float(e1_value.get())*2.20462
    p1.delete("1.0",END)
    p1.insert(END,pounds)

    ounces=float(e1_value.get())*35.274
    o1.delete("1.0",END)
    o1.insert(END,ounces)

kg_label=Label(window,text='Kg')
kg_label.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text='Convert',command=kg_to_grams)
b1.grid(row=0,column=2)

g1=Text(window,height=1,width=10)
g1.grid(row=1,column=0)

p1=Text(window,height=1,width=10)
p1.grid(row=1,column=1)

o1=Text(window,height=1,width=10)
o1.grid(row=1,column=2)

window.mainloop()