from tkinter import*
from PIL import Image,ImageTk   #pip install pillow for images
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Rishabh")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variable
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


        # ============Title===========

        lbl_title = Label(self.root,text="Manage Product Category", font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=2)

        lbl_name = Label(self.root,text="Enter Category Name", font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name = Entry(self.root,text="Enter Category Name", textvariable=self.var_name,font=("goudy old style",25),bg="lightyellow").place(x=50,y=170,width=300)
        




if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
