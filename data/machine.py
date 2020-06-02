#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT PEMANGGIL

from os import system
from data import clr

while True:
    system(clr.d)
    print("MULTI KALKULATOR")
    print("""-------------------------------------------------------
Silahkan pilih jenis kalkulator yang anda inginkan
1. Kalkulator Numerik [COMING SOON]
2. Kalkulator Konversi Suhu [COMING SOON]
3. Kalkulator Konversi Waktu 
4. Kalkulator Konversi Mata Uang
5. Kalkulator Berat Badan Ideal
6. Kalkulator Konversi Satuan Panjang 
7. Kalkulator Konversi Satuan Berat 
8. Kalkulator Konversi Satuan Luas
9. Kalkulator Volume Bangun Ruang
10. Kalkulator Perhitungan Bunga Bank
11. Kalkulator Estimasi Biaya Listrik Bulanan
0. Keluar
-------------------------------------------------------""")

    jenis = input("Respon: ")
    
    if jenis == '1':
        system(clr.d)
        print('COMING SOON')
        print()
        input('Tekan enter untuk keluar...')
        system(clr.d)
        break
            
    elif jenis == '2':
        system(clr.d)
        print('COMING SOON')
        print()
        input('Tekan enter untuk keluar...')
        system(clr.d)
        break
            
    elif jenis == '3':
        from data import time
        system(clr.d)
        break
    
    elif jenis == '4':
        from data import kurs
        system(clr.d)
        break
    
    elif jenis == '5':
        from data import bbi
        system(clr.d)
        break
    
    elif jenis == '6':
        from data import panjang
        system(clr.d)
        break
            
    elif jenis == '7':
        from data import berat
        system(clr.d)
        break
            
    elif jenis == '8':
        from data import luas
        system(clr.d)
        break
    
    elif jenis == '9':
        from data import volume
        system(clr.d)
        break
    
    elif jenis == '10':
        from data import bunga
        system(clr.d)
        break
    
    elif jenis == '11':
        from data import listrik
        system(clr.d)
        break
    
    elif jenis == '0':
        system(clr.d)
        break
