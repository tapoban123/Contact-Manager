from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


root = Tk()
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
    top=Toplevel(root,bg='#F0DC82')
    top.geometry('700x400')
    top.title('Contact Manager')

    Label(top,text='Contact Manager',font=('Segoe UI Black',30),bg='#F0DC82').place(x=180,y=10)

    Button(top, text="Add Contact",font=('Malgun Gothic Bold',18),padx=52,pady=5,borderwidth=5,command=add_rec).place(x=20,y=100)

    Button(top, text="Delete Contact",font=('Malgun Gothic Bold',18),padx=40,pady=5,borderwidth=5,command=delete_rec).place(x=20,y=200)

    Button(top, text="Edit Contact",font=('Malgun Gothic Bold',18),padx=56,pady=5,borderwidth=5,command=edit_rec).place(x=400,y=100)

    Button(top, text="View all Contacts",font=('Malgun Gothic Bold',18),padx=28,pady=5,borderwidth=5,command=view_all).place(x=400,y=200)

    Button(top,text='Exit',font=('Malgun Gothic Bold',18),padx=296,pady=5,borderwidth=5,command=root.quit).place(x=20,y=300)


def add_recs_to_db():
    if len(entry_fname.get()) == len(entry_lname.get()) == len(entry_phno.get()) == len(entry_address.get()) == 0:
        messagebox.showerror('Unfilled Contact Details',"You need to fill up the details first and then press 'Enter' or 'OK'",parent=top_add)
        entry_fname.focus()
    else:
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
    global top_add
    global entry_fname
    global entry_lname
    global entry_phno
    global entry_address

    top_add = Toplevel(root,bg='#99BADD')
    top_add.title('Add a Contact')
    top_add.geometry('785x435')

    Label(top_add,text='Please fill the following Details',font=('Cambria Bold',25),bg='#99BADD').place(x=180,y=20)

    Label(top_add,text='First Name:',font=('Cambria',18),bg='#99BADD').place(x=50,y=100)
    Label(top_add,text='Last Name:',font=('Cambria',18),bg='#99BADD').place(x=50,y=140)
    Label(top_add,text='Phone Number:',font=('Calibri',18),bg='#99BADD').place(x=50,y=180)
    Label(top_add,text='Address:',font=('Calibri',18),bg='#99BADD').place(x=50,y=220)

    entry_fname = Entry(top_add,width=30,borderwidth=8,font=('Arial',15),bg='#DCDCDC')
    entry_lname = Entry(top_add,width=30,borderwidth=8,font=('Arial',15),bg='#DCDCDC')
    entry_phno = Entry(top_add,width=30,borderwidth=8,font=('Arial',15),bg='#DCDCDC')
    entry_address = Entry(top_add,width=30,borderwidth=8,font=('Arial',15),bg='#DCDCDC')

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
    top_delete = Toplevel(root)
    top_delete.title('Delete a Contact')
    top_delete.geometry('500x400')

    Label(top_delete,text='Coming Soon...',font=('Arial',25)).pack(padx=30,pady=160)


def edit_rec():
    top_edit = Toplevel(root)
    top_edit.title('Edit a Contact')
    top_edit.geometry('500x400')

    Label(top_edit,text='Coming Soon...',font=('Arial',25)).pack(padx=30,pady=160)


