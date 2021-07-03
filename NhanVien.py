from db import *

class NhanVien():
    def __init__(self) -> None:
        self.ten_Tk = None
        self.ten_Nv = None
        self.ngay_sinh = None
        self.cmnd = None
        self.dia_chi = None

    def dang_nhap(self,value) -> bool:
        for i in value:
            if i.get() == "":
                return False
        trang_thai , gia_tri = select_nhan_vien_pass(value[0].get())
        if gia_tri != None and trang_thai == True:
            matKhau = taoPass(value[1].get(),gia_tri[1])
            matKhau = md5_pass(matKhau)
            if matKhau ==  gia_tri[0]:
                self.tenTk = value[0].get()
                tam = select_nhan_vien_4( value[0].get())
                print('tam: ', tam)
                self.ten = tam[0]
                self.ngay_sinh = tam[1]
                self.dia_chi = tam[2]
                self.cmnd = tam[3]
                return True
            else :
                return False
        else:
            return False