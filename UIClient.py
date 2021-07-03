from traning_data import train_classifer
from connect_cam_mobile import *
from DocGia import DocGia
from tkinter import ttk,messagebox
from tkinter import *
from PIL import Image,ImageTk
from tk_tools import Calendar
import os
import glob
import time

class Start(Frame):
    #contructor Start App Client
    def __init__(self,master=None):
        if(master == None):
            return
        self.master = master
        self.doc_gia =DocGia()
        self.bg_dang_nhap =Image.open("img/BG.png").resize((500, 300), Image.ANTIALIAS)
        self.bg_dang_nhap = ImageTk.PhotoImage(self.bg_dang_nhap)
        self.trangThai = False
        self.display()

    #display Start app
    def display(self):
    
    # create nootbook
        Noot = ttk.Notebook(self.master)
        Noot.pack(expand=True)
    #


    #Frame Đăng nhập
        dang_nhap = Frame(Noot,height=300,width=500)
        dang_nhap.pack(fill='both', expand=True)
        self.value_dn = [StringVar(),StringVar()]
        Label(dang_nhap,image=self.bg_dang_nhap).place(x=0,y=0)
        Label(dang_nhap,text="Tên tài khoản").place(relx=0.17,rely=0.35)
        Label(dang_nhap,text="Mật khẩu").place(relx=0.215,rely=0.475)
        Entry(dang_nhap,textvariable= self.value_dn[0]).place(relx=0.35,rely=0.35)
        Entry(dang_nhap,show="*",textvariable=self.value_dn[1]).place(relx=0.35,rely=0.475)
        Button(dang_nhap,text="Đăng nhập",command=self.dang_nhap).place(relx=0.615,rely=0.6)
        Noot.add(dang_nhap,text="Đăng nhập")
    #Frame Đăng nhập bằng Face id
        dang_nhap_faceid =  Frame(Noot,height=300,width=500)
        dang_nhap_faceid.pack()
        self.face =Image.open("img\homepagepic.png")
        self.face1 = ImageTk.PhotoImage(self.face)
        self.face.close()
        self.tentk = StringVar()
        Noot.add(dang_nhap_faceid,text="Face id")
        self.lb_face = Label(dang_nhap_faceid,image=self.face1)
        self.lb_face.grid(sticky=W,column=0,row=0,rowspan=3)
        Label(dang_nhap_faceid,text="Tên tài khoản").grid(sticky=W,column=1,row=0)
        Entry(dang_nhap_faceid,textvariable=self.tentk).grid(sticky=W,column=2,row=0)
        Button(dang_nhap_faceid,text="Đăng nhập",command=self.dang_nhap_face).grid(column=1,row=0,rowspan=2,columnspan=2)
        Button(dang_nhap_faceid,text="Tắt",command=self.tatCam).grid(stick=E,column=2,row=0,rowspan=2,columnspan=2)

    #Frame Đăng ký
        dang_ky = Frame(Noot,height=300,width=500)
        dang_ky.pack(fill='both', expand=True)
        self.value = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        Label(dang_ky,text="Tên tài khoản").grid(column=0,row=0)
        Label(dang_ky,text="Mật khẩu").grid(column=0,row=1)
        Label(dang_ky,text="Tên").grid(column=0,row=2)
        Label(dang_ky,text="Ngày sinh").grid(column=0,row=3)
        Label(dang_ky,text="Địa chỉ").grid(column=0,row=4)
        Label(dang_ky,text= "         ").grid(column=2,row=0)
        Entry(dang_ky,textvariable=self.value[0]).grid(column=1,row=0)
        Entry(dang_ky,textvariable=self.value[1],show="*").grid(column=1,row=1)
        Entry(dang_ky,textvariable=self.value[2]).grid(column=1,row=2)
        Entry(dang_ky,textvariable=self.value[3]).grid(column=1,row=3)
        Entry(dang_ky,textvariable=self.value[4]).grid(column=1,row=4)
        Button(dang_ky,text="Đăng ký",command=self.dang_ky).grid(column=1,row=5,sticky=E)
        self.ngaySinh = Calendar(dang_ky,self.showNgay,year=2000,month=1,object=self)
        self.ngaySinh.grid(column=3,row=0,rowspan=5)
    #
    
        self.master.bind('<Return>',self.dang_nhap_event)

        Noot.add(dang_ky,text="Đăng ký")
        self.master.geometry("500x300")
        mainloop()


    def showNgay(self):
        ngaySinh = self.ngaySinh.getTime()
        nam=ngaySinh[0]
        thang =  ngaySinh[1]
        ngay = ngaySinh[2]
        if ngay <10 :
            ngay = "0"+str(ngay)
        if thang <10 :
            thang = "0"+str(thang)
        chuoi = str(nam)+"-"+str(thang)+"-"+str(ngay)
        self.value[3].set(chuoi)

    def huyChon(self):
        self.value[3].set("")

    def dang_ky(self):
        temp = self.doc_gia.DangKy(self.value)
        if temp == False :
            messagebox.showerror("THÔNG BÁO","NHẬP THIẾU THUỘC TÍNH")
        elif temp == True:
            messagebox.showinfo("THÔNG BÁO","THÊM ĐỘC GIẢ THÀNH CÔNG")
            for i in self.value:
                i.set("")
        else :
            messagebox.showerror("THÔNG BÁO",temp)

    def dang_nhap(self):
        tam = self.doc_gia.DangNhap(self.value_dn)
        if tam == True:
            self.trangThai = True
            self.master.destroy()
        else:
            messagebox.showinfo("THÔNG BÁO","ĐĂNG NHẬP KHÔNG THÀNH CÔNG")

    def dang_nhap_event(self,event):
        tam = self.doc_gia.DangNhap(self.value_dn)
        if tam == True:
            self.trangThai = True
            self.master.destroy()
        else:
            messagebox.showinfo("THÔNG BÁO","ĐĂNG NHẬP KHÔNG THÀNH CÔNG")

    def dang_nhap_face(self):   
        self.bat_cam =  True
        dem=0
        file = 'data/classifiers/{ten_tk}_classifier.xml'.format(ten_tk=self.tentk.get())
        if os.path.isfile(file):
            while self.bat_cam :
                a,b = xuat_cam(self.tentk.get())
                a = ImageTk.PhotoImage(a)
                self.lb_face.config(image=a)
                self.master.update()
                if b==1:
                    messagebox.showinfo("THÔNG BÁO","Đăng nhập thành công")
                    self.bat_cam = False
                    self.doc_gia.dangNhap_Face(self.tentk.get())
                    self.trangThai=TRUE
                    self.master.destroy()
                else:
                    if dem == 30:
                        messagebox.showerror("THÔNG BÁO","KHÔNG TÌM THẤY KHUÔN MẶT")
                        self.bat_cam = FALSE
                dem+=1

    def tatCam(self):
        self.lb_face['image']=self.face1
        self.bat_cam=False

    def __del__(self):
        if self.trangThai == True:
            ChucNangChinh(Tk(),self.doc_gia)

