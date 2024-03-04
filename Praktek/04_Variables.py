"""
Python tidak memiliki perintah untuk mendeklarasikan variabel.
Sebuah variabel dibuat pada saat Anda pertama kali memberikan nilai padanya.
Bahsa python adalah case sensitif sama seperti C++
"""

# 1. Membuat variabel

x = 12 #ini adalah variabel
print("x = ", x)

a = "Aku cinta python"
print("a : ", a)

nama = "Beno Gabriel"
umur = 19
print("Nama \t:", nama)
print("Umur \t:", umur)

nama = "Benony Gabriel" #variabel nama sekarang bernilai `Benony Gabriel`
print("Nama \t:", nama)

angka = 12
print("angka\t: ", angka)

angka = 5
print("angka\t: ", angka)

# 2. Casting variabel

# Jika Anda ingin menentukan tipe data dari sebuah variabel, hal ini dapat dilakukan dengan casting.

a = str("Hello world") #bertipe string (str)
print("a = ", a)

a = int(4) #bertipe integer (int)
print("a = ", a)
print("a + a = ", a + a)

a = str(4) #bertipe string (str)
print("a + a = ", a + a)

a = float(4) #bertipe desimal (float)
print("a = ", a)

# 3. Get the Type

# Anda bisa mendapatkan tipe data dari sebuah variabel dengan fungsi type().
a = 3
b = 2.5
c = "Hello"
print("a = ", a, "\nb = ", b, "\nc = ", c)

print("Type of a = ", type(a))
print("Type of b = ", type(b))
print("Type of c = ", type(c))

# Tanda Kutip Tunggal atau Ganda?

# Variabel string dapat dideklarasikan dengan menggunakan tanda kutip tunggal atau ganda:

ingat = "Python is fun"
print("ingat = ", ingat)

ingat = 'Python is fun'
print("ingat = ", ingat)

# 4. Case sensitif

a = 2
A = 7

print("a = ", a, "\nA = ", A)
print("a != A")
print(a, " != ", A)

# Penamaan variabel
a = 3
A = 4
myVar = "Hello"
MyVar = "World"
my_var = "Dunia"

print(a, A, myVar, MyVar, my_var)

# Assign muultiple value

# 1. Many value to multiple variabel
x, y, z = "Orange", 3.5, 2
print("x = ", x)
print("y = ", y)
print("z = ", z)

print("Type of x =", type(x))
print("Type of y =", type(y))
print("Type of z =", type(z))

# 2. One value to multiple variabel
x = y = z = "Apple"
print("x = ", x)
print("y = ", y)
print("z = ", z)

# 3. Unpack a collection
fruits = ["Mangga", "Jeruk", "Apel"]
x, y, z = fruits
print("\nx = ", x)
print("y = ", y)
print("z = ", z)

data = ["Beno", 19, "Ilmu Komputer"]
x, y, z = data
print("\nx = ", x)
print("y = ", y)
print("z = ", z)

x = data
print("\nx =", data)

x  = "Python "
print(x)
print(x * 5)
print(x, "is fun")

y = "C++ "
print(y)
print(y * 5)

print(x, "vs", y)
print(x + y)

z = 3
print("z = ", z)
print("z * 2 = ", z * 2)
print("z = ", z + 2 * 3)

print(x * z)

# Global variabel
"""
Variabel yang dibuat di luar fungsi (seperti pada semua contoh di atas) dikenal sebagai variabel global.

Variabel global dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar fungsi.
"""

# Buat variabel global
x = "Python"

# Buat fungsi
def myfunc():
  print(x + " is fun")

myfunc() # panggil fungsi

def test():
  x = "C++"
  print("x = ", x)

test()

print(x, "is fun")

# Global keyword
"""
Biasanya, ketika Anda membuat variabel di dalam sebuah fungsi, variabel tersebut bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut.

Untuk membuat variabel global di dalam fungsi, Anda dapat menggunakan kata kunci global.
"""

def myfunc2():
  global x
  x = "Rubby"
  print("x = ", x)

myfunc2()

print("x = ", x)