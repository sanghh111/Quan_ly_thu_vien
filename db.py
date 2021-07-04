import sqlite3
from sqlite3.dbapi2 import Cursor
import hashlib
import string
import random
from tkinter import BooleanVar
from tkinter.constants import N
from typing import List
from datetime import date, datetime

def connect_db(dbfile):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    return con, cur

con,cur = connect_db("ThuVien.db") 

def sinh_chuoi(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#decrypt
def taoPass(_pass,chuoi):
    dem = int(len(_pass)/2)
    for i in range(0,len(_pass),dem):
        try:
            _pass= _pass[:i] + chuoi[0] + _pass[i:]
            chuoi=chuoi[1:]
        except:
            return _pass
    if len(chuoi) !=0:
        _pass = _pass+chuoi
    return _pass

def md5_pass(_pass):
    _pass = hashlib.md5(_pass.encode())
    return _pass.hexdigest()

def insert_doc_gia(tk,mk,ten,ngay_sinh,dia_chi):
    tam = sinh_chuoi()
    mk = taoPass(mk,tam)
    mk = md5_pass(mk)
    cau_truy_van='''INSERT into "Doc gia" (ten_tk,mat_khau,ten,ngay_sinh,dia_chi,tam)
    VALUES("{_tk}","{_mk}","{_ten}","{_ngay_sinh}","{_dia_chi}","{_tam}")'''.format(_tk=tk,_mk=mk,_ten=ten,_ngay_sinh=ngay_sinh,_dia_chi=dia_chi,_tam=tam)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as E:
        return E

def select_doc_gia_pass(tk):
    cau_truy_van='''Select "mat_khau","tam"
    From "Doc gia"
    Where ten_tk = "{_tk}"'''.format(_tk=tk)
    try:
        result = cur.execute(cau_truy_van).fetchone()
        return True,result
    except Exception as E:
        return False, E

def select_doc_gia_3(tk):
    cau_truy_van='''Select ten,ngay_sinh,dia_chi,so_sach
    From "Doc gia"
    Where ten_tk = "{_tk}"'''.format(_tk=tk)
    try:
        result = cur.execute(cau_truy_van).fetchone()
        return result
    except Exception as E:
        return E

def insert_nhan_vien(tk,mk,ten,ngay_sinh,dia_chi,cmnd):
    tam = sinh_chuoi()
    mk = taoPass(mk,tam)
    mk = md5_pass(mk)
    cau_truy_van='''INSERT into "Nhan Vien" (ten_tk,mat_khau,ten,ngay_sinh,dia_chi,cmnd,tam)
    VALUES("{_tk}","{_mk}","{_ten}","{_ngay_sinh}","{_dia_chi}","{_cmnd}","{_tam}")'''.format(_tk=tk,_mk=mk,_ten=ten,_ngay_sinh=ngay_sinh,_dia_chi=dia_chi,_tam=tam,_cmnd=cmnd)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as E:
        return E

def select_nhan_vien_pass(tk):
    cau_truy_van='''Select "mat_khau","tam"
    From "Nhan Vien"
    Where ten_tk = "{_tk}"'''.format(_tk=tk)
    try:
        result = cur.execute(cau_truy_van).fetchone()
        return True,result
    except Exception as E:
        return False, E

def select_nhan_vien_4(tk):
    cau_truy_van='''Select ten,ngay_sinh,dia_chi,cmnd
    From "Nhan Vien"
    Where ten_tk = "{_tk}"'''.format(_tk=tk)
    try:
        result = cur.execute(cau_truy_van).fetchone()
        return result
    except Exception as E:
        return E

def select_the_loai():
    cau_truy_van = '''Select *
    From "The loai"'''
    try:
        result = cur.execute(cau_truy_van).fetchall()
        return result
    except Exception as E:
        return False

def select_sach(the_loai):
    cau_truy_van = '''Select *
    From "Sach"
    Where ma_the_loai = "_tl"'''.format(the_loai)
    try:
        result = cur.execute(cau_truy_van).fetchall()
        return result
    except Exception as E:
        return E

def select_the_loai() ->list:
    cau_truy_van = '''Select *
    From "The loai sach"
    '''
    return cur.execute(cau_truy_van).fetchall() 

def select_sach_TL(TL) ->list:
    cau_truy_van = '''Select *
    From "Sach"
    where ma_the_loai = "{TL}"
    '''.format(TL=TL)
    return cur.execute(cau_truy_van).fetchall()

def insert_tl(mtl,ttl):
    cau_truy_van = '''Insert into "The loai sach"
    Values("{_mtl}","{_ttl}")
    '''.format(_mtl=mtl,_ttl=ttl)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as E:
        return E

def insert_sach(ms,mtl,ts,sl,gia):
    cau_truy_van = '''Insert into "Sach"(ma_sach,ma_the_loai,ten_sach,so_luong,giá)
    values("{_ms}","{_mtl}","{_ts}",{_sl},{_gia})
    '''.format(_ms=ms,_mtl=mtl,_ts=ts,_sl=sl,_gia=gia)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e

def select_tam_NK():
    cau_truy_van = '''select count(*)
    from "Nhat ky muon sach"
    '''
    return cur.execute(cau_truy_van).fetchone()[0]

def insert_NK(tk):
    dem = select_tam_NK()
    dem = int(dem) +1
    chuoi = "MS"+str(dem)
    today = date.today()
    cau_truy_van = '''Insert into "Nhat ky muon sach"
    Values("{_chuoi}","{_tk}","{_today}",{_dem})'''.format(_chuoi=chuoi,_tk=tk,_dem=dem,_today=today)
    print('cau_truy_van: ', cau_truy_van)
    try:
        cur.execute(cau_truy_van)
        return True,chuoi
    except Exception as E:
        return E,False

def insert_chi_tiet(ten,value):
    cau_truy_van = '''insert into "Chi tiet muon sach"
    values("{mms}","{ms}")'''.format(mms=ten,ms=value)
    print('cau_truy_van: ', cau_truy_van)
    try: 
        cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e

# a = insert_nhan_vien("sang","123","Sang","2000-08-04","123131","123131321")
# print('a: ', a)
# if a== True:
#     con.commit()