#When login success
class ChucNangChinh(Frame):
    def __init__(self,master,d_g):
        self.master = master
        self.d_g = d_g
        self.display()

    def display(self):
        noot = ttk.Notebook(self.master,height=600,width=800)
        noot.grid(column=0,row=0)
# data\classifiers\sang_classifier.xml
        self.file = 'data/classifiers/{ten_tk}_classifier.xml'.format(ten_tk=self.d_g.get_tk())
        print('self.file: ', self.file)

    #Thong tin doc gia
        self.frame1 = Frame (noot)
        self.frame1.pack()

        self.face = Image.open(r"img\homepagepic.png").resize((250, 100), Image.ANTIALIAS)
        self.face = ImageTk.PhotoImage(self.face)

        noot.add(self.frame1,text="THÔNG TIN")
        thong_tin = Frame(self.frame1,height=100,width=200)
        thong_tin.grid(column=0,row=0)
        Label(thong_tin,text="THÔNG TIN ĐỘC GIẢ").grid(column=1,row=0,columnspan=2)
        Label(thong_tin,text="tên tài khoản:").grid(column=1,row=1,sticky=W)
        Label(thong_tin,text="Tên độc giả:").grid(column=1,row=2,sticky=W)
        Label(thong_tin,text="ngày sinh:").grid(column=1,row=3,sticky=W)
        Label(thong_tin,text="Địa chỉ:").grid(column=1,row=4,sticky=W)
        Label(thong_tin,text="Số sách đã mượn").grid(column=1,row=5,sticky=W)
        Label(thong_tin,text="face id:").grid(column=1,row=6,sticky=W)
        #Get data doc gia
        Label(thong_tin,text=self.d_g.get_tk()).grid(column=2,row=1,sticky=W)
        Label(thong_tin,text=self.d_g.get_ten()).grid(column=2,row=2,sticky=W)
        Label(thong_tin,text=self.d_g.get_ngaySinh()).grid(column=2,row=3,sticky=W)
        Label(thong_tin,text=self.d_g.get_dia_chi()).grid(column=2,row=4,sticky=W)
        Label(thong_tin,text=self.d_g.get_so_sach()).grid(column=2,row=5,sticky=W)
        #Kiem tra file  = data\tentk\tentk.xml
        if os.path.isfile(self.file):
            Label(thong_tin,text="Có").grid(column=2,row=6,stick=W)
        else :
            self.btn_dk = Button(thong_tin,text="Đăng kí faceID",command = self.dang_ky_face)
            self.btn_dk.grid(column=2,sticky=W,row=6)
        self.master.geometry('800x600')
        mainloop()

    def dang_ky_face(self):
        self.btn_dk['state']=DISABLED
        so_anh = len(glob.glob('data/{ten_tk}/*.jpg'.format(ten_tk = self.d_g.get_tk())))
        self.dang_ky =Frame(self.frame1)
        self.dang_ky.grid(column=1,row=0)
        self.lb_face=Label(self.dang_ky,image=self.face)
        self.lb_face.grid(column=0,row=0,columnspan=2)
        # self.master.after(1000,self.doi_hinh,self.face)
        Label(self.dang_ky,text='Số ảnh được nhân diện').grid(column=0,row=1)
        self.so_anh_nd = Label(self.dang_ky,text=so_anh)
        self.so_anh_nd.grid(column=1,row=1)
        Button(self.dang_ky,text="Nhận diện khuôn mặt",command=self.nhan_dien).grid(column=2,row=0,sticky=N)
        Button(self.dang_ky,text="Tắt",command=self.tat).grid(column=3,row=0,sticky=N)
        Button(self.dang_ky,text="Trainning data",command=self.tran).grid(column=4,row=0,sticky=N)

    def nhan_dien(self):
        self.trangThai = True
        while self.trangThai == True:
            img,so_anh = nhan_dien_khuon_mat(self.d_g.get_tk(),int(self.so_anh_nd['text']))
            self.so_anh_nd['text']=so_anh
            img = ImageTk.PhotoImage(img)
            self.lb_face['image']=img
            self.master.update()

    def tat(self):
        self.lb_face.config(image=self.face)
        self.trangThai = False

    def doi_hinh(self,hinh):
        self.lb_face.config(image=hinh)
        self.master.update()

    def tran(self):
        if len(glob.glob('data/{ten_tk}/*.jpg'.format(ten_tk = self.d_g.get_tk()))) >= 300 and not os.path.isfile(self.file):
            train_classifer(self.d_g.get_tk())
            messagebox.showinfo("THÔNG BÁO","TRAINNING THÀNH CÔNG")
        else:
            messagebox.showerror("THÔNG BÁO","SỐ ẢNH KHÔNG ĐỦ")
Start(Tk())


    
