# This is code to reverse a string in python
x=input("Enter a word:")

reversed_x = ""

i = len(x) - 1  # Starts writing from the last character

# The loop writes every individual letter until the full word is formed
while i >= 0:
    reversed_x += x[i]
    i -= 1

print(reversed_x)