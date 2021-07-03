import sqlite3
from sqlite3.dbapi2 import Cursor
import hashlib
import string
import random
from tkinter import BooleanVar
from typing import List

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

# a = insert_nhan_vien("sang","123","Sang","2000-08-04","123131","123131321")
# print('a: ', a)
# if a== True:
#     con.commit()