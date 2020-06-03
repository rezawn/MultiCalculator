#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KONVERSI MATA UANG ONLINE

from os import system
from data import clr

system(clr.d)
print('KALKULATOR KONVERSI MATA UANG')
print('-------------------------------------------------------')
input('''WARNING: Diperlukan koneksi internet

      

Tekan enter untuk melanjutkan...''')

system(clr.d)
print('getting environment...')
system('pip install requests')
import requests

curr = ['USD','AUD','CAD','CNY','EUR','GBP','JPY','MXN','IDR']

while True:
    system(clr.d)
    print('KALKULATOR KONVERSI MATA UANG')
    print('-------------------------------------------------------')
    print('''Pilih jenis konversi di bawah ini
1. Dollar Amerika "USD" ke Rupiah "IDR"
2. Dollar Australia "AUD" ke Rupiah "IDR"
3. Dollar Kanada "CAD" ke Rupiah "IDR"
4. Yuan "CNY" ke Rupiah "IDR"
5. Euro "EUR" ke Rupiah "IDR"
6. Poundsterling "GBP" ke Rupiah "IDR"
7. Yen "JPY" ke Rupiah "IDR"
8. Peso Meksiko "MXN" ke Rupiah "IDR"
0. Keluar
-------------------------------------------------------\n''')

    jenis = int(input('Respon: '))

    if jenis >= 1:
        system(clr.d)
    
        print('KALKULATOR KONVERSI MATA UANG')
        print('-------------------------------------------------------')
        url = "http://markets.money.cnn.com/common/modules/iframe/currencyConverter.asp"

        jumlah = input(f"Masukkan jumlah uang dalam {curr[jenis-1]} yang akan dikonversi : ")

        req = f"..requester..=ContentBuffer&convert=1&base={curr[jenis-1]}&quote=IDR&amount="+ str(jumlah)
        app = {'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache"}
        res = requests.request("POST", url, data=req, headers=app)

        print(str(jumlah) +' '+ curr[jenis-1] +' '+ res.text)
        
        print()
        ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
        if ulang != 'y':
            system(clr.d)
            break
    
    elif jenis == 0:
        system(clr.d)
        break