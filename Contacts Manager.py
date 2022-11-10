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
        CONTACT_LAST_NAME VARCHAR(40) NOT NULL, 
        CONTACT_PH_NO INTEGER(15) NOT NULL,
        CONTACT_ADDRESS TEXT
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


def add_recs_to_db():
    cursor.execute('SELECT * FROM CONTACT_RECS;')
    NO_OF_RECS = cursor.fetchall()

    cursor.execute(f"INSERT INTO CONTACT_RECS VALUES({len(NO_OF_RECS)+1},'{entry_fname.get().strip()}','{entry_lname.get().strip()}',{entry_phno.get().strip()},'{entry_address.get().strip()}');")
    conn.commit()

    entry_fname.delete(0,END)
    entry_lname.delete(0,END)
    entry_phno.delete(0,END)
    entry_address.delete(0,END)

    entry_fname.focus()


def  add_rec():
    top_add = Toplevel()
    top_add.title('Add a Contact')
    top_add.geometry('785x435')

    global entry_fname
    global entry_lname
    global entry_phno
    global entry_address

    Label(top_add,text='Please fill the following Details',font=('Cambria Bold',25)).place(x=180,y=20)

    Label(top_add,text='First Name:',font=('Cambria',18)).place(x=50,y=100)
    Label(top_add,text='Last Name:',font=('Cambria',18)).place(x=50,y=140)
    Label(top_add,text='Phone Number:',font=('Calibri',18)).place(x=50,y=180)
    Label(top_add,text='Address:',font=('Calibri',18)).place(x=50,y=220)

    entry_fname = Entry(top_add,width=30,borderwidth=8,font=('Arial',15))
    entry_lname = Entry(top_add,width=30,borderwidth=8,font=('Arial',15))
    entry_phno = Entry(top_add,width=30,borderwidth=8,font=('Arial',15))
    entry_address = Entry(top_add,width=30,borderwidth=8,font=('Arial',15))

    entry_fname.place(x=390,y=100)
    entry_lname.place(x=390,y=140)
    entry_phno.place(x=390,y=180)
    entry_address.place(x=390,y=220)

    entry_fname.focus()
    entry_fname.bind('<Return>',lambda x: entry_lname.focus())
    entry_lname.bind('<Return>',lambda x: entry_phno.focus())
    entry_phno.bind('<Return>',lambda x: entry_address.focus())
    entry_address.bind('<Return>',lambda x: add_recs_to_db())

    Button(top_add,text='Close',font=('Malgun Gothic Bold',18),padx=120,pady=10,borderwidth=5,command=top_add.destroy).place(x=50,y=300)
    Button(top_add,text='OK',font=('Malgun Gothic Bold',18),padx=143,pady=10,borderwidth=5,command=add_recs_to_db).place(x=390,y=300)


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
