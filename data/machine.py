#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT PROGRAM

from os import system
from data import clr

while True:
    system(clr.d)
    print("MULTI KALKULATOR")
    print("""-------------------------------------------------------
Silahkan pilih jenis kalkulator yang anda inginkan
1.  Kalkulator Numerik
2.  Kalkulator Konversi Suhu
3.  Kalkulator Konversi Waktu 
4.  Kalkulator Konversi Mata Uang
5.  Kalkulator Berat Badan Ideal
6.  Kalkulator Konversi Satuan Panjang 
7.  Kalkulator Konversi Satuan Berat 
8.  Kalkulator Konversi Satuan Luas
9.  Kalkulator Volume Bangun Ruang
10. Kalkulator Perhitungan Bunga Bank
11. Kalkulator Estimasi Biaya Listrik Bulanan
12. Informasi Program
0.  Keluar
-------------------------------------------------------""")

    jenis = input("Respon: ")
    
    if jenis == '1':
        while True:
            system(clr.d)
            from math import *
            
            print('KALKULATOR NUMERIK')
            print("""-------------------------------------------------------
PETUNJUK PENGGUNAAN
# Gunakan + untuk penjumlahan
# Gunakan - untuk pengurangan
# Gunakan * untuk perkalian
# Gunakan / untuk pembagian
# Gunakan ** untuk perpangkatan dan akar
# Gunakan *z untuk mengubah derajat ke radian
# Gunakan *y untuk mengubah radian ke derajat
# Pada trigonometri gunakan format sin(x) untuk x dalam radian
# Untuk nilai arc gunakan format asin(x) hasil dalam radian
# Gunakan penulisan tanda dalam kurung dengan benar

Contoh: 1+(1*(4**0.5))
-------------------------------------------------------""")
            z = pi/179.99999999999998
            y = 1/z
            
            h = input()
            i = str(h)
            j = eval(i)
        
            print()
            print('Hasil perhitungan adalah', j)
            print()
            
            ulang = input("Apakah anda ingin menggunakan kalkulator numerik lagi? (y/n) ")
            if ulang != 'y':
                system(clr.d)
                break
            
    elif jenis == '2':
        while True:
            system(clr.d)
            print('KALKULATOR KONVERSI SUHU')
            print("""-------------------------------------------------------
Pilih derajat suhu yang ingin anda konversi
1. Celcius
2. Reamur
3. Fahrenheit
4. Kelvin
0. Kembali ke menu awal
-------------------------------------------------------""")
            
            jenis = input('Respon: ')
            
            if jenis == '1':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI SUHU DARI DERAJAT CELCIUS')
                    print('-------------------------------------------------------')
                    C = float(input('Inputkan suhu dalam celcius: '))
                
                    R = (4/5)*C
                    F = ((9/5)*C)+32
                    K = C+273
                
                    print()
                    print(f"""Suhu dalam {C} derajat celcius dikonversi menjadi
Reamur     : {R} derajat reamur
Fahrenheit : {F} derajat fahrenheit
Kelvin     : {K} kelvin""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
                
            elif jenis == '2':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI SUHU DARI DERAJAT REAMUR')
                    print('-------------------------------------------------------')
                    R = float(input('Inputkan suhu dalam reamur: '))
                    
                    C = (5/4)*R
                    F = ((9/4)*R)+32
                    K = ((5/4)*R)+273
                    
                    print()
                    print(f"""Suhu dalam {R} derajat reamur dikonversi menjadi
Celcius    : {C} derajat celcius
Fahrenheit : {F} derajat fahrenheit
Kelvin     : {K} kelvin""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '3':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI SUHU DARI DERAJAT FAHRENHEIT')
                    print('-------------------------------------------------------')
                    F = float(input('Inputkan suhu dalam fahrenheit: '))
                    
                    C = ((5/9)*(F-32))
                    R = ((4/9)*(F-32))
                    K = (((5/9)*(F-32))+273)
                    
                    print()
                    print(f"""Suhu dalam {F} derajat fahrenheit dikonversi menjadi
Celcius    : {C} derajat celcius
Reamur     : {R} derajat reamur
Kelvin     : {K} kelvin""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '4':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI SUHU DARI KELVIN')
                    print('-------------------------------------------------------')
                    K = float(input('Inputkan suhu dalam kelvin: '))
                    
                    C = K-273
                    R = (K-273)*4/5
                    F = ((K-273)*(9/5))+32
                    
                    print()
                    print(f"""Suhu dalam {K} kelvin dikonversi menjadi
Celcius    : {C} derajat celcius
Reamur     : {R} derajat reamur
Fahrenheit : {F} derajat fahrenheit""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
        
            elif jenis == '0':
                system(clr.d)
                break
            
    elif jenis == '3':
        while True:
            system(clr.d)
            print('KALKULATOR KONVERSI WAKTU')
            print('''-------------------------------------------------------
Pilih satuan waktu yang akan anda konversi
1. Detik
2. Menit
3. Jam
4. Hari
0. Kembali ke menu awal
-------------------------------------------------------''')

            jenis = input('Respon: ')
    
            if jenis == '1':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI WAKTU DARI DETIK')
                    print('-------------------------------------------------------')
                    S = float(input('Inputkan waktu dalam detik: '))
                    M = S/60
                    J = M/60
                    H = J/24
            
                    print()
                    print(f'''Waktu dalam {S} detik dikonversi menjadi
Menit  : {M} menit
Jam    : {J} jam
Hari   : {H} hari''')
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
                    if ulang != 'y':
                        break

            elif jenis == '2':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI WAKTU DARI MENIT')
                    print('-------------------------------------------------------')
                    M = float(input('Inputkan waktu dalam menit: '))
                    S = M*60
                    J = M/60
                    H = J/24
            
                    print()
                    print(f'''Waktu dalam {M} menit dikonversi menjadi
Detik  : {S} Detik
Jam    : {J} jam
Hari   : {H} hari''')
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
                    if ulang != 'y':
                        break
     
            elif jenis == '3':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI WAKTU DARI JAM')
                    print('-------------------------------------------------------')
                    J = float(input('Inputkan waktu dalam jam: '))
                    S = J*3600
                    M = J*60
                    H = J/24
            
                    print()
                    print(f'''Waktu dalam {J} jam dikonversi menjadi
Detik  : {S} Detik
Menit  : {M} menit
Hari   : {H} hari''')
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
                    if ulang != 'y':
                        break
    
            elif jenis == '4':
                while True:
                    system(clr.d)
                    print('MENGKONVERSI WAKTU DARI HARI')
                    print('-------------------------------------------------------')
                    H = float(input('Inputkan waktu dalam hari: '))
                    J = H*24
                    M = J*60
                    S = M*60
            
                    print()
                    print(f'''Waktu dalam {H} hari dikonversi menjadi
Detik  : {S} Detik
Menit  : {M} menit
Jam    : {J} jam''')
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
                    if ulang != 'y':
                        break
    
            elif jenis == '0':
                system(clr.d)
                break    
    
    elif jenis == '4':
        while True:
            system(clr.d)   
            print('KALKULATOR KONVERSI MATA UANG')
            print('-------------------------------------------------------')
            print('''Pilih metode konversi di bawah ini
1. Offline
2. Online
0. Kembali ke menu awal
-------------------------------------------------------\n''')
            met = input('Respon: ')
    
            if met == '1':
                system(clr.d)
                print('KALKULATOR KONVERSI MATA UANG')
                print('-------------------------------------------------------')
    
                kurs = {}
    
                uanga = input('Inputkan jenis mata uang pertama: ')
                uangb = input('Inputkan jenis mata uang kedua: ')

                kurs['first'] = uanga
                kurs['second'] = uangb

                system(clr.d)
                print('KALKULATOR KONVERSI MATA UANG')
                print('-------------------------------------------------------')
                print('''PETUNJUK
Untuk nilai kurs dari mata uang yang lebih kecil
dianjurkan untuk menggunakan pecahan.

misal, nilai kurs rupiah ke dollar: 1/10000
-------------------------------------------------------''')

                print()
                nilai = input(f"Inputkan nilai kurs {kurs['first']} ke {kurs['second']}: ")
                hit = eval(nilai)

                kurs['exchange'] = hit

                print() 
                input('Tekan enter untuk melanjutkan...')
    
                while True:
                    system(clr.d)
                    print('KALKULATOR KONVERSI MATA UANG')
                    print('-------------------------------------------------------')
                    print(f'''Jenis konversi mata uang yang telah diinputkan
1. Konversi {kurs['first']} ke {kurs['second']}
2. Konversi {kurs['second']} ke {kurs['first']}
-------------------------------------------------------''')

                    pilih = input('Pilih jenis konversi mata uang: ')
    
                    if pilih == '1':
                        system(clr.d)
                        print('KALKULATOR KONVERSI MATA UANG')
                        print('-------------------------------------------------------')
        
                        a = float(input(f"Inputkan jumlah uang dalam {kurs['first']}: "))
                        b = a*kurs['exchange']
        
                        print()
                        print(f"Uang senilai {a} {kurs['first']} setara dengan {b} {kurs['second']}")
            
                        print()
                        ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
                        if ulang != 'y':
                            system(clr.d)
                            break
        
                    elif pilih == '2':
                        system(clr.d)
                        print('KALKULATOR KONVERSI MATA UANG')
                        print('-------------------------------------------------------')
        
                        c = float(input(f"Inputkan jumlah uang dalam {kurs['second']}: "))
                        d = c*(1/kurs['exchange'])
        
                        print()
                        print(f"Uang senilai {c} {kurs['second']} setara dengan {d} {kurs['first']}")
         
                        print()
                        ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n)')
                        if ulang != 'y':
                            system(clr.d)
                            break
    
            elif met == '2':
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
0. Kembali
-------------------------------------------------------\n''')

                    jenis = int(input('Respon: '))

                    if 9 > jenis >= 1:
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
        
                    break
    
            elif met == '0':
                break
    
    elif jenis == '5':
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
0. Kembali ke menu awal
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
                    UA = float(input('Usia Anak dalam Satuan Tahun : '))
      
                    Bbi_anak=(2*UA)+8
      
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
      
                    BMin = (90/100)*Bbi_pria
                    BMax = (120/100)*Bbi_pria
      
                    BBA = float(input('Berat Badan saat ini dalam Kg : '))
      
                    if BBA<=(90/100)*Bbi_pria:
                        print("Berat Badan Anda saat ini adalah Kurang")
       
                    elif (90/100)*Bbi_pria<BBA<=(110/100)*Bbi_pria:
                        print("Berat Badan Anda saat ini adalah Normal")

                    elif (110/100)*Bbi_pria<BBA<=(120/100)*Bbi_pria:
                        print("Berat Badan Anda saat ini adalah Berlebih")
          
                    elif BBA>(120/100)*Bbi_pria:
                        print("Badan Anda saat ini adalah Gemuk")
      
                    print("Batas minimum Berat Badan Anda dalam satuan Kg adalah : ",BMin)
                    print("Batas maksimum Berat Badan Anda dalam satuan Kg adalah : ",BMax)
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
      
                    BMin = (90/100)*Bbi_wanita
                    BMax = (120/100)*Bbi_wanita
      
                    BBA = float(input('Berat Badan saat ini dalam Kg : '))
      
                    if BBA<=(90/100)*Bbi_wanita:
                        print("Berat Badan Anda saat ini adalah Kurang")
          
                    elif (90/100)*Bbi_wanita<BBA<=(110/100)*Bbi_wanita:
                        print("Berat Badan Anda saat ini adalah Normal")
          
                    elif (110/100)*Bbi_wanita<BBA<=(120/100)*Bbi_wanita:
                        print("Berat Badan Anda saat ini adalah Berlebih")
          
                    elif BBA>(120/100)*Bbi_wanita:
                        print("Badan Anda saat ini adalah Gemuk")
          
                    print("Batas minimum Berat Badan Anda dalam satuan Kg adalah : ",BMin)
                    print("Batas maksimum Berat Badan Anda dalam satuan Kg adalah : ",BMax)
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
    
    elif jenis == '6':
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
0. Kembali ke menu awal
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
            
    elif jenis == '7':
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
  0. Kembali ke menu awal
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
            
    elif jenis == '8':
        iterasi = True
        while iterasi:
            system(clr.d)
            print('KALKULATOR KONVERSI SATUAN LUAS')
            print("""-------------------------------------------------------
Pilih satuan luas yang akan dikonversi
1. Kilometer persegi
2. Hektometer persegi (Hektar)
3. Dekameter persegi (Are)
4. Meter persegi
5. Desimeter persegi 
6. Centimeter persegi
7. Milimeter persegi
0. Kembali ke menu awal
-------------------------------------------------------""")
    
            jenis = input('Satuan yang akan dikonversi: ')
    
            if jenis == '1':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN KILOMETER PERSEGI')
            
                    LKm = float(input('Inputkan nilai luas dalam satuan kilometer persegi : '))
            
                    LHm = LKm*10**2
                    LDam = LKm*10**4
                    LM = LKm*10**6
                    LDm = LKm*10**8
                    LCm = LKm*10**10
                    LMm = LKm*10**12
            
                    print()
                    print(f"""Luas dalam {LKm} kilometer persegi dikonversi menjadi
1. Hektometer persegi (Hektare) = {LHm} hm persegi
2. Dekameter persegi (Are) = {LDam} dam persegi
3. Meter persegi = {LM} m persegi
4. Desimeter persegi = {LDm} dm persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '2':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN HEKTOMETER PERSEGI ATAU HEKTAR')
            
                    LHm = float(input('Inputkan nilai luas dalam satuan hektometer persegi (hektar) : '))
            
                    LKm = LHm/10**2
                    LDam = LHm*10**2
                    LM = LHm*10**4
                    LDm = LHm*10**6
                    LCm = LHm*10**8
                    LMm = LHm*10**10
            
                    print()
                    print(f"""Luas dalam {LHm} hektometer persegi (hektar) dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi    
2. Dekameter persegi (Are) = {LDam} dam persegi
3. Meter persegi = {LM} m persegi
4. Desimeter persegi = {LDm} dm persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '3':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN DEKAMETER PERSEGI ATAU ARE')
            
                    LDam = float(input('Inputkan nilai luas dalam satuan dekameter (are) persegi : '))
            
                    LKm = LDam/10**4
                    LHm = LDam/10**2
                    LM = LDam*10**2
                    LDm = LDam*10**4
                    LCm = LDam*10**6
                    LMm = LDam*10**8
            
                    print()
                    print(f"""Luas dalam {LDam} dekameter persegi (are) dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Meter persegi = {LM} m persegi
4. Desimeter persegi = {LDm} dm persegi          
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '4':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN METER PERSEGI')
            
                    LM = float(input('Inputkan nilai luas dalam satuan meter persegi : '))
            
                    LKm = LM/10**6
                    LHm = LM/10**4
                    LDam = LM/10**2
                    LDm = LM*10**2
                    LCm = LM*10**4
                    LMm = LM*10**6
            
                    print()
                    print(f"""Luas dalam {LM} meter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Desimeter persegi = {LDm} dm persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '5':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN DESIMETER PERSEGI')
            
                    LDm = float(input('Inputkan nilai luas dalam satuan desimeter persegi : '))
            
                    LKm = LDm/10**8
                    LHm = LDm/10**6
                    LDam = LDm/10**4
                    LM = LDm/10**2
                    LCm = LDm*10**2
                    LMm = LDm*10**4
            
                    print()
                    print(f"""Luas dalam {LDm} desimeter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Meter persegi = {LM} m persegi
5. Centimeter persegi = {LCm} cm persegi
6. Milimeter persegi = {LMm} mm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '6':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN CENTIMETER PERSEGI')
            
                    LCm = float(input('Inputkan nilai luas dalam satuan centimeter persegi : '))
            
                    LKm = LCm/10**10
                    LHm = LCm/10**8
                    LDam = LCm/10**6
                    LM = LCm/10**4
                    LDm = LCm/10**2
                    LMm = LCm*10**2
            
                    print()
                    print(f"""Luas dalam {LCm} centimeter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Meter persegi = {LM} m persegi
5. Desimeter persegi = {LDm} dm persegi
6. Milimeter persegi = {LMm} mm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '7':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    print('MENGKONVERSI NILAI LUAS DALAM SATUAN MILIMETER PERSEGI')
            
                    LMm = float(input('Inputkan nilai luas dalam satuan milimeter persegi : '))
            
                    LKm = LMm/10**12
                    LHm = LMm/10**10
                    LDam = LMm/10**8
                    LM = LMm/10**6
                    LDm = LMm/10**4
                    LCm = LMm/10**2
            
                    print()
                    print(f"""Luas dalam {LMm} milimeter persegi dikonversi menjadi
1. Kilometer persegi = {LKm} km persegi
2. Hektometer persegi (hektar) = {LHm} hm persegi
3. Dekameter persegi (are) = {LDam} dam persegi
4. Meter persegi = {LM} m persegi
5. Desimeter persegi = {LDm} dm persegi
6. Centimeter persegi = {LCm} cm persegi""")
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
            
            elif jenis == '0':
                system(clr.d)
                break
    
    elif jenis == '9':
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
0. Kembali ke menu awal
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
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
                    ulang = input('Apakah anda ingin menggunakan perhitungan ini lagi? (y/n) ')
                    if ulang != 'y':
                        break

            elif jenis == '0':
                system(clr.d)
                break
    
    elif jenis == '10':
        def BungaSederhana(awal, sukuBunga, waktu):
            nilaiakhir = awal + (awal * (sukuBunga / 100)) * (waktu / 12)
            return nilaiakhir

        def BungaMajemuk(awal, sukuBunga, waktu):
            nilaiakhir = awal * (pow((1 + sukuBunga / 100), (waktu / 12)))
            return nilaiakhir

        iterasi = True
        while iterasi:
            system(clr.d)
            print('KALKULATOR PERHITUNGAN BUNGA BANK')
            print("""-------------------------------------------------------
Pilih Jenis Bunga Bank yang Ingin Dihitung
1. Bunga Sederhana
2. Bunga Majemuk
0. Kembali ke menu awal
-------------------------------------------------------""")
    
            jawab = input('Respon: ')
            if jawab == '0':
                system(clr.d)
                break
    
            elif jawab == '1':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    awal = float(input("Masukkan Nilai Awal: "))
                    sukuBunga = float(input("Masukkan Persentase Suku Bunga: "))
                    waktu = float(input("Berapa lama periodenya (dalam bulan)? "))
                    nilaiakhir = BungaSederhana(awal, sukuBunga, waktu)
                    print(f"Maka Nilai Akhir yang akan diperoleh dalam periode {waktu} bulan adalah ", nilaiakhir)
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break

            elif jawab == '2':
                iterasi = True
                while iterasi:
                    system(clr.d)
                    awal = float(input("Masukkan Nilai Awal: "))
                    sukuBunga = float(input("Masukkan Persentase Suku Bunga: "))
                    waktu = float(input("Berapa lama periodenya (dalam bulan)? "))
                    nilaiakhir = BungaMajemuk(awal, sukuBunga, waktu)
                    print(f"Maka Nilai Akhir yang akan diperoleh dalam periode {waktu} bulan adalah ", nilaiakhir)
                    print()
                    ulang = input('Apakah anda ingin menggunakan konversi ini lagi? (y/n) ')
                    if ulang != 'y':
                        break
    
    elif jenis == '11':
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
    
    elif jenis == '12':
        from sys import platform
        system(clr.d)

        print(f"""PROGRAM INFORMATION
-------------------------------------------------------
Name        : Multi Calculator
Running OS  : {platform}
Version     : 2.0 [newest]
Released    : 8.6.20
Author      : Kelompok 4 Kelas A TI UNS 19 
Github      : https://github.com/rezawn/MultiCalculator
-------------------------------------------------------
THANKYOU FOR USING THIS PROGRAM
-------------------------------------------------------""")

        print()
        input('Tekan enter untuk kembali ke menu awal...')
    
    elif jenis == '0':
        system(clr.d)
        break
