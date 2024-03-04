"""
Karakter Escape
Untuk menyisipkan karakter yang tidak diperbolehkan dalam string, gunakan karakter escape.

Karakter escape adalah garis miring \ yang diikuti dengan karakter yang ingin Anda sisipkan.

Contoh karakter ilegal adalah tanda kutip ganda di dalam string yang dikelilingi oleh tanda kutip ganda:

txt = "We are the so-called "Vikings" from the north."

Untuk memperbaiki masalah ini, gunakan karakter escape \":

Karakter escape memungkinkan Anda menggunakan tanda kutip ganda ketika Anda biasanya tidak diizinkan:
txt = "We are the so-called \"Vikings\" from the north."
"""


# Contoh tanda kutip tunggal dan ganda
txt = "We are the so-called \"Vikings\" from the north"
print(txt)
txt = "We are the so-called \'Vikings\' from the north"
print(txt)
txt = "it\'s alright"
print(txt)


# Contoh backslash `\`
txt = "Memasukan backslash \\ begini caranya"
print(txt)


# Newline
txt = "Hello \nWorld!"
print(txt)


# Carriage Return
txt = "Hello \rGuys!"
print(txt)


# Tab
txt = "Nama \t: Beno"
print(txt)



# Backspace
txt = "Nama\b: Beno"
print(txt)



# Form feed
txt = "Nama \f: Beno"
print(txt)



# Octal Value
txt = "\110\145\154\154\157"
print(txt)



# Hex Value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)