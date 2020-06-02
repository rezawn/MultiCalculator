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
    
    jenis = input('Respon: ')
    
    if jenis == '1':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN KILOMETER PERSEGI')
            
            a = float(input('Inputkan nilai luas dalam satuan kilometer persegi : '))
            
            b = a*10**2
            c = a*10**4
            d = a*10**6
            e = a*10**8
            f = a*10**10
            g = a*10**12
            
            print()
            print(f"""Luas dalam {a} kilometer persegi dikonversi menjadi
1. Hektometer persegi (Hektare) = {b} hm persegi
2. Dekameter persegi (Are) = {c} dam persegi
3. Meter persegi = {d} m persegi
4. Desimeter persegi = {e} dm persegi
5. Centimeter persegi = {f} cm persegi
6. Milimeter persegi = {g} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '2':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN HEKTOMETER PERSEGI ATAU HEKTAR')
            
            a = float(input('Inputkan nilai luas dalam satuan hektometer persegi (hektar) : '))
            
            b = a/10**2
            c = a*10**2
            d = a*10**4
            e = a*10**6
            f = a*10**8
            g = a*10**10
            
            print()
            print(f"""Luas dalam {a} hektometer persegi (hektar) dikonversi menjadi
1. Kilometer persegi = {b} km persegi    
2. Dekameter persegi (Are) = {c} dam persegi
3. Meter persegi = {d} m persegi
4. Desimeter persegi = {e} dm persegi
5. Centimeter persegi = {f} cm persegi
6. Milimeter persegi = {g} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '3':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN DEKAMETER PERSEGI ATAU ARE')
            
            a = float(input('Inputkan nilai luas dalam satuan dekameter (are) persegi : '))
            
            b = a/10**4
            c = a/10**2
            d = a*10**2
            e = a*10**4
            f = a*10**6
            g = a*10**8
            
            print()
            print(f"""Luas dalam {a} dekameter persegi (are) dikonversi menjadi
1. Kilometer persegi = {b} km persegi
2. Hektometer persegi (hektar) = {c} hm persegi
3. Meter persegi = {d} m persegi
4. Desimeter persegi = {e} dm persegi          
5. Centimeter persegi = {f} cm persegi
6. Milimeter persegi = {g} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '4':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN METER PERSEGI')
            
            a = float(input('Inputkan nilai luas dalam satuan meter persegi : '))
            
            b = a/10**6
            c = a/10**4
            d = a/10**2
            e = a*10**2
            f = a*10**4
            g = a*10**6
            
            print()
            print(f"""Luas dalam {a} meter persegi dikonversi menjadi
1. Kilometer persegi = {b} km persegi
2. Hektometer persegi (hektar) = {c} hm persegi
3. Dekameter persegi (are) = {d} dam persegi
4. Desimeter persegi = {e} dm persegi
5. Centimeter persegi = {f} cm persegi
6. Milimeter persegi = {g} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '5':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN DESIMETER PERSEGI')
            
            a = float(input('Inputkan nilai luas dalam satuan desimeter persegi : '))
            
            b = a/10**8
            c = a/10**6
            d = a/10**4
            e = a/10**2
            f = a*10**2
            g = a*10**4
            
            print()
            print(f"""Luas dalam {a} desimeter persegi dikonversi menjadi
1. Kilometer persegi = {b} km persegi
2. Hektometer persegi (hektar) = {c} hm persegi
3. Dekameter persegi (are) = {d} dam persegi
4. Meter persegi = {e} m persegi
5. Centimeter persegi = {f} cm persegi
6. Milimeter persegi = {g} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '6':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN CENTIMETER PERSEGI')
            
            a = float(input('Inputkan nilai luas dalam satuan centimeter persegi : '))
            
            b = a/10**10
            c = a/10**8
            d = a/10**6
            e = a/10**4
            f = a/10**2
            g = a*10**2
            
            print()
            print(f"""Luas dalam {a} centimeter persegi dikonversi menjadi
1. Kilometer persegi = {b} km persegi
2. Hektometer persegi (hektar) = {c} hm persegi
3. Dekameter persegi (are) = {d} dam persegi
4. Meter persegi = {e} m persegi
5. Desimeter persegi = {f} dm persegi
6. Milimeter persegi = {g} mm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '7':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('MENGKONVERSI NILAI LUAS DALAM SATUAN MILIMETER PERSEGI')
            
            a = float(input('Inputkan nilai luas dalam satuan milimeter persegi : '))
            
            b = a/10**12
            c = a/10**10
            d = a/10**8
            e = a/10**6
            f = a/10**4
            g = a/10**2
            
            print()
            print(f"""Luas dalam {a} milimeter persegi dikonversi menjadi
1. Kilometer persegi = {b} km persegi
2. Hektometer persegi (hektar) = {c} hm persegi
3. Dekameter persegi (are) = {d} dam persegi
4. Meter persegi = {e} m persegi
5. Desimeter persegi = {f} dm persegi
6. Centimeter persegi = {g} cm persegi""")
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '0':
        system(clr.d)
        break
        
