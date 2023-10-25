n = 17
width = len(bin(n)) - 2
print(width)
for i in range (1, (n + 1)):
    decimal = str(i).rjust(width)
    octal = oct(i)[2:].rjust(width)
    hexadecimal = hex(i)[2:].upper().rjust(width)
    binary = bin(i)[2:].rjust(width)  
    print(decimal, octal, hexadecimal, binary)