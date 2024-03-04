"""
Python Numbers

Ada tiga jenis angka dalam Python:
  - int
  - float
  - kompleks
  
Variabel bertipe numerik dibuat saat Anda menetapkan nilai padanya
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Numbers in Python

# int
# Int, atau bilangan bulat, adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tidak terbatas.
a = 12  
b = -87
c = 0
d = 345834576578164587876
print("a =", a, "\nType of a =",type(a))
print("b =", b, "\nType of b =",type(b))
print("c =", c, "\nType of c =",type(c))
print("d =", d, "\nType of d =",type(d), "\n\n")

# float
# Float adalah angka, positif atau negatif, yang mengandung satu atau lebih desimal(dengan simbol `.` sebagai koma).
a = 12.34  
b = -0.87
c = 0.009
d = -1.25
print("a =", a, "\nType of a =",type(a))
print("b =", b, "\nType of b =",type(b))
print("c =", c, "\nType of c =",type(c))
print("d =", d, "\nType of d =",type(d), "\n\n")

# Float juga bisa berupa angka ilmiah dengan "e" untuk menunjukkan pangkat 10.
a = 12e4  
b = 78E2
c = -1.25e100
print("a =", a, "\nType of a =",type(a))
print("b =", b, "\nType of b =",type(b))
print("c =", c, "\nType of c =",type(c), "\n\n")

# complex
# Bilangan kompleks ditulis dengan "j" sebagai bagian imajiner
a = 3j  
b = 5+2j
c = 0.009j
d = -8j
print("a =", a, "\nType of a =",type(a))
print("b =", b, "\nType of b =",type(b))
print("c =", c, "\nType of c =",type(c))
print("d =", d, "\nType of d =",type(d), "\n\n")

# Jensi konversi
# Anda dapat mengonversi dari satu tipe ke tipe lainnya dengan metode int(), float(), dan complex()
a = 3
b = 5.2
c = 8j
print("a =", a, "\nType of a =",type(a))
print("b =", b, "\nType of b =",type(b))
print("c =", c, "\nType of c =",type(c), "\n\n")

# Konversi int to float
x = float(a)
print("x =", x, "\nType of x =",type(x))

# Konversi float to int
y = int(b)
print("y =", y, "\nType of y =",type(y))

# Konversi complex to int
z = complex(a)
print("z =", z, "\nType of z =",type(z))


# Random number
# Python tidak memiliki fungsi random() untuk membuat angka acak, tetapi Python memiliki modul bawaan bernama random yang dapat digunakan untuk membuat angka acak

import random

print(random.randrange(1, 10))
