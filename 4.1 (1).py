# 1
a = int(input("Write a number a: "))
if a > 0:
    a += 1
elif a < 0:
    a = a - 2

print(a)


# 2
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
c = int(input("Write a number c: "))
l = [a, b, c]
positive = 0
negative = 0

for i in l:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1

print("positive numbers: ", positive)
print("negative numbers: ", negative)


# 3
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
if a > b:
    print(b)
else:
    print(a)


# 4
a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
c = int(input("Write a number c: "))
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

largest = a
middle = 0
if b > largest:
    largest = b
if c > largest:
    largest = c
    middle = (a + b + c) - smallest - largest

print(middle)
