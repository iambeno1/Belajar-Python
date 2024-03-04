"""
String
String dalam python dikelilingi oleh tanda kutip tunggal, atau tanda kutip ganda.

'hello' sama dengan "halo".
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

print("Aku cinta Python -> kutip dua")
print('Aku cinta Python -> kutip satu')


# Assign String to a Variable
name = "Beno"
print("Name : " + name)


# Multiline string (bisa pake kutip dua maupun kutip satu)
text = """Belajar Python
    1. Ony jago koding
    2. Ony ahli koding
    3. Ony sukses
    4. Ony bijak
    5. Ony kaya
    Itulah Ony di masa depan
    """

print("Text : ", text)
# Catatan: pada hasilnya, jeda baris disisipkan pada posisi yang sama seperti dalam kode.


# String adalah Array
"""
Seperti banyak bahasa pemrograman populer lainnya, string dalam Python adalah array byte yang merepresentasikan karakter unicode.

Namun, Python tidak memiliki tipe data karakter, satu karakter hanyalah sebuah string dengan panjang 1.

Tanda kurung siku dapat digunakan untuk mengakses elemen-elemen string.
"""

name = "Benony Gabriel"
print("Name : " + name)
# Dapatkan karakter pada posisi 1 (ingat bahwa karakter pertama memiliki posisi 0):
print("Karakter ke-2 dari", name, "adalah", name[1])


# Perulangan melalui string
# Karena string adalah array, kita dapat mengulang karakter dalam string, dengan perulangan for.

for x in "Banana":
    print(x)


# String length
# Untuk mendapatkan panjang sebuah string, gunakan fungsi len().

country = "Indonesia"
print("Country :", country)
print("Panjang", country, "=", len(country))


# Check String
# Untuk memeriksa apakah frasa atau karakter tertentu ada dalam sebuah string, kita dapat menggunakan kata kunci 'in'.

text = "Aku cinta python"
print("Aku" in text) # true
print("kamu" in text) # false

# gunakan statement if untuk memeriksa
if "Aku" in text:
    print("Yes ada")
else:
    print("No, tak ada")


# Bagaimana kalo kita buat input dari user
print("====Search====")
print("Text: ", text)
cari = str(input("Masukan kata/char yang ingin dicari dari text: "))

if cari in text:
    print("Yes,", cari, "ditemukan")
else:
    print("Sorry,", cari, "tidak ditemukan")


# Check if NOT
# Untuk memeriksa apakah frasa atau karakter tertentu TIDAK ada dalam sebuah string, kita dapat menggunakan kata kunci not in.

print("====Not Search====")
print("Text: ", text)
cari = str(input("Masukan kata/char yang not ingin dicari dari text: "))

if cari not in text:
    print("Sorry,", cari, "tidak ditemukan")
else:
    print("Yes,", cari, "ditemukan")
