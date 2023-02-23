from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend import *

db = database("ppbank.db")

class data:
    def __init__(self, root):
        self.root = root
        self.root.title("bank management")
        self.root.geometry("1920x1080+0+0")
        self.root.state("zoomed")
        self.root.configure(bg="#C6FCFF")

        AC_NO=StringVar()
        NAME=StringVar()
        BRANCH=StringVar()
        TYPE=StringVar()
        AMOUNT=StringVar()

        frame1 = Frame(self.root,bg="#C6FCFF",width=1920,height=600)
        frame1.pack(side=TOP,fill=X)

        lab = Label(frame1, text="BANK MANAGEMENT SYSTEM",fg="#FF0000",bg="#C6FCFF")
        lab.config(font=("Koulen",35,"bold"))
        lab.grid(row=0,columnspan=4,padx=400,pady=20)

        ac = Label(frame1, text="Enter your account number", font=("Titillium Web",20),bg="#C6FCFF",fg="black",anchor=W,width=25)
        ac.grid(row=1,column=0,padx=(200,0), pady=(20,0))
        name = Label(frame1, text="Enter your name", font=("Titillium Web",20),bg="#C6FCFF",fg="black",anchor=W,width=25)
        name.grid(row=2, column=0,padx=(200,0), pady=(20,0))
        branch = Label(frame1, text="Enter your branch", font=("Titillium Web",20),bg="#C6FCFF",fg="black",anchor=W,width=25)
        branch.grid(row=3, column=0,padx=(200,0), pady=(20,0))
        type = Label(frame1, text="Enter your account type", font=("Titillium Web",20),bg="#C6FCFF",fg="black",anchor=W,width=25)
        type.grid(row=4, column=0,padx=(200,0), pady=(20,0))
        amount = Label(frame1, text="Enter your amount", font=("Titillium Web",20),bg="#C6FCFF",fg="black",anchor=W,width=25)
        amount.grid(row=5, column=0,padx=(200,0), pady=(20,0))

        e1 = Entry(frame1,textvariable=AC_NO,width=25, font=("Titillium Web",20),cursor="heart")
        e2 = Entry(frame1,textvariable=NAME,width=25, font=("Titillium Web",20), cursor="heart")
        e3 = Entry(frame1,textvariable=BRANCH,width=25, font=("Titillium Web",20), cursor="heart")
        e5 = Entry(frame1, textvariable=AMOUNT,width=25, font=("Titillium Web",20), cursor="heart")
        e4 = ttk.Combobox(frame1, state="readonly", font=("Titillium Web",20), cursor="heart",textvariable=TYPE,width=24)
        e4['values'] = ("savings", "current")


        e1.grid(row=1, column=1,padx=(30,30), pady=(20,0))
        e2.grid(row=2, column=1,padx=(30,30), pady=(20,0))
        e3.grid(row=3, column=1,padx=(30,30), pady=(20,0))
        e4.grid(row=4, column=1,padx=(30,30), pady=(20,0))
        e5.grid(row=5, column=1,padx=(30,30), pady=(20,0))

        frame2 = Frame(self.root,bg="#C6FCFF",width=1920,height=80)
        frame2.pack(fill=X)

        def fetchdata():

            table.delete(*table.get_children())
            for row in db.fetch():
                table.insert("", END, values=row)

        def cleardata():

            AC_NO .set("")
            NAME .set("")
            BRANCH.set("")
            TYPE.set("")
            AMOUNT.set("")

        def insertdata():
            if e2.get() == " " or e3.get() == "" or e4.get() == "" or e5.get() == "":
                messagebox.showinfo("Message", "fill the information")
            else:
                db.insert(e2.get(), e3.get(), e4.get(), e5.get())
                fetchdata()
                cleardata()
                messagebox.showinfo("Message", "data inserted successfully")


        def getrecord(event):
            showrows = table.focus()
            datas = table.item(showrows)
            global row
            row=datas['values']
            AC_NO.set(row[0])
            NAME.set(row[1])
            BRANCH.set(row[2])
            TYPE.set(row[3])
            AMOUNT.set(row[4])

        def updatedata():
            if e2.get() == " " or e3.get() == "" or e4.get() == "" or e5.get() == "":
                messagebox.showinfo("Message", "fill the information")
            else:
                db.update(e2.get(), e3.get(), e4.get(), e5.get(),row[0])
                fetchdata()
                cleardata()
                messagebox.showinfo("Message", "record updated successfully")

        def deletedata():
            db.delete(row[0])
            fetchdata()
            cleardata()
            messagebox.showinfo("Message", "record deleted successfully")
        def exitdata():
            exitdata= messagebox.askyesno("conformation meassage","sure do you want to exit")
            if exitdata > 0:
                root.destroy()
                return

        enter = Button(frame2, text="enter", font=("Titillium Web",20), fg="white", bg="#250074", cursor="dot",command=insertdata, width=10)
        enter.grid(row=0, column=0,padx=(110,0),pady=(20,30))
        update = Button(frame2, text="update", font=("Titillium Web",20), fg="white", bg="#250074", cursor="dot", command=updatedata, width=10)
        update.grid(row=0, column=1,padx=(110,0),pady=(20,30))
        clear = Button(frame2, text="clear", font=("Titillium Web",20), fg="white", bg="#250074", cursor="dot", command=cleardata, width=10)
        clear.grid(row=0, column=2,padx=(110,0),pady=(20,30))
        delete = Button(frame2, text="delete", font=("Titillium Web",20), fg="white", bg="#250074", cursor="dot", command=deletedata, width=10)
        delete.grid(row=0, column=3,padx=(110,0),pady=(20,30))
        exit = Button(frame2, text="exit", font=("Titillium Web",20), fg="white", bg="#250074", cursor="dot", command=exitdata, width=10)
        exit.grid(row=0, column=4, padx=(110,0),pady=(20,30))

        frame3 = Frame(self.root,bg="yellow",width=1920,height=400)
        frame3.pack(side=BOTTOM,fill=X)

        style = ttk.Style()
        style.configure("Records.Treeview", font=("calibiri",15), rowheight=50)
        style.configure("Records.Treeview.Heading", font=("calibiri",25))

        table = ttk.Treeview(frame3,columns=(0,1,2,3,4,5),style="Records.Treeview")
        table.heading("0", text="ac")
        table.column("0",anchor=CENTER,stretch=NO,width=300)
        table.heading("1", text="name")
        table.column("1",anchor=CENTER,stretch=NO,width=300)
        table.heading("2", text="branch")
        table.column("2",anchor=CENTER,stretch=NO,width=300)
        table.heading("3", text="ac_type")
        table.column("3",anchor=CENTER,stretch=NO,width=300)
        table.heading("4", text="balance")
        table.column("4",anchor=CENTER,stretch=NO,width=300)
        table["show"] = 'headings'
        table.bind("<ButtonRelease-1>",getrecord)
        table.pack(fill=X)

        fetchdata()

if __name__ == '__main__':
    root = Tk()
    a = data(root)
    root.mainloop()
