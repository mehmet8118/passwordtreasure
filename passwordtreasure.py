#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "D E R E L I "

import sys
import threading
import os
import requests
import socket
import random

alfabe = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
buyuk_alfabe = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
sayi = ["1","2","3","4","5","6","7","8","9"]
isaretler = ["!",".","-"]
sifre = []

for i in range(20):
    sifre.append(random.choice(alfabe))
    sifre.append(random.choice(buyuk_alfabe))
    sifre.append(random.choice(sayi))
    #sifre.append(random.choice(isaretler))




f = open("sifrelerim.txt","a")
for i in sifre:
    f.write(i)

deger = input("Sifre Bilgisi: ")
f.write("  "+"--"+deger+"   \n")
