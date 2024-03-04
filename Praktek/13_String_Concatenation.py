"""
String Concatenation
To concatenate, or combine, two strings you can use the + operator.
"""

import os

# Bersihkan layar terminal
os.system("cls" if os.name == "nt" else "clear")


# Menggabungkan variabel a dengan variabel b menjadi variabel c:
a = "Hello"
b = "Python"
c = a + b
print(c) # result: HelloPython

a = "Hello"
b = "Python"
c = a + " " + b
print(c) # result: Hello Python