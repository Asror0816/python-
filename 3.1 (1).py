import math

# 1
a = int(input("Write a number a: "))
print("S is " + str(6 * a ** 2))
print("V is " + str(a ** 3))

# 2
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
c = int(input("Write a number c: "))
print("S is " + str(6 * a ** 2))
print("V is " + str(2 * (a * b + b * c + a * c)))

# 3
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
print((a + b) / 2)

# 4
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
z = a + b
c = a * b
k1 = a ** 2
k2 = b ** 2
print(f"Sum: {z}\n" +
      f"Multiply: {c}\n" +
      f"a^2: {k1}\n" +
      f"b^2: {k2}\n")


# 5
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
z = a + b
c = a * b
k1 = a ** 2
k2 = b ** 2
mod1 = abs(a)
mod2 = abs(b)

print(f"Sum: {z}\n" +
      f"Multiply: {c}\n" +
      f"a^2: {k1}\n" +
      f"b^2: {k2}\n{mod1}\n{mod2}")


# 6
x1 = int(input("Write a number x1: "))
y1 = int(input("Write a number y1: "))
x2 = int(input("Write a number x2: "))
y2 = int(input("Write a number y2: "))
s = math.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2))
print(f"s = {s}")
