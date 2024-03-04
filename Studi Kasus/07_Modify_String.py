import os

# Bersihkan layar
os.system("cls" if os.name == "nt" else "clear")

print("==========MODIFY STRING==========\n")
teks = str(input("Masukkan sebuah kalimat: "))

while True:
    print("Pilih opsi untuk edit")
    print("1. To Upper Case")
    print("2. To Lower Case")
    print("3. Replace")
    print("4. Exit")
    pilihan = int(input("Masukkan pilihan kamu: "))
    
    if pilihan == 1:
        print("Upper Case:", teks.upper())
    elif pilihan == 2:
        print("Lower Case:", teks.lower())
    elif pilihan == 3:
        ganti = str(input("Masukkan string yang mau diganti: "))
        if ganti in teks:
            string_baru = str(input("Masukkan string baru: "))
            print("Replace:", teks.replace(ganti, string_baru))
        else:
            print(ganti, "tidak ditemukan, coba lagi")
    elif pilihan == 4:
        print("Exit")
        break
    else:
        print("Pilihan tidak tersedia, coba lagi!")
        
    