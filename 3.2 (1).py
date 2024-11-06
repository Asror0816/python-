a = int(input("Write a number a: "))
b = int(input("Write a number b: "))
z = a + b
d = a - b
c = a * b
dev = b / a
rem = a % b
whole = a // b
k1 = a ** 2
k2 = b ** 2
k3 = b ** a
g = z > c
s = z < c
e = z == c

print(f"Sum: {z}\n" +
      f"Multiply: {c}\n" +
      f"a^2: {k1}\n" +
      f"b^2: {k2}\n" +
      f"a-b= {d}\n" +
      f"a/b={dev}\n" +
      f"remainder of a/b: {rem}\n" +
      f"the whole number: {whole}\n" +
      f"b^a={k3}\n" +
      f"greater: {g}\n" +
      f"smaller: {s}\n" +
      f"equal: {e}"
      )
