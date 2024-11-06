import math

a = int(input("Write a number a: "))
S = a ** 2
print("Square: ", S)

d = int(input("Write a number d: "))
L = d * 3.14
print("Circle perimeter: ", L)


L = int(input("Write a number L: "))
R = L / 2 / 3.14
S = 3.14 * R ** 2
print("R: ", R)
print("S: ", S)


a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
c = math.sqrt(a ** 2 + b ** 2)
(a ** 2 + b ** 2) ** 0.5
P = a + b + c
print(f"c is {c}\n" + f"P is {P}\n")