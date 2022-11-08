from tkinter import *
import sqlite3

root= Tk()
root.geometry('800x700')
root.title('Contact Manager')

conn = sqlite3.connect("Contacts_Mng.db")
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS CONTACT_RECS
    (
        CONTACT_ID int(5) PRIMARY KEY,
        CONACT_FIRST_NAME VARCHAR(40) NOT NULL, 
        CONTACT_NUMBER INTEGER(15) NOT NULL, 
        CONTACT_DETAILS VARCHAR(50)
    );
''')


def fill_details():
    top=Toplevel(bg='#F0DC82')
    top.geometry('700x400')
    top.title('Contact Manager')

    Label(top,text='Contact Manager',font=('Segoe UI Black',30),bg='#F0DC82').place(x=180,y=10)

    Button(top, text="Add Contact",font=('Malgun Gothic Bold',18),padx=52,pady=5,borderwidth=5,command=add_rec).place(x=20,y=100)

    Button(top, text="Delete Contact",font=('Malgun Gothic Bold',18),padx=40,pady=5,borderwidth=5,command=delete_rec).place(x=20,y=200)

    Button(top, text="Edit Contact",font=('Malgun Gothic Bold',18),padx=56,pady=5,borderwidth=5,command=edit_rec).place(x=400,y=100)

    Button(top, text="View all Contacts",font=('Malgun Gothic Bold',18),padx=28,pady=5,borderwidth=5,command=view_all).place(x=400,y=200)

    Button(top,text='Exit',font=('Malgun Gothic Bold',18),padx=296,pady=5,borderwidth=5,command=root.quit).place(x=20,y=300)


def  add_rec():
    top_add = Toplevel()
    top_add.title('Add a Contact')
    top_add.geometry('800x400')

    Label(top_add,text='Please fill the following Details',font=('Cambria Bold',25)).place(x=180,y=20)

    Label(top_add,text='First Name',font=('Cambria',18)).place(x=50,y=80)
    Label(top_add,text='Last Name',font=('Cambria',18)).place(x=50,y=120)
    Label(top_add,text='Phone Number',font=('Calibri',18)).place(x=50,y=160)
    Label(top_add,text='Details about the Contact',font=('Calibri',18)).place(x=50,y=200)

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
