#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KALKULATOR LUAS

from os import system
from data import clr

iterasi = True
while iterasi:
    system(clr.d)
    print('KALKULATOR KONVERSI SATUAN LUAS')
    print("""-------------------------------------------------------
Pilih satuan luas yang akan dikonversi
1. Kilometer persegi
2. Hektometer persegi (Hektar)
3. Dekameter persegi (Are)
4. Meter persegi
5. Desimeter persegi 
6. Centimeter persegi
7. Milimeter persegi
0. Keluar
-------------------------------------------------------""")
    
    jenis = input('Satuan yang akan dikonversi: ')
    
    if jenis == '1':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN KILOMETER PERSEGI')
            
            LKm = float(input('Inputkan nilai luas dalam satuan kilometer persegi : '))
            
            LHm = LKm*10**2
            LDam = LKm*10**4
            LM = LKm*10**6
            LDm = LKm*10**8
            LCm = LKm*10**10
            LMm = LKm*10**12
            
            print()
            print(f"""Luas dalam {LKm} kilometer persegi dikonversi menjadi
1. Hektometer persegi (Hektare) = {LHm} hm persegi
2. Dekameter persegi (Are) = {LDam} dam persegi
3. Meter persegi = {LM} m persegi
4. Desimeter persegi = {LDm} dm persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '2':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN HEKTOMETER PERSEGI ATAU HEKTAR')
            
            LHm = float(input('Inputkan nilai luas dalam satuan hektometer persegi (hektar) : '))
            
            LKm = LHm/10**2
            LDam = LHm*10**2
            LM = LHm*10**4
            LDm = LHm*10**6
            LCm = LHm*10**8
            LMm = LHm*10**10
            
            print()
            print(f"""Luas dalam {LHm} hektometer persegi (hektar) dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi    
2. Dekameter persegi (Are) = {LDam} dam persegi
3. Meter persegi = {LM} m persegi
4. Desimeter persegi = {LDm} dm persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '3':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN DEKAMETER PERSEGI ATAU ARE')
            
            LDam = float(input('Inputkan nilai luas dalam satuan dekameter (are) persegi : '))
            
            LKm = LDam/10**4
            LHm = LDam/10**2
            LM = LDam*10**2
            LDm = LDam*10**4
            LCm = LDam*10**6
            LMm = LDam*10**8
            
            print()
            print(f"""Luas dalam {LDam} dekameter persegi (are) dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Meter persegi = {LM} m persegi
4. Desimeter persegi = {LDm} dm persegi          
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '4':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN METER PERSEGI')
            
            LM = float(input('Inputkan nilai luas dalam satuan meter persegi : '))
            
            LKm = LM/10**6
            LHm = LM/10**4
            LDam = LM/10**2
            LDm = LM*10**2
            LCm = LM*10**4
            LMm = LM*10**6
            
            print()
            print(f"""Luas dalam {LM} meter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Desimeter persegi = {LDm} dm persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '5':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN DESIMETER PERSEGI')
            
            LDm = float(input('Inputkan nilai luas dalam satuan desimeter persegi : '))
            
            LKm = LDm/10**8
            LHm = LDm/10**6
            LDam = LDm/10**4
            LM = LDm/10**2
            LCm = LDm*10**2
            LMm = LDm*10**4
            
            print()
            print(f"""Luas dalam {LDm} desimeter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Meter persegi = {LM} m persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '6':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN CENTIMETER PERSEGI')
            
            LCm = float(input('Inputkan nilai luas dalam satuan centimeter persegi : '))
            
            LKm = LCm/10**10
            LHm = LCm/10**8
            LDam = LCm/10**6
            LM = LCm/10**4
            LDm = LCm/10**2
            LMm = LCm*10**2
            
            print()
            print(f"""Luas dalam {LCm} centimeter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Meter persegi = {LM} m persegi
5. Desimeter persegi = {LDm} dm persegi
6. Milimeter persegi = {LMm} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '7':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN MILIMETER PERSEGI')
            
            LMm = float(input('Inputkan nilai luas dalam satuan milimeter persegi : '))
            
            LKm = LMm/10**12
            LHm = LMm/10**10
            LDam = LMm/10**8
            LM = LMm/10**6
            LDm = LMm/10**4
            LCm = LMm/10**2
            
            print()
            print(f"""Luas dalam {LMm} milimeter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Meter persegi = {LM} m persegi
5. Desimeter persegi = {LDm} dm persegi
6. Centimeter persegi = {LCm} cm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '0':
        system(clr.d)
        break
        
