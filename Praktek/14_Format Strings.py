"""
String Format

Metode format() mengambil argumen yang dilewatkan, memformatnya, dan menempatkannya di dalam string di mana placeholder {} berada:
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# contoh salah
"""
age = 19
txt = "Halo saya Beno dan saya berumur" + age
"""

# Solusi, lakukan format -> format()
age = 19
txt = "Halo saya Beno dan saya berumur {}"
print(txt.format(age))

# Contoh lain
name = "Beno"
age = 19
salary = 10
rank = 1

txt = "Halo saya " + name + " dan saya berumur {} tahun \nGaji saya {} dolar perhari dan saya diperingkat ke-{} siswa dengan gaji harian tertinggi"

print(txt.format(age, salary, rank))

# Bisa juga pakai index yang ditempatkan pada placeholder {index}
txt = "Halo saya " + name + " dan saya digaji {1} dolar perhari \nSaya berada di posisi ke {2} siswa dengan gaji harian tertinggi, padahal saya baru beruasia {0} tahun"

print(txt.format(age, salary, rank))

# conto lain
harga_item = 10
no_item = 18
stok_item = 70
kuantitas = 3

my_order = """
            Order Anda
            No item     : {1}
            Qty         : {2}
            Harga       : {0}
            -----------------
            Sisa stok   : {4}
            -----------------
            Total bayar : {3}
            """

print(my_order.format(harga_item, no_item, kuantitas, (kuantitas * harga_item), (stok_item - kuantitas)))


