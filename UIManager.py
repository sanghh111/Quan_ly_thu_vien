from giaiThuat import quickSort_s, quickSort_tl, timKiem_Int, timKiem_String
from db import *
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
        kinh_lup = Image.open('img/kinh_lup.jpg').resize((15, 15), Image.ANTIALIAS)
        kinh_lup = ImageTk.PhotoImage(kinh_lup)

        self.nho_hon = Image.open('img/less.png').resize((15, 15), Image.ANTIALIAS)
        self.nho_hon = ImageTk.PhotoImage(self.nho_hon)

        self.lon_hon = Image.open('img/bigger.png').resize((15, 15), Image.ANTIALIAS)
        self.lon_hon = ImageTk.PhotoImage(self.lon_hon)

        self.bang = Image.open('img/equal.jpg').resize((15, 15), Image.ANTIALIAS)
        self.bang = ImageTk.PhotoImage(self.bang)

        Label(self.master,image=self.img).grid(column=0,row=0,stick=W)

        mygreen = "#d2ffd2"
        myred = "#dd0202"

        style = ttk.Style()

        
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        style.map('Treeview',
            background=[('selected','red')])

        # style.theme_use("yummy")
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

        self.tree = ttk.Treeview(frame_tree,yscrollcommand=scroll_bar,height=5)
        self.tree.pack()

        self.tree['column']=('Thể loại','Tên sách','Số lượng','Số sách còn lại','Giá sách')

        self.tree.column('#0',stretch=NO,width=0)
        self.tree.column('Thể loại',width=150,anchor=CENTER)
        self.tree.column('Tên sách',width=75)
        self.tree.column('Số lượng',width=75,anchor=CENTER)
        self.tree.column('Số sách còn lại',width=100)
        self.tree.column('Giá sách',width=75,anchor=CENTER)


        self.tree.heading('Thể loại',text='Thể loại',command=self.goi_ham_sap_xep(0))
        self.tree.heading('Tên sách',text='Tên sách',command=self.goi_ham_sap_xep(1))
        self.tree.heading('Số lượng',text='Số lượng',command=self.goi_ham_sap_xep(2))
        self.tree.heading('Số sách còn lại',text='Số sách còn lại',command=self.goi_ham_sap_xep(3))
        self.tree.heading('Giá sách',text="Giá sách",command=self.goi_ham_sap_xep(4))

        dem = 0
        self.tl_sach = select_the_loai()
        self.tl_view = self.tl_sach.copy()
        self.sach = []
        for i in self.tl_view:
            chuoi = (f'{i[1]}',f'',f'',f'',f'')
            self.tree.insert("","end",dem,values=(chuoi))
            sach = select_sach_TL(i[0])
            tam = dem + 1/10
            self.sach.append(sach)
            for j in sach:
                chuoi = (f'{i[1]}',f'{j[2]}',f'{j[3]}',f'{j[4]}',f'{j[5]}')
                self.tree.insert(dem,"end",tam,values=chuoi)
                tam += 0.1
            dem+=1
        self.sach_view = self.sach.copy()


        # self.the_loai_sach =  
    #The loai sach
        the_loai_sach = LabelFrame(quan_ly_sach,text="Thể loại sách",width=200,height=200)
        the_loai_sach.grid(column=0,row=2)

        Label(the_loai_sach,width=5).grid(column=0,row=0)
        
        self.value_tl = [StringVar(),StringVar()]
        Label(the_loai_sach,text="Mã thể loại sách").grid(column=1,row=0)
        Entry(the_loai_sach,textvariable=self.value_tl[0]).grid(column=2,row=0)
        Label(the_loai_sach,text="Tên thể loại sách").grid(column=1,row=1)
        Entry(the_loai_sach,textvariable=self.value_tl[1]).grid(column=2,row=1)

        Button(the_loai_sach,text="Thêm thể loại sách",command=self.them_the_loai).grid(column=3,row=2,sticky=E)
        
        Label(the_loai_sach,width=7).grid(column=3,row=0)

    #Sach
        sach = LabelFrame(quan_ly_sach,text='Sách')
        sach.grid(column=0,row=3)
        
        Label(sach,width=9).grid(column=0,row=1)

        self.value_sach = [StringVar(),StringVar(),IntVar(),IntVar(),IntVar()]
        Label(sach,text='Mã sách').grid(column=1,row=0,sticky=W)
        Entry(sach,textvariable=self.value_sach[0]).grid(column=2,row=0)
        Button(sach,image=kinh_lup,command=self.goi_ham_tim_kiem(0)).grid(column=3,row=0)
        
        Label(sach,text='Tên sách').grid(column=1,row=1,sticky=W)
        Entry(sach,textvariable=self.value_sach[1]).grid(column=2,row=1)
        Button(sach,image=kinh_lup,command=self.goi_ham_tim_kiem(2)).grid(column=3,row=1)

        self.btn_pss = []
        Label(sach,text='Số lượng').grid(column=1,row=2,sticky=W)
        Entry(sach,textvariable=self.value_sach[2]).grid(column=2,row=2)
        Button(sach,image=kinh_lup,command=self.goi_ham_tim_kiem(3)).grid(column=3,row=2)
        self.btn_pss.append(Button(sach,image=self.bang,command=self.call_xet_trang_thai(0)))#pss=phep so sanh
        self.btn_pss[0].grid(column=4,row=2,sticky=W)
        # 0 la bang 1 la lon hon va 2 la nhon hon
        self.trangThai_sach=[0,0,0]
        Label(sach,text='Số lượng còn lại').grid(column=1,row=3,sticky=W)
        Entry(sach,textvariable=self.value_sach[3]).grid(column=2,row=3)
        Button(sach,image=kinh_lup,command=self.goi_ham_tim_kiem(4)).grid(column=3,row=3)
        self.btn_pss.append(Button(sach,image=self.bang,command=self.call_xet_trang_thai(1)))#pss=phep so sanh
        self.btn_pss[1].grid(column=4,row=3,sticky=W)

        Label(sach,text='Giá').grid(column=1,row=4,sticky=W)
        Entry(sach,textvariable=self.value_sach[4]).grid(column=2,row=4)
        Button(sach,image=kinh_lup,command=self.goi_ham_tim_kiem(5)).grid(column=3,row=4)
        self.btn_pss.append(Button(sach,image=self.bang,command=self.call_xet_trang_thai(2)))#pss=phep so sanh
        self.btn_pss[2].grid(column=4,row=4,sticky=W)

        Button(sach,text='Thêm sách',command=self.them_sach).grid(column=0,row=5,sticky=W)
        Button(sach,text='Chỉnh sửa sách',command=self.chinh_sua_sach).grid(column=2,row=5,sticky=W)
        Button(sach,text='Xóa sách',command=self.xoa_sach).grid(column=3,row=5,columnspan=2,sticky=E)

        Label(sach,width=9).grid(column=4,row=1)    
        self.tree.bind("<<TreeviewSelect>>",self.chon_tree)

    #
        noot.add(quan_ly_sach,text="Quản lý sách")
        noot.bind('<Button-1>',self.chuyenTrang)

        self.master.geometry("600x410")
        mainloop()

    def call_xet_trang_thai(self,stt):
        def __callback() :
            return self.thay_doi_thuoc_tinh(stt)
        return __callback

    def thay_doi_thuoc_tinh(self,stt):
        if(self.trangThai_sach[stt]==0):
            self.btn_pss[stt].config(image = self.lon_hon)
            self.trangThai_sach[stt] = 1
            self.master.update()
        elif self.trangThai_sach[stt] == 1:
            self.btn_pss[stt].config(image = self.nho_hon)
            self.trangThai_sach[stt] = 2
            self.master.update()
        elif self.trangThai_sach[stt]  == 2:
            self.btn_pss[stt].config(image = self.bang)
            self.trangThai_sach[stt] = 0
            self.master.update()

    def them_the_loai(self):
        if(self.value_tl[0].get() == self.value_tl[1].get() == ""):
            messagebox.showerror("THÔNG BÁO","NHẬP THIẾU THUỘC TÍNH THỂ LOẠI")
        else:
            trangThai = insert_tl(self.value_tl[0].get(),self.value_tl[1].get())
            if trangThai == True:
                messagebox.showinfo("THÔNG BÁO","THÊM THÀNH CÔNG THỂ LOẠI")
                self.tl_sach.append((self.value_tl[0].get(),self.value_tl[1].get()))
                con.commit()
                self.load_lai()
                self.value_tl[0].set("")
                self.value_tl[1].set("")
                self.sach.append([])
            else: 
                messagebox.showerror("THÔNG BÁO",trangThai)
                con.rollback()

    def sayHello(self):
        print("HELLo")

    def load_lai(self):
        for the_loai in self.tree.get_children():
            # for sach in the_loai.get_children():
                # self.tree.delete(sach)
            self.tree.delete(the_loai)
        self.tl_view.clear()
        self.sach_view.clear()
        self.tl_view = self.tl_sach.copy()
        dem = 0
        for i in self.tl_view:
            chuoi = (f'{i[1]}',f'',f'',f'',f'')
            self.tree.insert("","end",dem,values=(chuoi))
            tam = dem + 1/10
            try:    
                sach = self.sach[dem]
            except:
                break
            self.sach_view.append(sach)
            for j in sach:
                chuoi = (f'{i[1]}',f'{j[2]}',f'{j[3]}',f'{j[4]}',f'{j[5]}')
                self.tree.insert(dem,"end",tam,values=chuoi)
                tam += 0.1
            dem+=1

    def chon_tree(self,e):
        chon = self.tree.selection()
        value = self.tree.item(chon)['values']
        tam = str(chon[0])
        if tam.find('.') == -1 :
            self.value_tl[1].set(value[0])
        else:
            tam = float(tam)
            int_tam = int(tam)
            print('str(int_tam-tam)[:1]: ', str(tam-int_tam))
            tam = str(tam-int_tam)[2:]
            tam = int(tam)
            
            print('tam: ', tam)
            self.value_tl[0].set(self.tl_view[int(int_tam)][0])
            self.value_tl[1].set(value[0])
            self.value_sach[0].set(self.sach_view[int_tam][tam][0])
            print('self.sach_view[int_tam][tam]: ', self.sach_view[int_tam][tam])
            self.value_sach[1].set(value[1])
            self.value_sach[2].set(value[2])
            self.value_sach[3].set(value[3])
            self.value_sach[4].set(value[4])

    def them_sach(self):
        so = self.tree.selection()
        value = self.tree.item(so)['values']
        print('value: ', value)
        if(value == ()):
            messagebox.showerror("THÔNG BÁO","CHƯA CHỌN THỂ LOẠI SÁCH")
            return
        if self.value_sach[0].get() =="" and self.value_sach[1].get() == "" and self.value_sach[2].get() == 0 and self.value_sach[4].get() == 0:
            messagebox.showerror("THÔNG BÁO","NHẬP THIẾU THUỘC TÍNH")
            return
        else:
            tam = int(so[0])
            trang_thai = insert_sach(self.value_sach[0].get(),
                                    self.tl_view [tam][0],
                                    self.value_sach[1].get(),
                                    self.value_sach[2].get(),
                                    self.value_sach[4].get())
            if trang_thai == True:
                tam = int(so[0])
                self.sach[tam].append((self.value_sach[0].get(),
                                self.tl_view [tam][0],
                                self.value_sach[1].get(),
                                self.value_sach[2].get(),
                                0,
                                self.value_sach[4].get()))
                messagebox.showinfo("THÔNG BÁO","THÊM SÁCH THÀNH CÔNG")
                con.commit()
                self.load_lai()
                self.value_sach[0].set("")
                self.value_sach[1].set("")
                self.value_sach[2].set(0)
                self.value_sach[3].set(0)
                self.value_sach[4].set(0)
            else :
                con.rollback()
                messagebox.showerror("THÔNG BÁO",trang_thai)

    def chinh_sua_sach(self):
        pass

    def xoa_sach(self):
        pass

    def goi_ham_tim_kiem(self,stt):
        def __callback():
            return self.tim_kiem(stt)
        return __callback

    def tim_kiem(self,stt):
        self.sach_view.clear()
        self.sach_view=[]
        self.tl_view.clear()
        self.tl_view=self.tl_sach.copy()
        i=0
        xoa=0
        if(stt==0  or stt ==2):
            if stt == 2:
                tam = 1
            elif stt==0:
                tam=0
            while( i < (len(self.tl_sach))):
                sach = []
                timKiem_String(self.sach[i].copy(),stt,self.value_sach[tam].get(),sach)
                if(sach != []): 
                    self.sach_view.append(sach)
                else:
                    self.tl_view.remove(self.tl_view[i-xoa])
                    xoa = xoa + 1
                i +=1
        else:
            while(i<len(self.tl_sach)):
                sach = []
                timKiem_Int(self.sach[i].copy(),stt,self.value_sach[stt-1].get(),self.trangThai_sach[stt-3],sach)
                if(sach != []):
                    self.sach_view.append(sach)
                else:
                    self.tl_view.remove(self.tl_view[i-xoa])
                    xoa=xoa+1
                i+=1
        self.load_view()

    def load_view(self):
        for the_loai in self.tree.get_children  ():
            self.tree.delete(the_loai)
        dem=0
        for i in self.tl_view:
            chuoi = (f'{i[1]}',f'',f'',f'',f'')
            tl = self.tree.insert("","end",dem,values=(chuoi))
            tam = dem +0.1
            for j in self.sach_view[dem]:
                chuoi = (f'{i[1]}',f'{j[2]}',f'{j[3]}',f'{j[4]}',f'{j[5]}')
                self.tree.insert(tl,'end',tam,values=chuoi)
                tam+=0.1
            dem+=1

    def goi_ham_sap_xep(self,stt):
        def __callback():
            return self.sap_xep(stt)
        return __callback

    def sap_xep(self,stt):
        if(stt == 0):
            self.tl_view.clear()
            self.sach_view.clear()
            self.tl_view = self.tl_sach.copy()
            self.sach_view =  self.sach.copy()
            quickSort_tl(self.tl_view,self.sach_view,0,len(self.tl_view)-1)
            print(self.tl_view)
            self.load_view()
        else:
            self.tl_view.clear()
            self.sach_view.clear()
            self.tl_view = self.tl_sach.copy()
            self.sach_view =  self.sach.copy()
            for i in range(len(self.tl_view)):
                quickSort_s(self.sach_view[i],stt,0,len(self.sach_view[i])-1)
            print(self.tl_view)
            self.load_view()


    def chuyenTrang(self,e):
        self.load_lai()
Start(Tk())