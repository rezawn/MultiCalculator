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
      
      PKm = float(input('Inputkan nilai panjang dalam satuan kilometer : '))
      
      PHm = PKm*10
      PDam = PKm*100
      PM = PKm*1000
      PDm = PKm*10000
      PCm = PKm*100000
      PMm = PKm*1000000
      
      print()
      print(f"""Panjang dalam {PKm} kilometer dikonversi menjadi
Hektometer = {PHm} hm
Dekameter = {PDam} dam
Meter = {PM} m
Desimeter = {PDm} dm
Centimeter = {PCm} cm
Milimeter = {PMm} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '2':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN HEKTOMETER')
      
      PHm = float(input('Inputkan nilai panjang dalam satuan hektometer : '))
      
      PKm = PHm/10
      PDam = PHm*10
      PM = PHm*100
      PDm = PHm*1000
      PCm = PHm*10000
      PMm = PHm*100000
      
      print()
      print(f"""Panjang dalam {PHm} hektometer dikonversi menjadi
Kilometer = {PKm} km
Dekameter = {PDam} hm
Meter = {PM} m
Desimeter = {PDm} dm
Centimeter = {PCm} cm
Milimeter = {PMm} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '3':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN DEKAMETER')
      
      PDam = float(input('Inputkan nilai panjang dalam satuan dekameter : '))
      
      PKm = PDam/100
      PHm = PDam/10
      PM = PDam*10
      PDm = PDam*100
      PCm = PDam*1000
      PMm = PDam*10000
      
      print()
      print(f"""Panjang dalam {PDam} dekameter dikonversi menjadi
Kilometer = {PKm} km
Hektometer = {PHm} hm
Meter = {PM} m
Desimeter = {PDm} dm
Centimeter = {PCm} cm
Milimeter = {PMm} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
      
  elif jenis == '4':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN METER')
      
      PM = float(input('Inputkan nilai panjang dalam satuan meter : '))
      
      PKm = PM/1000
      PHm = PM/100
      PDam = PM/10
      PDm = PM*10
      PCm = PM*100
      PMm = PM*1000
      
      print()
      print(f"""Panjang dalam {PM} meter dikonversi menjadi
Kilometer = {PKm} km
Hektometer = {PHm} hm
Dekameter = {PDam} dam
Desimeter = {PDm} dm
Centimeter = {PCm} cm
Milimeter = {PMm} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '5':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN DESIMETER')
      
      PDm = float(input('Inputkan nilai panjang dalam satuan desimeter : '))
      
      PKm = PDm/10000
      PHm = PDm/1000
      PDam = PDm/100
      PM = PDm/10
      PCm = PDm*10
      PMm = PDm*100
      
      print()
      print(f"""Panjang dalam {PDm} desimeter dikonversi menjadi
Kilometer = {PKm} km
Hektometer = {PHm} hm
Dekameter = {PDam} dam
Meter = {PM} m
Centimeter = {PCm} cm
Milimeter = {PMm} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '6':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN CENTIMETER')
      
      PCm = float(input('Inputkan nilai panjang dalam satuan centimeter : '))
      
      PKm = PCm/100000
      PHm = PCm/10000
      PDam = PCm/1000
      PM = PCm/100
      PDm = PCm/10
      PMm = PCm*10
      
      print()
      print(f"""Panjang dalam {PCm} centimeter dikonversi menjadi
Kilometer = {PKm} km
Hektometer = {PHm} hm
Dekameter = {PDam} dam
Meter = {PM} m
Desimeter = {PDm} dm
Milimeter = {PMm} mm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '7':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGKONVERSI NILAI PANJANG DALAM SATUAN MILIMETER')
      
      PMm = float(input('Inputkan nilai panjang dalam satuan milimeter : '))
      
      PKm = PMm/1000000
      PHm = PMm/100000
      PDam = PMm/10000
      PM = PMm/1000
      PDm = PMm/100
      PCm = PMm/10
      
      print()
      print(f"""Panjang dalam {PMm} milimeter dikonversi menjadi
Kilometer = {PKm} km
Hektometer = {PHm} hm
Dekameter = {PDam} dam
Meter = {PM} m
Desimeter = {PDm} dm
Centimeter = {PCm} cm""")
      print()
      ulang = input('Apakah Anda ingin menggunakan konversi ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '0':
    system(clr.d)
    break

      
      





    
