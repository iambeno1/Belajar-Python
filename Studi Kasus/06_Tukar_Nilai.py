import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")

# Nilai awal
x = 5
y = 3

print("Sebelum ditukar")
print("x =", x)
print("y =", y)

# Tukar Nilai
z = x
x = y
y = z

print("Setelah ditukar")
print("x =", x)
print("y =", y)

