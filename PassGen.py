import random

x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    try:
        long = int(input("Introduce la longitud de tu contraseña: "))
        break 
    except ValueError:
        print("Error: Ingresa un número valido!!")

gen = ""

for value in range(long):
    caracter = random.choice(x)
    gen += caracter

print("Tu contraseña generada es:", gen)