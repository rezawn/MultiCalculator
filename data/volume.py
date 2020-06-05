#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KALKULATOR VOLUME

from os import system
from data import clr

iterasi = True
while iterasi:
    system(clr.d)
    print('KALKULATOR VOLUME BANGUN RUANG')
    print("""----------------------------------------------
Pilih Bangun Ruang :
1. Kubus
2. Balok
3. Prisma Segitiga
4. Limas Segitiga
5. Limas Segiempat
6. Tabung
7. Kerucut
8. Bola
0. Keluar
-----------------------------------------------------------""")

    jenis = input('Bangun Ruang: ')

    if jenis == '1':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME KUBUS')
            s=float(input('sisi:'))
            v=s**3
            print('Volume Kubus: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
    
    elif jenis == '2':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME BALOK')
            p=float(input('panjang:'))
            l=float(input('lebar:'))
            Tb=float(input('tinggi balok:'))
            v=p*l*Tb
            print('Volume Balok: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
    
    elif jenis == '3':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME PRISMA SEGITIGA')
            a=float(input('alas:'))
            t=float(input('tinggi alas segitiga:'))
            Tp=float(input('tinggi prisma:'))
            LA=(a*t)/2
            v=LA*Tp
            print('Volume Prisma Segitiga: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break

    elif jenis == '4':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME LIMAS SEGITIGA')
            a=float(input('alas:'))
            t=float(input('tinggi alas segitiga:'))
            Tl=float(input('tinggi limas:'))
            LA=(a*t)/2
            v=(LA*Tl)/3
            print('Volume Limas Segitiga: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
 
    elif jenis == '5':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME LIMAS SEGIEMPAT')
            p=float(input('panjang alas:'))
            l=float(input('lebar alas:'))
            Tl=float(input('tinggi limas:'))
            LA=p*l
            v=(LA*Tl)/3
            print('Volume Limas Segitiga: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '6':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME TABUNG')
            r=float(input('jari-jari:'))
            Tt=float(input('tinggi tabung:'))
            LA=(22/7.0)*r*r
            v=LA*Tt
            print('Volume Tabung: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
    
    elif jenis == '7':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME KERUCUT')
            r=float(input('jari-jari:'))
            Tk=float(input('tinggi kerucut:'))
            LA=(22/7.0)*r*r
            v=(LA*Tk)/3
            print('Volume Kerucut: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
    
    elif jenis == '8':
        loop = True
        while loop == True:
            system(clr.d)
            print('MENGHITUNG VOLUME BOLA')
            r=float(input('jari-jari:'))
            v=(4*(22/7.0)*r**3)/3
            print('Volume Bola: ',v)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break

    elif jenis == '0':
        system(clr.d)
        break
        
        
        
        
        
        