def search_contact():
    if len(search_fname.get()) > 0 and (len(search_lname.get()) == len(search_phno.get()) == 0):
        cursor.execute(F"SELECT * FROM CONTACT_RECS WHERE CONACT_FIRST_NAME LIKE '{search_fname.get().title()}%';")
        fname_data = cursor.fetchall()

        for rec in contacts_tree.get_children():
            contacts_tree.delete(rec)

        fname_iid = 1
        for data in fname_data:
            if fname_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=fname_iid,values=data,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=fname_iid,values=data,tags='oddrow')
            fname_iid += 1
    
    if len(search_lname.get()) > 0 and (len(search_fname.get()) == len(search_phno.get()) == 0):
        cursor.execute(F"SELECT * FROM CONTACT_RECS WHERE CONTACT_LAST_NAME LIKE '{search_lname.get().title()}%';")
        lname_data = cursor.fetchall()

        for rec2 in contacts_tree.get_children():
            contacts_tree.delete(rec2)

        lname_iid = 1
        for data2 in lname_data:
            if lname_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=lname_iid,values=data2,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=lname_iid,values=data2,tags='oddrow')
            lname_iid += 1

    elif len(search_phno.get()) > 0 and (len(search_fname.get()) == len(search_lname.get()) == 0):
        cursor.execute(F"SELECT * FROM CONTACT_RECS WHERE CONTACT_PH_NO LIKE '{int(search_phno.get())}%';")
        phno_data = cursor.fetchall()

        for rec_phno in contacts_tree.get_children():
            contacts_tree.delete(rec_phno)
        
        phno_iid = 1
        for data3 in phno_data:
            if phno_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=phno_iid,values=data3,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=phno_iid,values=data3,tags='oddrow')
            phno_iid += 1
    
    elif (len(search_fname.get()) == len(search_lname.get()) == len(search_phno.get()) == 0):
        cursor.execute('SELECT * FROM CONTACT_RECS;')
        ALL_DATA = cursor.fetchall()

        for s_recs in contacts_tree.get_children():
            contacts_tree.delete(s_recs)

        all_iid = 1
        for all_recs in ALL_DATA:
            if all_iid  % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=all_iid,values=all_recs,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=all_iid,values=all_recs,tags='oddrow')
            all_iid += 1

    elif (len(search_fname.get()) > 0 and len(search_lname.get())) > 0 and len(search_phno.get()) == 0:
        cursor.execute(F"SELECT * FROM CONTACT_RECS WHERE CONACT_FIRST_NAME LIKE '{search_fname.get()}%' and CONTACT_LAST_NAME LIKE '{search_lname.get()}%';")
        fname_lname = cursor.fetchall()

        for recfl in contacts_tree.get_children():
            contacts_tree.delete(recfl)

        fl_iid = 1
        for data4 in fname_lname:
            if fl_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=fl_iid,values=data4,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=fl_iid,values=data4,tags='oddrow')
            fl_iid += 1

    elif len(search_fname.get()) == 0 and (len(search_lname.get()) > 0 and len(search_phno.get()) > 0):
        cursor.execute(f"SELECT * FROM CONTACT_RECS WHERE CONTACT_LAST_NAME LIKE '{search_lname.get()}%' and CONTACT_PH_NO LIKE '{search_phno.get()}%';")
        phno_lname = cursor.fetchall()

        for recphl in contacts_tree.get_children():
            contacts_tree.delete(recphl)
        
        phl_iid = 1
        for data5 in phno_lname:
            if phl_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=phl_iid,values=data5,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=phl_iid,values=data5,tags='oddrow')
            phl_iid += 1
        
    elif len(search_fname.get()) > 0 and len(search_lname.get()) == 0 and len(search_phno.get()) > 0:
        cursor.execute(f"SELECT * FROM CONTACT_RECS WHERE CONACT_FIRST_NAME LIKE '{search_fname.get()}%' and CONTACT_PH_NO LIKE '{search_phno.get()}%';")
        fphno = cursor.fetchall()

        for fph in contacts_tree.get_children():
            contacts_tree.delete(fph)
        
        fph_iid = 1
        for data6 in fphno:
            if fph_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=fph_iid,values=data6,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=fph_iid,values=data6,tags='oddrow')
            fph_iid += 1

    elif len(search_fname.get()) > 0 and len(search_lname.get()) > 0 and len(search_phno.get()) > 0:
        cursor.execute(f"SELECT * FROM CONTACT_RECS WHERE CONACT_FIRST_NAME LIKE '{search_fname.get()}%' AND CONTACT_LAST_NAME LIKE '{search_lname.get()}%' AND CONTACT_PH_NO LIKE '{search_phno.get()}%';")
        fname_lname_phno = cursor.fetchall()

        for flphno in contacts_tree.get_children():
            contacts_tree.delete(flphno)
        
        fname_lname_phno_iid = 1
        for data7 in fname_lname_phno:
            if fname_lname_phno_iid % 2 == 0:
                contacts_tree.insert(parent='',index='end',iid=fname_lname_phno_iid,values=data7,tags='evenrow')
            else:
                contacts_tree.insert(parent='',index='end',iid=fname_lname_phno_iid,values=data7,tags='oddrow')
            fname_lname_phno_iid += 1


