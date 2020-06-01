#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KONVERSI MATA UANG

from os import system
from data import clr

system(clr.d)
print('KALKULATOR KONVERSI MATA UANG')
print('-------------------------------------------------------')
    
kurs = {}
    
uangdi = input('Inputkan jenis mata uang pertama: ')
uangter = input('Inputkan jenis mata uang kedua: ')

kurs['dikonversi'] = uangdi
kurs['terkonversi'] = uangter

system(clr.d)
print('KALKULATOR KONVERSI MATA UANG')
print('-------------------------------------------------------')
print('''PETUNJUK
Untuk nilai tukar yang lebih kecil dianjurkan untuk
menggunakan perbandingan.

misal: 1/10000
-------------------------------------------------------''')

print()
nilai = input(f"Inputkan nilai tukar mata uang {kurs['dikonversi']} dalam {kurs['terkonversi']}: ")
hit = eval(nilai)

kurs['nilaitukar'] = hit

print() 
input('Tekan enter untuk melanjutkan...')
    
while True:
    system(clr.d)
    print('KALKULATOR KONVERSI MATA UANG')
    print('-------------------------------------------------------')
    print(f'''Jenis mata uang yang telah diinputkan
1. {kurs['dikonversi']}
2. {kurs['terkonversi']}
-------------------------------------------------------''')

    pilih = input('Pilih jenis mata uang yang akan dikonversi: ')
    
    if pilih == '1':
        system(clr.d)
        print('KALKULATOR KONVERSI MATA UANG')
        print('-------------------------------------------------------')
        
        a = float(input(f"Inputkan jumlah uang dalam {kurs['dikonversi']} yang akan dikonversi: "))
        b = a*kurs['nilaitukar']
        
        print()
        print(f"Uang senilai {a} {kurs['dikonversi']} setara dengan {b} {kurs['terkonversi']}")
            
        print()
        ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
        if ulang != 'y':
            system(clr.d)
            break
        
    elif pilih == '2':
        system(clr.d)
        print('KALKULATOR KONVERSI MATA UANG')
        print('-------------------------------------------------------')
        
        a = float(input(f"Inputkan jumlah uang dalam {kurs['terkonversi']} yang akan dikonversi: "))
        b = a*(1/kurs['nilaitukar'])
        
        print()
        print(f"Uang senilai {a} {kurs['terkonversi']} setara dengan {b} {kurs['dikonversi']}")
         
        print()
        ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
        if ulang != 'y':
            system(clr.d)
            break