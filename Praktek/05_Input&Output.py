import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Belajar Input
# Secara default jika variabel yang dimasukan value melalui input user adalah bertipe str (string) untuk itu kita bisa menggunakan cara agar menerima input sesuaai dengan yang kita mau, seperti contoh

nama = input("Masukkan nama kamu\t  : ")
tahun_lahir = int(input("Masukkan tahun lahir kamu : "))

print("Hai",nama,"! Selamat ya kamu sekarang berumur ",(2024 - tahun_lahir),"tahun\n")