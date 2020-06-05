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
            C = float(input('Inputkan suhu dalam celcius: '))
                
            R = (4/5)*C
            F = ((9/5)*C)+32
            K = C+273
                
            print()
            print(f"""Suhu dalam {C} derajat celcius dikonversi menjadi
Reamur     : {R} derajat reamur
Fahrenheit : {F} derajat fahrenheit
Kelvin     : {K} kelvin""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
                
    elif jenis == '2':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI DERAJAT REAMUR')
            print('-------------------------------------------------------')
            R = float(input('Inputkan suhu dalam reamur: '))
                    
            C = (5/4)*R
            F = ((9/4)*R)+32
            K = ((5/4)*R)+273
                    
            print()
            print(f"""Suhu dalam {R} derajat reamur dikonversi menjadi
Celcius    : {C} derajat celcius
Fahrenheit : {F} derajat fahrenheit
Kelvin     : {K} kelvin""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '3':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI DERAJAT FAHRENHEIT')
            print('-------------------------------------------------------')
            F = float(input('Inputkan suhu dalam fahrenheit: '))
                    
            C = ((5/9)*(F-32))
            R = ((4/9)*(F-32))
            K = (((5/9)*(F-32))+273)
                    
            print()
            print(f"""Suhu dalam {F} derajat fahrenheit dikonversi menjadi
Celcius    : {C} derajat celcius
Reamur     : {R} derajat reamur
Kelvin     : {K} kelvin""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '4':
        while True:
            system(clr.d)
            print('MENGKONVERSI SUHU DARI KELVIN')
            print('-------------------------------------------------------')
            K = float(input('Inputkan suhu dalam kelvin: '))
                    
            C = K-273
            R = (K-273)*4/5
            F = ((K-273)*(9/5))+32
                    
            print()
            print(f"""Suhu dalam {K} kelvin dikonversi menjadi
Celcius    : {C} derajat celcius
Reamur     : {R} derajat reamur
Fahrenheit : {F} derajat fahrenheit""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '0':
        system(clr.d)
        break
