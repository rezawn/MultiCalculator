#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sys import platform
from os import system
from data import clr

system(clr.d)

print(f"""PROGRAM INFORMATION
-------------------------------------------------------
Name        : Multi Calculator
Running OS  : {platform}
Version     : 1.0 [newest]
Released    : 3.6.20
Author      : Kelompok 4 Kelas A TI UNS 19 
Github      : https://github.com/rezawn/MultiCalculator
-------------------------------------------------------
THANKYOU FOR USING THIS PROGRAM
-------------------------------------------------------""")

print()
input('Tekan enter untuk keluar...')