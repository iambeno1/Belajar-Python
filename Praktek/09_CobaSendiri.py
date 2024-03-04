import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Biodata
nama = input("Mahukkan nama kamu: ")
umur = input("Masukkan umur kamu: ") # Secara default ini akan menerima input berupa str walaupun kita memasukan int
print(type(umur))
print("Hai", nama, "! kamu sekarang berumur", umur)

# Jika ingin menerima input yang lebih spesifik bisa gunakan casting, berikut contohnya:
nama = str(input("Masukkan nama kamu: "))
tahun_lahir = int(input("Masukkan tahun lahir: "))
print("Hai", nama, "kamu sekarang berumur", (2024-tahun_lahir), "tahun")

# Ya benar, kelebihannya kita bisa melakukan oprasi arimatika jika variabelnya kita casting menjadi lebih spesifik sesuai kebutuhan