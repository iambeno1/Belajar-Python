"""
Casting dalam python adalah proses mengubah tipe data suatu nilai ke tipe data lain. Misalnya, mengubah string menjadi int atau float menjadi bool. Casting dilakukan dengan menggunakan fungsi konstruktor dari masing-masing tipe data, seperti int(), float(), str(), bool(), dll

Casting dalam python dilakukan dengan menggunakan fungsi-fungsi konstruktor:
  - int() - mengkonstruksi sebuah angka integer dari literal integer, literal float (dengan menghapus semua desimal), atau literal string (asalkan string tersebut mewakili bilangan bulat)
  - float() - membuat angka float dari literal bilangan bulat, literal float, atau literal string (asalkan string mewakili float atau bilangan bulat)
  - str() - membuat string dari berbagai macam tipe data, termasuk string, literal bilangan bulat, dan literal float
"""

import os

# Bersihkan layar terminal
# os.system("cls")
os.system("cls" if os.name == "nt" else "clear")


# INT
w = int(1)    # w will be 1
x = int(5.9)  # x will be 5
y = int("3")  # y will be 3
# z = int("3.2")  # kalo seperti ini akan mengalami error

# FLOAT
w = float(2)      # w will be 2.0
x = float(0.5)    # x will be 0.5
y = float("3")    # y will be 3.0
z = float("2.5")  # z will be 2.5

# STR
w = str(5)    # w will be "5"
x = str(2.4)  # x will be "2.4"
y = str("8")  # y will be "8"