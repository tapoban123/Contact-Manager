from tkinter import *

root= Tk()
root.geometry('800x700')
root.title('Contact Manager')

def fill_details():
    top=Toplevel(bg='#F0DC82')
    top.geometry('700x400')
    top.title('Contact Manager')
    Label(top,text='Contact Manager',font=('Segoe UI Black',30),bg='#F0DC82').place(x=180,y=10)

    Button(top, text="Add Contact",font=('Malgun Gothic Bold',18),padx=52,pady=5,borderwidth=5,command=add_rec).place(x=20,y=100)

    Button(top, text="Delete Contact",font=('Malgun Gothic Bold',18),padx=40,pady=5,borderwidth=5,command=delete_rec).place(x=20,y=200)

    Button(top, text="Edit Contact",font=('Malgun Gothic Bold',18),padx=56,pady=5,borderwidth=5,command=edit_rec).place(x=400,y=100)

    Button(top, text="View all Contacts",font=('Malgun Gothic Bold',18),padx=28,pady=5,borderwidth=5, command=view_all).place(x=400,y=200)

    Button(top,text='Exit',font=('Malgun Gothic Bold',18),padx=296,pady=5,borderwidth=5,command=root.quit).place(x=20,y=300)


def  add_rec():
    top_add = Toplevel()
    top_add.title('Add a Contact')
    top_add.geometry('500x400')

def delete_rec():
    top_delete = Toplevel()
    top_delete.title('Delete a Contact')
    top_delete.geometry('500x400')

def edit_rec():
    top_edit = Toplevel()
    top_edit.title('Edit a Contact')
    top_edit.geometry('500x400')

def view_all():
    top_view_all = Toplevel()
    top_view_all.title('All Contacts')
    top_view_all.geometry('500x400')


text1 = "Contact Manager \n\n\n\n\n\n\nClick Anywhere to Continue"

myButton_begin =Button(root,text=text1,font=('Calibri',35),bg='#BF94E4',padx=600,pady=600,command=fill_details)

myButton_begin.pack()

root.mainloop()