# This is code to sum up the digits in a number
x=int(input("Emter a number with more than one place value: "))

sum=0
# I needed to extract the numbers individully and using the modulus I was able to get the last value consitently
while(x>0):
 rem = x % 10
 sum=sum+rem
 x=x//10 #This removes the last value without using remainders due to use of double foward slashes 

print(sum)
