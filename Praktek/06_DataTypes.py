"""
Tipe Data Python

Variabel dapat menyimpan data dengan tipe yang berbeda, dan tipe yang berbeda dapat melakukan hal yang berbeda.
Python memiliki tipe data bawaan yang secara default dalam kategori berikut:

Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
None Type       :	NoneType

"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Mengetahui tipe data dengan fungsi type()
x = 5
print("x = ", x)
print("Type of x =", type(x), "\n")

# Tipe data str (string)
x = "Aku cinta python"
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data int (integer)
x = 4
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data float
x = 4.5
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data complex
x = 5j
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data list 
x = ["merah", "putih", "biru", "kuning", "hijau"]
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data tuple
x = ("kisar", "ambon", "jawa")
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data range
x = range(6)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data dict
x = {"Nama" : "Beno", "Umur" : 19}
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data set
x = {"CS", "CE", "EE", "PE", "HI", "GL"}
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data frozenset
x = frozenset({"CS", "CE", "EE", "PE", "HI", "GL"})
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data bool (boolean)
x = True
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data bytes
x = b"Python"
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data bytearray
x = bytearray(6)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data memoryview
x = memoryview(bytes(6))
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data none
x = None
print("x =", x)
print("Type of x =", type(x), "\n")


# Mengatur tipe data spesifik
# Jika ingin membuat tipe data spesifik, dapat menggunakan fungsi konstruktor berikut:

# Tipe data str (string)
x = str("Aku cinta python")
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data int (integer)
x = int(4)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data float
x = float(4.5)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data complex
x = complex(5j)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data list 
x = list(["merah", "putih", "biru", "kuning", "hijau"])
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data tuple
x = tuple(("kisar", "ambon", "jawa"))
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data range
x = range(6)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data dict
x = dict({"Nama" : "Beno", "Umur" : 19})
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data set
x = set({"CS", "CE", "EE", "PE", "HI", "GL"})
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data frozenset
x = frozenset({"CS", "CE", "EE", "PE", "HI", "GL"})
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data bool (boolean)
x = bool(5)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data bytes
x = bytes(7)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data bytearray
x = bytearray(6)
print("x =", x)
print("Type of x =", type(x), "\n")

# Tipe data memoryview
x = memoryview(bytes(6))
print("x =", x)
print("Type of x =", type(x), "\n")