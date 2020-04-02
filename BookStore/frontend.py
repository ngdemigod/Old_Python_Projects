from tkinter import *
import backend #imports functions from backend.py

def get_selected_row(event):
    try:
        global selected_tuple #global (keyword) makes selected_tuple a global variable that can be used outside the function 
        index=list1.curselection()[0] #curselection - grabs the user's selected row from the listbox and Index variable will hold the id number for that selected row
        selected_tuple=list1.get(index) #saves the selected row (in tuple form) to the variable 
        
        e1.delete(0,END) #this will clear out any text in the entry text box
        e1.insert(END,selected_tuple[1]) #inserts the selected row's title (2nd tuple item) when the row is selected from listbox
        
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2]) #inserts the selected row's author (3rd tuple item) when the row is selected from listbox
        
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3]) #inserts the selected row's year (4th tuple item) when the row is selected from listbox
        
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])  #inserts the selected row's isbn (5th tuple item) when the row is selected from listbox
    except IndexError:
        pass

def view_command():
    list1.delete(0,END) #this will clear out the listbox content
    for row in backend.view():
        list1.insert(END,row) #displays results in listbox


def search_command():
    list1.delete(0,END)

    ### for loop that performs the backend search function using the inputted text in the entry boxes ###
    for row in backend.search(title_Text.get(),author_Text.get(),year_Text.get(),isbn_Text.get()):
        list1.insert(END,row)


def insert_command():
    backend.insert(title_Text.get(),author_Text.get(),year_Text.get(),isbn_Text.get()) #performs backend insert function inputs from entry boxes
    list1.delete(0,END)
    list1.insert(END,(title_Text.get(),author_Text.get(),year_Text.get(),isbn_Text.get()))
    

def update_command():
    backend.update(selected_tuple[0],title_Text.get(),author_Text.get(),year_Text.get(),isbn_Text.get()) #performs backend update function
    ### uses the id from selected_tuple to identity row & replaces data with inputs from entry boxes
    


def delete_command():
    backend.delete(selected_tuple[0]) #performs backend delete function on the selected row in listbox


window=Tk() #Tk() - used to create the root window for the GUI (i.e. assigned to the window variable)

l1=Label(window,text='Title') #Label() - creates a widget to display some short text or image
l1.grid(row=0,column=0) #.grid() - used to determine the placement of the widget in the root window

l2=Label(window,text='Author')
l2.grid(row=0,column=2)

l3=Label(window,text='Year')
l3.grid(row=1,column=0)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

title_Text=StringVar() #StringVar() - creates an empty string to hold a string variable in tkinter 
e1=Entry(window,textvariable=title_Text) #Entry() - create entry text box
e1.grid(row=0,column=1)

author_Text=StringVar()
e2=Entry(window,textvariable=author_Text)
e2.grid(row=0,column=3)

year_Text=StringVar()
e3=Entry(window,textvariable=year_Text)
e3.grid(row=1,column=1)

isbn_Text=StringVar()
e4=Entry(window,textvariable=isbn_Text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35) #Listbox - creates a listbox widget
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window) #Scrollbar - creates a scrollbar widget
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set) #yscrollcommand - links the listbox vertical scrolling command with the scrollbar 
sb1.configure(command=list1.yview) #.yview() - sets scrollbar to perform changes the vertical position of the listbox

### Selecting a row from listbox triggers an event (i.e <<ListboxSelect>>) which passes that row into the get_selected_row function ###
list1.bind('<<ListboxSelect>>',get_selected_row) #bind (TK Keyword) - binds a function to a event

b1=Button(window,text="View All", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry", width=12,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy) #.destroy() - terminates root window
b6.grid(row=7,column=3)

window.mainloop() #mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed

