#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from os import system
from data import clr

    
name = []
power = []
usage = []
    
while True:
    system(clr.d)
    print('KALKULATOR ESTIMASI BIAYA LISTRIK BULANAN')
    print("""-------------------------------------------------------
Berikan data semua barang elektronik yang ada di rumah anda
-------------------------------------------------------\n""")

    input('Tekan enter untuk melanjutkan...')
    
    while True:
        system(clr.d)
        print('KALKULATOR ESTIMASI BIAYA LISTRIK BULANAN')
        print("-------------------------------------------------------")
        
        nama = input('Inputkan nama barang: ')
        name.append(nama)
        daya = int(input(f'Besar daya {nama} dalam watt: '))
        power.append(daya)
        waktu = int(input(f'Lama penggunaan {nama} per hari dalam jam: '))
        usage.append(waktu)
        
        print()
        nextdata = input('Tambahkan data barang yang lain (y/n) ? ')
        if nextdata != 'y':
            break
    
    system(clr.d) 
    print('KALKULATOR ESTIMASI BIAYA LISTRIK BULANAN')
    print("-------------------------------------------------------")
    
    multiple = []

    for x in range(0, len(power)):
        total = 0
        total = total + (power[x]*usage[x])
        multiple.append(total)
    
    powday = (sum(multiple))/1000
    powmonth = powday*30
    
    pricelist = int(input('Inputkan harga listrik per Kwh: '))

    price = powmonth*pricelist

    system(clr.d)
    print('KALKULATOR ESTIMASI BIAYA LISTRIK BULANAN')
    print("-------------------------------------------------------")
    
    print(f'Estimasi biaya listrik anda dalam sebulan sebesar {price}')
    
    print()
    ulang = input('Apakah anda ingin menggunakan kalkulator ini lagi? (y/n) ')
    if ulang != 'y':
        break
    
