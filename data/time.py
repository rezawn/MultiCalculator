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
            S = float(input('Inputkan waktu dalam detik: '))
            M = S/60
            J = M/60
            H = J/24
            
            print()
            print(f'''Waktu dalam {S} detik dikonversi menjadi
Menit  : {M} menit
Jam    : {J} jam
Hari   : {H} hari''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break

    elif jenis == '2':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI MENIT')
            print('-------------------------------------------------------')
            M = float(input('Inputkan waktu dalam menit: '))
            S = M*60
            J = M/60
            H = J/24
            
            print()
            print(f'''Waktu dalam {M} menit dikonversi menjadi
Detik  : {S} Detik
Jam    : {J} jam
Hari   : {H} hari''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break
     
    elif jenis == '3':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI JAM')
            print('-------------------------------------------------------')
            J = float(input('Inputkan waktu dalam jam: '))
            S = J*3600
            M = J*60
            H = J/24
            
            print()
            print(f'''Waktu dalam {J} jam dikonversi menjadi
Detik  : {S} Detik
Menit  : {M} menit
Hari   : {H} hari''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break
    
    elif jenis == '4':
        while True:
            system(clr.d)
            print('MENGKONVERSI WAKTU DARI HARI')
            print('-------------------------------------------------------')
            H = float(input('Inputkan waktu dalam hari: '))
            J = H*24
            M = J*60
            S = M*60
            
            print()
            print(f'''Waktu dalam {H} hari dikonversi menjadi
Detik  : {S} Detik
Menit  : {M} menit
Jam    : {J} jam''')
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
            if ulang != 'y':
                break
    
    elif jenis == '0':
        system(clr.d)
        break    
