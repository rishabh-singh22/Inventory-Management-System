# tkinter library used for build GUI application
from tkinter import*
from PIL import Image,ImageTk   #pip install pillow for images
from employee import employeeClass
from supplier import supllierClass

class Inventory:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Rishabh")
        self.root.config(bg="white")

        #----Title--------
        self.icon_title=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text="Inventory Management System ", image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)


        #====btn_logout ===========
        btn_logout = Button(self.root,text="Logout", font=("times new roman" , 15 , "bold") , bg="yellow", cursor="hand2").place(x=1150, y=15, height= 40 , width=150)

        #======clock=========
        self.lbl_clock = Label(self.root,text="Welome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        #======Left Menu Button==========
        self.Menulogo = Image.open("images/menu_im.png")
        self.Menulogo = self.Menulogo.resize((200,200),Image.LANCZOS)
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)

        LeftMenu = Frame(self.root,bd=2, relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,height=565,width=200)

        lbl_menuLogo = Label(LeftMenu,image=self.Menulogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu, text="Menu" , font=("times new roman", 20), bg="#009688").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu, text="Employee", image=self.icon_side, command=self.employee, compound=LEFT,padx=20,font=("times new roman", 20),anchor="w",bd=3,cursor="hand2", bg="white").pack(side=TOP,fill=X)
        btn_suppliers=Button(LeftMenu, text="Supplier", image=self.icon_side,command=self.supplier ,compound=LEFT,padx=20,font=("times new roman", 20),anchor="w",bd=3,cursor="hand2", bg="white").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu, text="Category", image=self.icon_side, compound=LEFT,padx=20,font=("times new roman", 20),anchor="w",bd=3,cursor="hand2", bg="white").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu, text="Product", image=self.icon_side, compound=LEFT,padx=20,font=("times new roman", 20),anchor="w",bd=3,cursor="hand2", bg="white").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu, text="Sales", image=self.icon_side, compound=LEFT,padx=20,font=("times new roman", 20),anchor="w",bd=3,cursor="hand2", bg="white").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT,padx=20,font=("times new roman", 20),anchor="w",bd=3,cursor="hand2" ,bg="white").pack(side=TOP,fill=X)

        #===== Content===

        self.lbl_employee = Label(self.root,text="Total Employee\n[ 0 ]", bg="#33bbf9", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root,text="Total Supplier\n[ 0 ]", bg="#ff5722", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category = Label(self.root,text="Total Category\n[ 0 ]", bg="#009688", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product\n[ 0 ]", bg="#607d8b", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales\n[ 0 ]", bg="#ffc107", bd=5,relief=RIDGE, fg="white", font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)



        #======footer=========
        lbl_footer = Label(self.root,text="Welome to Inventory Management System |  Developed by Rishabh\nFor any Technical Issue Contact: 999XXXX999", font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

    #==========================================================================================================
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supllierClass(self.new_win)  


if __name__=="__main__":
    root = Tk()
    obj = Inventory(root)
    root.mainloop()
