#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KONVERSI WAKTU

from os import system
from data import clr

while True:
    system(clr.d)
    print('KALKULATOR KONVERSI WAKTU')
    print('''-------------------------------------------------------
Pilih satuan waktu yang akan anda konversi
1. Detik
2. Menit
3. Jam
4. Hari
0. Keluar
-------------------------------------------------------''')

    jenis = input('Respon: ')
    
    if jenis == '1':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI DETIK')
            print('-------------------------------------------------------')
            a = float(input('Inputkan waktu dalam detik: '))
            b = a/60
            c = b/60
            d = c/24
            
            print()
            print(f'''Waktu dalam {a} detik dikonversi menjadi
Menit  : {b} menit
Jam    : {c} jam
Hari   : {d} hari''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break

    elif jenis == '2':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI MENIT')
            print('-------------------------------------------------------')
            a = float(input('Inputkan waktu dalam menit: '))
            b = a*60
            c = a/60
            d = c/24
            
            print()
            print(f'''Waktu dalam {a} menit dikonversi menjadi
Detik  : {b} Detik
Jam    : {c} jam
Hari   : {d} hari''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break
     
    elif jenis == '3':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI JAM')
            print('-------------------------------------------------------')
            a = float(input('Inputkan waktu dalam jam: '))
            b = a*3600
            c = a*60
            d = a/24
            
            print()
            print(f'''Waktu dalam {a} jam dikonversi menjadi
Detik  : {b} Detik
Menit  : {c} menit
Hari   : {d} hari''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break
    
    elif jenis == '4':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI HARI')
            print('-------------------------------------------------------')
            a = float(input('Inputkan waktu dalam hari: '))
            b = a*24
            c = b*60
            d = c*60
            
            print()
            print(f'''Waktu dalam {a} hari dikonversi menjadi
Detik  : {d} Detik
Menit  : {c} menit
Jam    : {b} jam''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break
    
    elif jenis == '0':
        system(clr.d)
        break    
