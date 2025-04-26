# This is code to reverse a string in python
x=input("Enter a word:")

reversed_x = ""

i = len(x) - 1  # Start from the last character

while i >= 0:
    reversed_x += x[i]
    i -= 1

print(reversed_x)