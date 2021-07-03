from db import *


class DocGia():
    def __init__(self) -> None:
        self.tenTK  =  None
        self.ten = None
        self.ngay_sinh = None
        self.dia_chi = None
        self.so_sach = None

    def DangNhap(self,value) -> bool:
        for i in value:
            if i.get() == "":
                return False
        trang_thai , gia_tri = select_doc_gia_pass(value[0].get())
        if gia_tri != None and trang_thai == True:
            matKhau = taoPass(value[1].get(),gia_tri[1])
            matKhau = md5_pass(matKhau)
            if matKhau ==  gia_tri[0]:
                self.tenTK = value[0].get()
                tam = select_doc_gia_3( value[0].get())
                self.ten = tam[0]
                self.ngay_sinh = tam[1]
                self.dia_chi = tam[2]
                self.so_sach = tam[3]
                return True
            else :
                return False
        else:
            return False

    def dangNhap_Face(self,tenTk):
        self.tenTK = tenTk
        tam = select_doc_gia_3( tenTk)
        self.ten = tam[0]
        self.ngay_sinh = tam[1]
        self.dia_chi = tam[2]
        self.so_sach = tam[3]

    def DangKy(self,value):
        for i in  value:
            if(i.get()==""):
                return False
        tam = insert_doc_gia(value[0].get(),value[1].get(),value[2].get(),value[3].get(),value[4].get())
        if tam == True:
            con.commit()
        else :
            con.rollback()
        return tam

    def get_tk(self):
        return self.tenTK
    
    def get_ten(self):
        return self.ten

    def get_ngaySinh(self):
        return self.ngay_sinh

    def get_dia_chi(self):
        return self.dia_chi

    def get_so_sach(self):
        return self.so_sach