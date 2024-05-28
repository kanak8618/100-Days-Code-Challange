# Please write a program to compress and decompress the string

import zlib

string = input("Enter A String : ")


compressed_string = zlib.compress(string.encode())
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)