"""
Python - Slicing Strings

Slicing / mengiris
Anda dapat mengembalikan rentang karakter dengan menggunakan sintaks slice.
Tentukan indeks awal dan indeks akhir, dipisahkan dengan tanda titik dua, untuk mengembalikan bagian dari string.
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Example
# Get the characters from position 2 to position 5 (not included):
x = "Hello, World"
print(x[2:5]) # akan menampilkan "llo"

# Catatan: Karakter pertama memiliki indeks 0.



# Slice From the Start
# Dengan mengabaikan indeks awal, rentang akan dimulai dari karakter pertama:
print(x[:5])


# Slice To the End
# Dengan mengabaikan indeks akhir, kisaran akan menuju ke ujung:
print(x[2:])


# Negative Indexing
# Gunakan indeks negatif untuk memulai irisan dari ujung string:
print(x[-5:-2])