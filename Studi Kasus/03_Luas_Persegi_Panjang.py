"""
Buatlah kode program dalam bahasa Python untuk menghitung luas persegi panjang. Kode program butuh 2 inputan berupa panjang dan lebar, kemudian menampilkan output luas persegi panjang.

Luas persegi panjang = panjang * lebar
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

print("======MENGHITUNG LUAS PERSEGI PANJANG======")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
luas = float(panjang * lebar)

print("Luas persegi panjang = ", luas)