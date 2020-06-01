#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KALKULATOR KONVERSI BERAT

from os import system
from data import clr

iterasi = True
while iterasi:
    system(clr.d)
    print('KALKULATOR KONVERSI SATUAN BERAT')
    print("""-------------------------------------------------------
Pilih satuan berat yang ingin anda konversi
  1. Ton
  2. Kilogram
  3. Hektogram
  4. Dekagram
  5. Gram
  6. Desigram
  7. Centigram
  8. Miligram
  0. Keluar
-------------------------------------------------------""")

    jenis = input("Respon :")

    if jenis == '1':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN TON')
                    
            a = float(input('Inputkan nilai berat dalam satuan ton : '))
        
            b = a*1000
            c = a*10000
            d = a*100000
            e = a*1000000
            f = a*10000000
            g = a*100000000
            h = a*1000000000
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Ton Dikonversi menjadi :
Kilogram   :{b} Kg
Hektogram  :{c} Hg
Dekagram   :{d} Dag
Gram       :{e} G
Desigram   :{f} Dg
Centigram  :{g} Cg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '2':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN KILOGRAM')
                    
            a = float(input('Inputkan nilai berat dalam satuan kilogram : '))
        
            b = a/1000
            c = a*10
            d = a*100
            e = a*1000
            f = a*10000
            g = a*100000
            h = a*1000000
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Kilogram Dikonversi menjadi :
Ton        :{b} Ton
Hektogram  :{c} Hg
Dekagram   :{d} Dag
Gram       :{e} G
Desigram   :{f} Dg
Centigram  :{g} Cg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '3':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN HEKTOGRAM')
                    
            a = float(input('Inputkan nilai berat dalam satuan hektogram : '))
        
            b = a/10000
            c = a/10
            d = a*10
            e = a*100
            f = a*1000
            g = a*10000
            h = a*100000
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Hektogram Dikonversi menjadi :
Ton        :{b} Ton
Kilogram   :{c} Kg
Dekagram   :{d} Dag
Gram       :{e} G
Desigram   :{f} Dg
Centigram  :{g} Cg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '4':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN DEKAGRAM')
                    
            a = float(input('Inputkan nilai berat dalam satuan dekagram : '))
        
            b = a/100000
            c = a/100
            d = a/10
            e = a*10
            f = a*100
            g = a*1000
            h = a*10000
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Dekagram Dikonversi menjadi :
Ton        :{b} Ton
Kilogram   :{c} Kg
Hektogram  :{d} Hg
Gram       :{e} G
Desigram   :{f} Dg
Centigram  :{g} Cg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '5':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN GRAM')
                    
            a = float(input('Inputkan nilai berat dalam satuan gram : '))
            
            b = a/1000000
            c = a/1000
            d = a/100
            e = a/10
            f = a*10
            g = a*100
            h = a*1000
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Gram Dikonversi menjadi :
Ton        :{b} Ton
Kilogram   :{c} Kg
Hektogram  :{d} Hg
Dekagram   :{e} Dag
Desigram   :{f} Dg
Centigram  :{g} Cg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '6':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN DESIGRAM')
                        
            a = float(input('Inputkan nilai berat dalam satuan desigram : '))
        
            b = a/10000000
            c = a/10000
            d = a/1000
            e = a/100
            f = a/10
            g = a*10
            h = a*100
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Desigram Dikonversi menjadi :
Ton        :{b} Ton
Kilogram   :{c} Kg
Hektogram  :{d} Hg
Dekagram   :{e} Dag
Gram       :{f} G
Centigram  :{g} Cg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '7':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN CENTIGRAM')
                    
            a = float(input('Inputkan nilai berat dalam satuan centigram : '))
        
            b = a/100000000
            c = a/100000
            d = a/10000
            e = a/1000
            f = a/100
            g = a/10
            h = a*10
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Centigram Dikonversi menjadi :
Ton        :{b} Ton
Kilogram   :{c} Kg
Hektogram  :{d} Hg
Dekagram   :{e} Dag
Gram       :{f} G
Desigram   :{g} Dg
Miligram   :{h} Mg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
        
    elif jenis == '8':
        loop = True
        while loop == True:
            system(clr.d)
            print()
            print('MENGKONVERSI BERAT DARI SATUAN MILIGRAM')
                    
            a = float(input('Inputkan nilai berat dalam satuan miligram : '))
        
            b = a/1000000000
            c = a/1000000
            d = a/100000
            e = a/10000
            f = a/1000
            g = a/100
            h = a/10
            
            print("---------------------------------------------------")
            print(f"""Berat {a} Miligram Dikonversi menjadi :
Ton        :{b} Ton
Kilogram   :{c} Kg
Hektogram  :{d} Hg
Dekagram   :{e} Dag
Gram       :{f} G
Desigram   :{g} Dg
Centigram  :{h} Cg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '0':
        system(clr.d)
        break
