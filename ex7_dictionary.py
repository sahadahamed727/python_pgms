marks = {
    "Anu": 85,
    "Binu": 70,
    "cinu": 90,
    "Dinu": 80
}

sorted_marks = dict(sorted(marks.items()))

print("Sorted Dictionary:",sorted_marks)
dict1 = {
    "a": 10,
    "b": 20
}

dict2 = {
    "c": 30,
    "d": 40
}

merged = {**dict1, **dict2}

print("\n2. Merged Dictionary:",merged)



string = input("\nEnter a string: ")

c = {}

for ch in string:
    c[ch] = c.get(ch, 0) + 1

print("3. Character Frequency:")
print(c)




set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1 & set2
unique = set1 ^ set2

print("\n4. Set Operations:")
print("Set 1:", set1)
print("Set 2:", set2)
print("Common elements:", common)
print("Unique elements:", unique)