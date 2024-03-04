"""
Buatlah kode program dalam bahasa Python untuk menghitung luas persegi. Kode program butuh 1 inputan berupa panjang sisi persegi, kemudian tampilkan output luas persegi.

Luas persegi = sisi * sisi = sisi^2
"""

import os

# Bersihkan layar termiinal
os.system("cls" if os.name == "nt" else "clear")

print("=====MENGHITUNG LUAS PERSEGI=====")

panjang = float(input("Masukkan panjang: "))
luas = float(panjang * panjang)

print("Luas persegi = ", luas)

