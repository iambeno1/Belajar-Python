"""
Slicing Strings

Anda dapat mengembalikan rentang karakter dengan menggunakan sintaks slice.
Tentukan indeks awal dan indeks akhir, dipisahkan dengan tanda titik dua, untuk mengembalikan bagian dari string.
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")



# Slicing String Example
a = "Python is fun"
print(a[2:6]) # Output: thon



# Note: Karakter pertama memiliki indeks 0.


# Slice From the Start
a = "Coding is my life"
print(a[:6]) # Output: Coding



# Slice to End
a = "Coding is my life"
print(a[0:]) 
print(a[7:]) 
print(a[:]) 


# Negative Indexing
a = "Coding is my life"
print(a[-7:-2])
