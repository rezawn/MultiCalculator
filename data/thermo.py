#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KONVERSI SUHU

from os import system
from data import clr

while True:
    system(clr.d)
    print('KALKULATOR KONVERSI SUHU')
    print("""-------------------------------------------------------
Pilih derajat suhu yang ingin anda konversi
1. Celcius
2. Reamur
3. Fahrenheit
4. Kelvin
0. Keluar
-------------------------------------------------------""")
            
    jenis = input('Respon: ')
            
    if jenis == '1':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI DERAJAT CELCIUS')
            print('-------------------------------------------------------')
            a = float(input('Inputkan suhu dalam celcius: '))
                
            b = (4/5)*a
            c = ((9/5)*a)+32
            d = a+273
                
            print()
            print(f"""Suhu dalam {a} derajat celcius dikonversi menjadi
Reamur     : {b} derajat reamur
Fahrenheit : {c} derajat fahrenheit
Kelvin     : {d} kelvin""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
                
    elif jenis == '2':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI DERAJAT REAMUR')
            print('-------------------------------------------------------')
            a = float(input('Inputkan suhu dalam reamur: '))
                    
            b = (5/4)*a
            c = ((9/4)*a)+32
            d = ((5/4)*a)+273
                    
            print()
            print(f"""Suhu dalam {a} derajat reamur dikonversi menjadi
Celcius    : {b} derajat celcius
Fahrenheit : {c} derajat fahrenheit
Kelvin     : {d} kelvin""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '3':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI DERAJAT FAHRENHEIT')
            print('-------------------------------------------------------')
            a = float(input('Inputkan suhu dalam fahrenheit: '))
                    
            b = ((5/9)*(a-32))
            c = ((4/9)*(a-32))
            d = (((5/9)*(a-32))+273)
                    
            print()
            print(f"""Suhu dalam {a} derajat fahrenheit dikonversi menjadi
Celcius    : {b} derajat celcius
Reamur     : {c} derajat reamur
Kelvin     : {d} kelvin""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '4':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI KELVIN')
            print('-------------------------------------------------------')
            a = float(input('Inputkan suhu dalam kelvin: '))
                    
            b = a-273
            c = (a-273)*4/5
            d = ((a-273)*(9/5))+32
                    
            print()
            print(f"""Suhu dalam {a} kelvin dikonversi menjadi
Celcius    : {b} derajat celcius
Reamur     : {c} derajat reamur
Fahrenheit : {d} derajat fahrenheit""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '0':
        system(clr.d)
        break
