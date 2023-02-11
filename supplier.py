from tkinter import*
from PIL import Image,ImageTk   #pip install pillow for images
from tkinter import ttk,messagebox


class supllierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Rishabh")
        self.root.config(bg="white")
        self.root.focus_force()

    #=======title=============

        title = Label(self.root,text="Manage Supplier Details", font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=20,width=1000)

        lbl_invoiceNo = Label(self.root,text="Invoice No.", font=("goudy old style",15),bg="white").place(x=50,y=70)
        lbl_supplierName = Label(self.root,text="Supplier Name", font=("goudy old style",15),bg="white").place(x=50,y=100)
        lbl_contact = Label(self.root,text="Contact ", font=("goudy old style",15),bg="white").place(x=50,y=130)
        lbl_Description = Label(self.root,text="Description ", font=("goudy old style",15),bg="white").place(x=50,y=160)


if __name__=="__main__":
    root = Tk()
    obj = supllierClass(root)
    root.mainloop()
