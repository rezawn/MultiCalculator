#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT KONVERSI MATA UANG

from os import system
from data import clr

while True:
    system(clr.d)   
    print('KALKULATOR KONVERSI MATA UANG')
    print('-------------------------------------------------------')
    print('''Pilih metode konversi di bawah ini
1. Offline
2. Online
0. Keluar
-------------------------------------------------------\n''')
    met = input('Respon: ')
    
    if met == '1':
        from data import kursoff
        break
    elif met == '2':
        from data import kursonn
        break
    elif met == '0':
        break