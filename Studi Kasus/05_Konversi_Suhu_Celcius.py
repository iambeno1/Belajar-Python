"""
Buatlah kode program Python konversi suhu. Program meminta 1 inputan berupa suhu dalam satuan derajat cescius. Hasilnya akan menampilkan konversi suhu untuk derajat Fahrenheit, Kelvin dan Reamur.

Rumus:
Fahrenheit = (9/5) * Celcius + 32
Kelvin = Celcius + 273.15
Reamur = (4/5) * Celcius
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

print("==========KONVERSI SUHU CELCIUS==========\n")

celcius = float(input("Masukkan suhu Celcius: "))

fahranheit = float((9/5 * celcius) + 32)
kelvin = float(celcius + 273.15)
reamur = float(4/5 * celcius)

print(celcius, "derajat Celcius =", fahranheit, "derajat Fahrenheit")
print(celcius, "derajat Celcius =", kelvin, "derajat Kelvin")
print(celcius, "derajat Celcius =", reamur, "derajat Reamur")