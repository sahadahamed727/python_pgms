string=input("Enter a string:")
old=input("Enter the character to replace:")
new=input("Enter the new character:")
result=string.replace(old,new)
print("new string:",result)
reverse=string[::-1]
print("Reversed string:",reverse)
if string==reverse:
    print("\n The string is a palindrome")
else:
    print("\n The string is not a palindrome")
characters=len(string)
words=len(string.split())
print("\nnumber of characters:",characters)
print("\nnumber of words:",words)