fruits = ["apple", "banana", "cherry"]
# add 5 more fruits
fruits.extend(["date", "elderberry", "fig", "grape", "honeydew"])

letter_count = {}

for fruit in fruits:
    for letter in fruit:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print(letter_count)

# shift the letters in each fruit by 1
shifted_fruits = []
for fruit in fruits:
    shifted_fruit = ""
    for letter in fruit:
        shifted_fruit += chr(ord(letter) + 1)
    shifted_fruits.append(shifted_fruit)

print(shifted_fruits)

# create a dictionary with the original fruit as the key and the shifted fruit as the value

fruit_dict = dict(zip(fruits, shifted_fruits))
print(fruit_dict)