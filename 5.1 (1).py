# 1
K = int(input('Введите первое число K: '))
N = int(input('Введите второе число N: '))

count = 0
while count < N:
    print(K)
    count += 1

# 2
a = int(input('Введите первое число a: '))
sum = 0

for i in range(1, a + 1, 2):
    sum += i

print(sum)

# 3
n = int(input('Введите первое число n: '))
sum = 0

for i in range(0, n + 1, 3):
    if i % 9 != 0:
        sum += i

print(sum)

# 4
n = int(input('Введите первое число n: '))
sum = 0

for i in range(1, n + 1):
    sum += i ** 2

print(sum)

# 5
n = (input('Enter a word: '))
a = int(input('Введите число: '))
print(n[:a - 1] + n[a:])

# 6
n = int((input('Enter a price: ')))
if n > 100000:
    n = n - n * 0.1
elif n > 50000:
    n = n - n * 0.05
else:
    n = n

print(n)

# 7
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

for i in reversed(range(a + 1, b)):
    print(i)
print("Between A and B there are: ", abs(a - b) - 1, "numbers")

# 8
n = int(input('Введите первое число: '))
cost = 0

for i in range(1, 11):
    print("Prise for ", i, "kg is: ", n * i)

# 9
n = int(input('Введите первое число: '))
cost = 0

for i in range(1, 10):
    i = i / 10
    print("Prise for ", i, "kg is: ", n * i)

# 2
word = "d!v!l@p!r"
result = ""
for i in word:
    if i == "!":
        result += "e"
    elif i == "@":
        result += "o"
    else:
        result += i

print(result)

# 3
a = input('Word: ')
b = input('Letter: ')
count = 0
for i in a:
    if i == b:
        count += 1

print(count)

