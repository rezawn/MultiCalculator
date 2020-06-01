#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#SCRIPT UTAMA

from sys import platform
from os import system
from data import clr

system(clr.d)

print('SELAMAT DATANG DI MULTI CALCULATOR')

print(f'''-------------------------------------------------------
You are using "{platform}" operation system. 
This program will run correctly only in Windows and 
Linux operation system.
-------------------------------------------------------
     
      ''')


input('Tekan enter untuk melanjutkan...')

from data import machine