def view_all():
    global search_fname
    global search_lname
    global search_phno
    global contacts_tree

    top_view_all = Toplevel(root,bg='#99BADD')
    top_view_all.title('All Contacts')
    top_view_all.geometry('780x670')

    frame1 = Frame(top_view_all,width=600)
    frame1.pack(side=TOP,anchor='n')

    frame2 = Frame(top_view_all,height=400,width=800,bg='#99BADD')
    frame2.pack(side=LEFT,anchor='e')

    Label(frame2,text='Search Record',font=('Calibri',20,'bold'),bg='#99BADD').place(x=320,y=5)
    Label(frame2,text='First Name:',font=('Calibri',16,'bold'),bg='#99BADD').place(x=60,y=70)
    Label(frame2,text='Last Name:',font=('Calibri',16,'bold'),bg='#99BADD').place(x=60,y=110)
    Label(frame2,text='Phone Number:',font=('Calibri',16,'bold'),bg='#99BADD').place(x=60,y=150)

    search_fname = Entry(frame2,width=30,borderwidth=8,font=('Arial 14'),bg='#DCDCDC')
    search_lname = Entry(frame2,width=30,borderwidth=8,font=('Arial 14'),bg='#DCDCDC')
    search_phno = Entry(frame2,width=30,borderwidth=8,font=('Arial 14'),bg='#DCDCDC')

    search_fname.place(x=340,y=70)
    search_lname.place(x=340,y=110)
    search_phno.place(x=340,y=150)

    search_fname.focus()
    search_fname.bind('<Return>',lambda x: search_lname.focus())
    search_lname.bind('<Return>',lambda x: search_phno.focus())
    search_phno.bind('<Return>',lambda x: search_contact())

    Button(frame2,text='Search',font=('Malgun Gothic Bold',18),padx=120,pady=10,borderwidth=4,command=search_contact).place(x=30,y=230)
    Button(frame2,text='Close',font=('Malgun Gothic Bold',18),padx=130,pady=10,borderwidth=4,command=top_view_all.destroy).place(x=400,y=230)

    scroll_y = Scrollbar(frame1,orient=VERTICAL)
    scroll_y.pack(side=RIGHT,fill=Y,expand=True)

    scroll_x = Scrollbar(frame1,orient=HORIZONTAL)
    scroll_x.pack(side=BOTTOM,fill=X)

    style = ttk.Style()
    style.configure('Treeview',
    font=('Cambria',14),
    rowheight=40)
    style.configure('Treeview.Heading',font=('Constantia',18,'bold'))

    contacts_tree = ttk.Treeview(frame1,height=7,selectmode='none',yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

    contacts_tree.tag_configure('oddrow',background='#F8F8FF')
    contacts_tree.tag_configure('evenrow',background='#9BDDFF')

    scroll_x.config(command=contacts_tree.xview)
    scroll_y.config(command=contacts_tree.yview)

    contacts_tree['columns'] = ('Contact ID','First Name','Last Name','Phone Number','Address')

    contacts_tree.heading('#0',text='')
    contacts_tree.heading('#1',text='Contact ID',anchor='c')
    contacts_tree.heading('#2',text='First Name',anchor='c')
    contacts_tree.heading('#3',text='Last Name',anchor='c')
    contacts_tree.heading('#4',text='Phone Number',anchor='c')
    contacts_tree.heading('#5',text='Address',anchor='c')

    contacts_tree.column('#0',width=0,minwidth=0,stretch=NO)
    contacts_tree.column('#1',width=150,minwidth=0,stretch=NO,anchor='c')
    contacts_tree.column('#2',width=200,minwidth=0,stretch=NO,anchor='c')
    contacts_tree.column('#3',width=240,minwidth=0,stretch=NO,anchor='c')
    contacts_tree.column('#4',width=260,minwidth=0,stretch=NO,anchor='c')
    contacts_tree.column('#5',width=400,minwidth=0,stretch=NO,anchor='c')

    cursor.execute('SELECT * FROM CONTACT_RECS;')
    CONTACTS = cursor.fetchall()

    tree_iid = 1 
    for contact in CONTACTS:
        if tree_iid % 2 == 0:
            contacts_tree.insert(parent='',index='end',iid=tree_iid,values=contact,tags='evenrow')
        else:
            contacts_tree.insert(parent='',index='end',iid=tree_iid,values=contact,tags='oddrow')
        tree_iid += 1

    contacts_tree.pack()


text1 = "Contact Manager \n\n\n\n\n\n\nClick Anywhere to Continue"

myButton_begin = Button(root,text=text1,font=('Calibri',35),bg='#BF94E4',padx=600,pady=600,command=fill_details)
myButton_begin.pack()

root.mainloop()
