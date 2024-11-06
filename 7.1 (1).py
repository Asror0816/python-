# 1
user_input = input("Введите текст: ")
letter_count = {}
for letter in user_input:
    if letter.isalpha():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print("Результат подсчета букв:")
print(letter_count)

# 2
dict1 = {'a': 1,
         'c': 2}
dict2 = {'c': 3,
         'd': 4}

merged_dict = {}

merged_dict.update(dict1)
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print(merged_dict)

# 3
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

count_dict = {}

for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)
