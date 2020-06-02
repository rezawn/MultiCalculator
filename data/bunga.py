# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:28:42 2020

@author: Cornelius Dianto
"""

from os import system
from data import clr

def BungaSederhana(awal, sukuBunga, waktu):
    nilaiakhir = awal + (awal * (sukuBunga / 100)) * waktu
    return nilaiakhir

def BungaMajemuk(awal, sukuBunga, waktu):
    nilaiakhir = awal * (pow((1 + sukuBunga / 100), waktu))
    return nilaiakhir

iterasi = True
while iterasi:
    system(clr.d)
    print('KALKULATOR PERHITUNGAN BUNGA BANK')
    print("""-------------------------------------------------------
Pilih Jenis Bunga Bank yang Ingin Dihitung
1. Bunga Sederhana
2. Bunga Majemuk
0. Kembali
-------------------------------------------------------""")
    
    jawab = input('Respon: ')
    if jawab == '0':
        system(clr.d)
        break
    
    if jawab == '1':
        iterasi = True
        while iterasi:
            system(clr.d)
            awal = float(input("Masukkan Nilai Awal: "))
            sukuBunga = float(input("Masukkan Suku Bunga: "))
            waktu = float(input("Berapa lama waktunya? "))
            nilaiakhir = BungaSederhana(awal, sukuBunga, waktu)
            print(f"Maka Nilai Akhir yang akan diperoleh adalah ", nilaiakhir)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
    elif jawab == '2':
        iterasi = True
        while iterasi:
            system(clr.d)
            awal = float(input("Masukkan Nilai Awal: "))
            sukuBunga = float(input("Masukkan Suku Bunga: "))
            waktu = float(input("Berapa lama waktunya? "))
            nilaiakhir = BungaMajemuk(awal, sukuBunga, waktu)
            print(f"Maka Nilai Akhir yang akan diperoleh adalah ", nilaiakhir)
            print()
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
    