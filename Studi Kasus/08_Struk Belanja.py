import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

produk = str("""
             Produk kami
             1. Coca-cola : Rp 8.000
             2. Fanta     : Rp 5.000
             """)

item_produk = ["Coca-cola", "Fanta"]
harga_produk = [8000, 5000]

struk_belanja = str("""
                  +----------------------------+
                  |        Order anda          |
                  |----------------------------|
                  | Nama item     : {0}        |
                  | Harga satuan  : {1}        |
                  | Kuantitas     : {2}        |
                  |----------------------------|
                  | Total tagihan : {3}        |
                  +----------------------------+
                  """)

while True:
    print("----- WELCOME -----")
    print("1. Lihat produk")
    print("2. Beli")
    print("0. Exit")
    pilihan = int(input("Masukkan pilihan: "))
    
    if pilihan == 1:
        os.system("cls")
        print(produk)
        os.system("pause")
    elif pilihan == 2:
        print(produk)
        no_produk = int(input("Masukkan nomor produk: "))
        qty = int(input("Masukkan jumlah beli: "))
        
        if no_produk == 1:
            print(struk_belanja.format(item_produk[0], harga_produk[0], qty, (qty * harga_produk[0])))
            break
        elif no_produk == 2:
            print(struk_belanja.format(item_produk[1], harga_produk[1], qty, (qty * harga_produk[1])))
            break
        else:
            print("Pilihan tidak tersedia, coba lagi!")
    elif pilihan == 0:
        break
    else:
        print("Pilihan tidak tersedia, coba lagi!")
            