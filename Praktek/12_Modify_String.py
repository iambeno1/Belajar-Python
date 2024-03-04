"""
MODIFY STRING
-------------
Python memiliki seperangkat metode bawaan yang dapat Anda gunakan pada string.

1. Upper Case / Huruf Besar -> upper()
2. Lower Case / Huruf Kecil -> lower()
3. Remove Whitespace / Menghapus Spasi -> strip()
4. Replace String -> replace(value)
5. Spilt String / Membagi String -> spilt("kode/simbol")

"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")


# UPPER CASE
x = "Hello World"
print("x =", x)
print("Upper x =", x.upper())

# LOWER CASE
x = "HELLO, WORLD"
print("x =", x)
print("Lower x =", x.lower())

# REMOVE WHITESPACE
x = "  Aku Cinta Python! "
print("x =", x)
print("Hapus Spasi x =", x.strip())

# REPLACE STRING
x = "Ony Gaby"
print("x =", x)
print("Replace x =", x.replace("Ony Gaby", "Benony Gabriel"))
print("Replace x =", x.replace("Ony", "Beno"))
print("Replace x =", x.replace("G", "R"))

# SPILT STRING
x = "Preorder"
print("x =", x)
print("Spilt x =", x.split("order"))
x = "Hi guys"
print("x =", x)
print("Spilt x =", x.split(" "))
x = "Kupu-kupu"
print("x =", x)
print("Spilt x =", x.split("-"))



