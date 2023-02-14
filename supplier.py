from tkinter import*
from PIL import Image,ImageTk   #pip install pillow for images
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Rishabh")
        self.root.config(bg="white")
        self.root.focus_force()

        #===================================================================

        #====All Variables============

        self.var_searchby = StringVar()
        self.var_searchText = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name= StringVar()
        self.var_contact = StringVar()
        
        # self.var_address = StringVar()

        

        #===========options=========
        

        lbl_search = Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=700,y=80)

        txt_search = Entry(self.root,textvariable=self.var_searchText, font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=140)
        btn_seach = Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

        #=======title=============

        title = Label(self.root,text="Supplier Details", font=("goudy old style",15,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)


        #===============Content===============

        # row 1
        lbl_supplier_invoice = Label(self.root,text="Invoice No.", font=("goudy old style",15),bg="white").place(x=50,y=80)
        txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice, font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
        
        # row2
        lbl_name = Label(self.root,text="Name", font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)
        
        # row3
        lbl_contact = Label(self.root,text="Contact", font=("goudy old style",15),bg="white").place(x=50,y=160)     
        txt_contact = Entry(self.root,textvariable=self.var_contact, font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)

        #=====row4=====
        lbl_description = Label(self.root,text="Description", font=("goudy old style",15),bg="white").place(x=50,y=200)
  
        self.txt_description = Text(self.root, font=("goudy old style",15),bg="lightyellow")
        self.txt_description.place(x=180,y=200,width=470,height=120)
       
        # Buttons
        btn_save = Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35) 
        btn_update = Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete = Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)



        # ====== Supplier Details with the help of TreeView===========

        supplier_frame = Frame(self.root,bd=3,relief=RIDGE)
        supplier_frame.place(x=700,y=120,width=380,height=350)

        Scrolly=Scrollbar(supplier_frame,orient=VERTICAL)
        Scrollx=Scrollbar(supplier_frame,orient=HORIZONTAL)

           # Tree View

        self.SupplierTable = ttk.Treeview(supplier_frame,columns=("invoice","name","contact","description"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.SupplierTable.xview)
        Scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("invoice",text="Invoice No.")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("description",text="Description")

        self.SupplierTable["show"] = "headings"   # To disappear space before headings
        self.SupplierTable.pack(fill=BOTH,expand=1)


        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)

        self.SupplierTable.column("contact",width=130)
        self.SupplierTable.column("description",width=180)

        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

# ======================================================================================================================

    def add(self):
        con = sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice Must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no. is already assigned,Try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,description) values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(), 
                                        self.var_contact.get(), 
                                        self.txt_description.get('1.0',END),
                                    
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)        
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def show(self):
        con = sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()

        try: 
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   



    def update(self):
        con = sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice Must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier Invoice",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,description=?, where invoice=?",(
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_description.get('1.0',END),
                                        self.var_sup_invoice.get(),
                                        
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)        
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier Invoice Must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier Invoice",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfuly",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_name.set(""),
        self.var_contact.set(""),                                       
        self.txt_description.delete('1.0',END),
        self.var_sup_invoice.set(""), 
        self.var_searchText.set(""),
        self.show()



    def search(self):
        con = sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()

        try: 
            if self.var_searchText.get()=="":
                messagebox.showerror("Error","Invoice No. Should Be Required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_searchText.get(),))
                rows=cur.fetchone()
                if rows != None:
                   self.SupplierTable.delete(*self.SupplierTable.get_children())
                   self.SupplierTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   





    def get_data(self,ev):
        f = self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_description.delete('1.0',END),
        self.txt_description.insert(END, row[3])
       

if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
