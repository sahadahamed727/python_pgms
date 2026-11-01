num = [10, 20, 30, 40, 50]
x = int(input("Enter a number to search: "))
if x in num:
    print(x, "is present in the list")
else:
    print(x, "is not present in the list")
num[1] = 25
print("Updated list:", num)
even = [n for n in num if n % 2 == 0]
print("Even numbers:", even)
num.remove(30)
print("After removing 30:", num)
num.sort()
print("Sorted list:", num)