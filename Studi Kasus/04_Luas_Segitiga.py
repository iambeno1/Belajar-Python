"""
Buatlah kode program dalam bahasa Python untuk menghitung luas segitiga. Kode program butuh 2 inputan berupa alas dan tinggi segitiga, kemudian menampilkan output luas segitiga.

Luas segitiga = 1/2 * alas * tinggi
"""

import os

# Bersihkan layar
os.system("cls" if os.name == "nt" else "clear")

print("=======MENGHITUNG LUAS SEGITIGA=======")
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkann tinggi: "))
luas = (0.5 * alas * tinggi)

print("Luas segitiga = ", luas)