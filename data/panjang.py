#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KALKULATOR KONVERSI PANJANG

from os import system
from data import clr

iterasi = True
while iterasi:
  system(clr.d)
  print('KALKULATOR KONVERSI SATUAN PANJANG')
  print("""-------------------------------------------------------
Pilih satuan panjang yang akan dikonversi
1. Kilometer (Km)
2. Hektometer (Hm)
3. Dekameter (Dam)
4. Meter (m)
5. Desimeter (Dm)
6. Centimeter (Cm)
7. Milimeter (Mm)
0. Keluar
-------------------------------------------------------""")
  
  jenis = input('Respon: ')
  
  if jenis == '1':
    iterasi = True 
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN KILOMETER')
      
      a = float(input('Inputkan nilai panjang dalam satuan kilometer : '))
      
      b = a*10
      c = a*100
      d = a*1000
      e = a*10000
      f = a*100000
      g = a*1000000
      
      print()
      print(f"""Panjang dalam {a} kilometer dikonversi menjadi
Hektometer = {b} hm
Dekameter = {c} dam
Meter = {d} m
Desimeter = {e} dm
Centimeter = {f} cm
Milimeter = {g} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '2':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN HEKTOMETER')
      
      a = float(input('Inputkan nilai panjang dalam satuan hektometer : '))
      
      b = a/10
      c = a*10
      d = a*100
      e = a*1000
      f = a*10000
      g = a*100000
      
      print()
      print(f"""Panjang dalam {a} hektometer dikonversi menjadi
Kilometer = {b} km
Dekameter = {c} hm
Meter = {d} m
Desimeter = {e} dm
Centimeter = {f} cm
Milimeter = {g} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '3':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN DEKAMETER')
      
      a = float(input('Inputkan nilai panjang dalam satuan dekameter : '))
      
      b = a/100
      c = a/10
      d = a*10
      e = a*100
      f = a*1000
      g = a*10000
      
      print()
      print(f"""Panjang dalam {a} dekameter dikonversi menjadi
Kilometer = {b} km
Hektometer = {c} hm
Meter = {d} m
Desimeter = {e} dm
Centimeter = {f} cm
Milimeter = {g} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
      
  elif jenis == '4':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN METER')
      
      a = float(input('Inputkan nilai panjang dalam satuan meter : '))
      
      b = a/1000
      c = a/100
      d = a/10
      e = a*10
      f = a*100
      g = a*1000
      
      print()
      print(f"""Panjang dalam {a} meter dikonversi menjadi
Kilometer = {b} km
Hektometer = {c} hm
Dekameter = {d} dam
Desimeter = {e} dm
Centimeter = {f} cm
Milimeter = {g} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '5':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN DESIMETER')
      
      a = float(input('Inputkan nilai panjang dalam satuan desimeter : '))
      
      b = a/10000
      c = a/1000
      d = a/100
      e = a/10
      f = a*10
      g = a*100
      
      print()
      print(f"""Panjang dalam {a} desimeter dikonversi menjadi
Kilometer = {b} km
Hektometer = {c} hm
Dekameter = {d} dam
Meter = {e} m
Centimeter = {f} cm
Milimeter = {g} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '6':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN CENTIMETER')
      
      a = float(input('Inputkan nilai panjang dalam satuan centimeter : '))
      
      b = a/100000
      c = a/10000
      d = a/1000
      e = a/100
      f = a/10
      g = a*10
      
      print()
      print(f"""Panjang dalam {a} centimeter dikonversi menjadi
Kilometer = {b} km
Hektometer = {c} hm
Dekameter = {d} dam
Meter = {e} m
Desimeter = {f} dm
Milimeter = {g} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '7':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN MILIMETER')
      
      a = float(input('Inputkan nilai panjang dalam satuan milimeter : '))
      
      b = a/1000000
      c = a/100000
      d = a/10000
      e = a/1000
      f = a/100
      g = a/10
      
      print()
      print(f"""Panjang dalam {a} milimeter dikonversi menjadi
Kilometer = {b} km
Hektometer = {c} hm
Dekameter = {d} dam
Meter = {e} m
Desimeter = {f} dm
Centimeter = {g} cm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '0':
    system(clr.d)
    break

      
      





    
