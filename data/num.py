#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KALKULATOR NUMERIK

from os import system
from data import clr

while True:
    system(clr.d)
    from math import *
            
    print('KALKULATOR NUMERIK')
    print("""-------------------------------------------------------
PETUNJUK PENGGUNAAN
# Gunakan + untuk penjumlahan
# Gunakan - untuk pengurangan
# Gunakan * untuk perkalian
# Gunakan / untuk pembagian
# Gunakan ** untuk perpangkatan dan akar
# Gunakan *z untuk mengubah radian ke derajat
# Gunakan *y untuk mengubah derajat ke radian
# Pada trigonometri gunakan format sin(x) untuk x dalam radian
# Untuk nilai arc gunakan format asin(x) hasil dalam radian
# Gunakan penulisan tanda dalam kurung dengan benar

Contoh: 1+(1*(4**0.5))
-------------------------------------------------------""")
    z = pi/179.99999999999998
    y = 1/z
            
    h = input()
    i = str(h)
    j = eval(i)
        
    print()
    print('Hasil perhitungan adalah', j)
    print()
            
    ulang = input("Apakah anda ingin menggunakan kalkulator numerik lagi? (y/n) ")
    if ulang != 'y':
        system(clr.d)
        break
