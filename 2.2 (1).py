text = "hello"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print("  hello  ".strip())
print("hello world".replace("world", "python"))
print("hello,world".split(","))
print(" ".join(["hello", "world"]))
print("hello world".startswith("hello"))
print("hello world".endswith("world"))
print("hello world".find("world"))
print("hello world".index("world"))
print("12345".isdigit())
print("hello".isalpha())
print("hello123".isalnum())
print("    ".isspace())
print("hello".center(10))
print("hello".ljust(10))
print("hello".rjust(10))
print("hello world".count("l"))
print("hello world".startswith("hello"))
print("hello world".endswith("world"))
print("Hello World".swapcase())
print("42".zfill(5))
print("hello world".partition(" "))

name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))

data = {"name": "Alice", "age": 30}
print("Name: {name}, Age: {age}".format_map(data))

number = "42"
print(number.zfill(5))

print("hello world".rpartition(" "))