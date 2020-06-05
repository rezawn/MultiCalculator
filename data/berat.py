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
                    
            b = float(input('Inputkan nilai berat dalam satuan kilogram : '))
        
            a = b/1000
            c = b*10
            d = b*100
            e = b*1000
            f = b*10000
            g = b*100000
            h = b*1000000
            
            print("---------------------------------------------------")
            print(f"""Berat {b} Kilogram Dikonversi menjadi :
Ton        :{a} Ton
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
                    
            c = float(input('Inputkan nilai berat dalam satuan hektogram : '))
        
            a = c/10000
            b = c/10
            d = c*10
            e = c*100
            f = c*1000
            g = c*10000
            h = c*100000
            
            print("---------------------------------------------------")
            print(f"""Berat {c} Hektogram Dikonversi menjadi :
Ton        :{a} Ton
Kilogram   :{b} Kg
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
                    
            d = float(input('Inputkan nilai berat dalam satuan dekagram : '))
        
            a = d/100000
            b = d/100
            c = d/10
            e = d*10
            f = d*100
            g = d*1000
            h = d*10000
            
            print("---------------------------------------------------")
            print(f"""Berat {d} Dekagram Dikonversi menjadi :
Ton        :{a} Ton
Kilogram   :{b} Kg
Hektogram  :{c} Hg
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
                    
            e = float(input('Inputkan nilai berat dalam satuan gram : '))
            
            a = e/1000000
            b = e/1000
            c = e/100
            d = e/10
            f = e*10
            g = e*100
            h = e*1000
            
            print("---------------------------------------------------")
            print(f"""Berat {e} Gram Dikonversi menjadi :
Ton        :{a} Ton
Kilogram   :{b} Kg
Hektogram  :{c} Hg
Dekagram   :{d} Dag
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
                        
            f = float(input('Inputkan nilai berat dalam satuan desigram : '))
        
            a = f/10000000
            b = f/10000
            c = f/1000
            d = f/100
            e = f/10
            g = f*10
            h = f*100
            
            print("---------------------------------------------------")
            print(f"""Berat {f} Desigram Dikonversi menjadi :
Ton        :{a} Ton
Kilogram   :{b} Kg
Hektogram  :{c} Hg
Dekagram   :{d} Dag
Gram       :{e} G
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
                    
            g = float(input('Inputkan nilai berat dalam satuan centigram : '))
        
            a = g/100000000
            b = g/100000
            c = g/10000
            d = g/1000
            e = g/100
            f = g/10
            h = g*10
            
            print("---------------------------------------------------")
            print(f"""Berat {g} Centigram Dikonversi menjadi :
Ton        :{a} Ton
Kilogram   :{b} Kg
Hektogram  :{c} Hg
Dekagram   :{d} Dag
Gram       :{e} G
Desigram   :{f} Dg
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
                    
            h = float(input('Inputkan nilai berat dalam satuan miligram : '))
        
            a = h/1000000000
            b = h/1000000
            c = h/100000
            d = h/10000
            e = h/1000
            f = h/100
            g = h/10
            
            print("---------------------------------------------------")
            print(f"""Berat {h} Miligram Dikonversi menjadi :
Ton        :{a} Ton
Kilogram   :{b} Kg
Hektogram  :{c} Hg
Dekagram   :{d} Dag
Gram       :{e} G
Desigram   :{f} Dg
Centigram  :{g} Cg     
------------------------------------------------------""")
            ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
            if ulang != 'y':
                break
            
    elif jenis == '0':
        system(clr.d)
        break
