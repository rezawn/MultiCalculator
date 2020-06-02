#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KALKULATOR BBI

from os import system
from data import clr

iterasi = True
while iterasi:
  system(clr.d)
  print('KALKULATOR BERAT BADAN IDEAL')
  print("""-------------------------------------------------------
Pilih kategori Anda
1. Bayi 0-12 bulan
2. Anak usia 1-10 tahun
3. Pria
4. Wanita
5. Ibu hamil
0. Keluar
-------------------------------------------------------""")
  
  jenis = input('Respon: ')
  
  if jenis == '1':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGHITUNG BERAT BADAN IDEAL')
      
      #usia dalam satuan bulan
      UB = float(input('Usia Bayi dalam Satuan Bulan : '))
      
      Bbi_bayi=(UB/2)+4
      
      print("Berat Badan Ideal (kg) : ",Bbi_bayi)
      ulang = input('Apakah Anda ingin menggunakan kategori ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '2':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGHITUNG BERAT BADAN IDEAL')
      
      #usia dalam satuan tahun
      UB = float(input('Usia Anak dalam Satuan Tahun : '))
      
      Bbi_anak=(2*UB)+8
      
      print("Berat Badan Ideal (kg) : ",Bbi_anak)
      ulang = input('Apakah Anda ingin menggunakan kategori ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '3':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGHITUNG BERAT BADAN IDEAL')
      
      #Tinggi badan dalam satuan cm
      TB = float(input('Tinggi Badan dalam Satuan Cm : '))
      
      Bbi_pria=(TB-100)-((TB-100)*(10/100))
      
      print("Berat Badan Ideal (kg) : ",Bbi_pria)
      ulang = input('Apakah anda ingin menggunakan kategori ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '4':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGHITUNG BERAT BADAN IDEAL')
      
      #Tinggi badam dalam satuan cm
      TB = float(input('Tinggi Badan dalam Satuan Cm : '))
      
      Bbi_wanita=(TB-100)-((TB-100)*(15/100))
      
      print("Berat Badan Ideal (kg) : ",Bbi_wanita)
      ulang = input('Apakah Anda ingin menggunakan kategori ini lagi? (y/n) ')
      if ulang != 'y':
        break
        
  elif jenis == '5':
    iterasi = True
    while iterasi:
      system(clr.d)
      print('MENGHITUNG BERAT BADAN IDEAL')
      
      BBI = float(input('Berat Badan Ideal Normal dalam Kg : '))
      #usia kehamilan dalam satuan minggu
      UK = float(input('Usia Kehamilan dalam Satuan Minggu : '))
     
      Bbi_wanita_hamil=BBI+(UK*0.35)
      
      if 0<UK<43:
        print("Berat Badan Ideal (Kg) : ",Bbi_wanita_hamil)
        ulang = input('Apakah Anda ingin menggunakan kategori ini lagi? (y/n) ')
        if ulang != 'y':
          break
        
      else:
        print("Usia Kehamilan Harus Berada Diantara 1-42 Minggu")
        ulang = input('Apakah Anda ingin menggunakan kategori ini lagi? (y/n) ')
        if ulang != 'y':
          break
          
  elif jenis == '0':
    system(clr.d)
    break
