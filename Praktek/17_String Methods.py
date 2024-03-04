"""
Metode String
Python memiliki sekumpulan metode bawaan yang dapat Anda gunakan pada string.

Note: Semua metode string mengembalikan nilai baru. Metode-metode ini tidak mengubah string asli.
"""

# capitalize()
txt = "hello bro"
print(txt.capitalize())	    # Mengubah karakter pertama menjadi huruf besar


# casefold()
txt = "HELLO BRO"
print(txt.casefold())	    # Mengonversi string menjadi huruf kecil


# center()
txt = "text tengah"
print(txt.center(20))       # Untuk mengatur string ke tengah


# count()	            Mengembalikan berapa kali nilai tertentu muncul dalam string
"""
Syntax count() 

string.count(value, start, end)

value : Wajib diisi. String. String yang akan dicari nilainya
start : Opsional. Bilangan bulat. Posisi untuk memulai pencarian. Nilai default adalah 0
end   : Opsional. Bilangan bulat. Posisi untuk mengakhiri pencarian. Defaultnya adalah akhir dari string

"""
txt = "Saya suka apel, apel adalah buah favorit saya."
print(txt.count("apel")) # Output: 2 -> terdapat dua buah kata apel dlm txt
print(txt.count("apel", 12, 24)) # Output: 1 -> terdapat satu kata apel pada range 12 - 24 dlm txt
print(txt.count("apel", 12)) # Output: 1 -> terdapat satu kata apel pada range 12 - akhir dlm txt


# encode()	        Returns an encoded version of the string


# endswith()	        Returns true if the string ends with the specified value
txt = "aku cinta Python!"
print(txt.endswith("cinta"))
print(txt.endswith("Python!"))
print(txt.endswith("!"))

# expandtabs()	    Sets the tab size of the string
txt = "H\te\tl\tl\to\t \tW\to\tr\tl\td"
print(txt.expandtabs(0))
print(txt.expandtabs(-5))
print(txt.expandtabs(2))

# find()	            Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	            Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	        Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	    Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	        Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	            Joins the elements of an iterable to the end of the string
# ljust()	            Returns a left justified version of the string
# lower()	            Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	        Returns a translation table to be used in translations
# partition()	        Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	            Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	            Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	            Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	            Returns a trimmed version of the string
# swapcase()	        Swaps cases, lower case becomes upper case and vice versa
# title()	            Converts the first character of each word to upper case
# translate()	        Returns a translated string
# upper()	            Converts a string into upper case
# zfill()	            Fills the string with a specified number of 0 values at the beginning