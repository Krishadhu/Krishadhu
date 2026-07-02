# Decimal to Binary, Octal and Hexadecimal

num = int(input("Enter a decimal number: "))

print("Binary      :", bin(num))
print("Octal       :", oct(num))
print("Hexadecimal :", hex(num))

# Binary to Decimal

binary = input("Enter a binary number: ")

decimal = int(binary, 2)

print("Decimal Number =", decimal)

# Octal to Decimal

octal = input("Enter an octal number: ")

decimal = int(octal, 8)

print("Decimal Number =", decimal)

# Hexadecimal to Decimal

hexa = input("Enter a hexadecimal number: ")

decimal = int(hexa, 16)

print("Decimal Number =", decimal)
