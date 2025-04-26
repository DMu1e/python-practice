# Code to show whether a number is odd or even 
number= int(input("Enter an integer number: "))

# The modulus will divide the number by two and if the remainder is zero then it is even 
remainder = number % 2

if (remainder == 0):
    print(number,"is an even number")
else:
    print(number,"is an odd number")