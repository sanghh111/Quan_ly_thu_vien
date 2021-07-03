from NhanVien import NhanVien
from tkinter import ttk,messagebox
from tkinter import *
from PIL import Image,ImageTk
from tk_tools import Calendar


class Start(Frame):
    #contructor Start App Client
    def __init__(self,master=None):
        if(master == None):
            return
        self.master = master
        self.nhanVien  =  NhanVien()
        self.bg_dang_nhap =Image.open("img/BG.png").resize((500, 300), Image.ANTIALIAS)
        self.bg_dang_nhap = ImageTk.PhotoImage(self.bg_dang_nhap)
        self.trangThai = False
        self.display()

    #display Start app
    def display(self):

    #Frame Đăng nhập
        dang_nhap = Frame(self.master,height=300,width=500)
        dang_nhap.pack(fill='both', expand=True)
        self.value_dn = [StringVar(),StringVar()]
        Label(dang_nhap,image=self.bg_dang_nhap).place(x=0,y=0)
        Label(dang_nhap,text="Tên tài khoản").place(relx=0.17,rely=0.35)
        Label(dang_nhap,text="Mật khẩu").place(relx=0.215,rely=0.475)
        Entry(dang_nhap,textvariable= self.value_dn[0]).place(relx=0.35,rely=0.35)
        Entry(dang_nhap,show="*",textvariable=self.value_dn[1]).place(relx=0.35,rely=0.475)
        Button(dang_nhap,text="Đăng nhập",command=self.dang_nhap).place(relx=0.615,rely=0.6)
    #
        self.master.geometry("500x300")
        mainloop()

    def dang_nhap(self):
        tam = self.nhanVien.dang_nhap(self.value_dn)
        if tam == True:
            self.trangThai = True
            self.master.destroy()
        else:
            messagebox.showinfo("THÔNG BÁO","ĐĂNG NHẬP KHÔNG THÀNH CÔNG")

    def __del__(self):
        if self.trangThai ==  True:
            Maneger(Tk(),self.nhanVien)
        

class Maneger(Frame):
    def __init__(self,master,nv):
        self.master =  master
        self.nv = nv
        self.img =Image.open("img/BG1.jpg").resize((600, 400), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.display()

    def display(self):

        Label(self.master,image=self.img).grid(column=0,row=0,stick=W)

        mygreen = "#d2ffd2"
        myred = "#dd0202"

        style = ttk.Style()


        style.theme_create( "yummy", parent="alt", settings={
                "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
                "TNotebook.Tab": {
                    "configure": {"padding": [5, 1], "background": mygreen },
                    "map":       {"background": [("selected", myred)],
                                "expand": [("selected", [1, 1, 1, 0])] } } } )

        style.theme_use("yummy")
        noot =  ttk.Notebook(self.master)
        noot.grid(column=0,row=0,sticky=N)

    #Chuc nang quan ly sach thu vien
        quan_ly_sach = Frame(noot)
        quan_ly_sach.pack()

        Label(quan_ly_sach,text="QUẢN LÝ SÁCH")

        frame_tree = Frame(quan_ly_sach)
        frame_tree.grid(column=0,row=1,columnspan=2)

        scroll_bar = Scrollbar(frame_tree)
        scroll_bar.pack(side=RIGHT,fill=Y)

        tree = ttk.Treeview(frame_tree,yscrollcommand=scroll_bar)
        tree.pack()

        tree['column']=('Thể loại','Tên sách','Số lượng')

        tree.column('#0',stretch=NO,width=0)
        tree.column('Thể loại',width=50)
        tree.column('Tên sách',width=100)
        tree.column('Số lượng',width=100,anchor=CENTER)

        tree.heading('Thể loại',text='Thể loại')
        tree.heading('Tên sách',text='Tên sách')
        tree.heading('Số lượng',text='Số lượng')


        # self.the_loai_sach =  

        Entry(quan_ly_sach).grid(column=0,row=2)
        
        Button(quan_ly_sach,text="Thêm thể loại sách",).grid(column=1,row=2)
        Button()

    #
        noot.add(quan_ly_sach,text="Quản lý sách")





        self.master.geometry("600x400")
        mainloop()


Start(Tk())