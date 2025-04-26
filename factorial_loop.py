# This code to do the factorial of a specific number using the while loop
x=int(input("Enter the you want the factorial for: "))

sum=1
y=0
# The loop repeats its self until it y and x are equal at the same time the number keeps multipling itself 
while(y<x):
 y=y+1
 sum=sum*y
 
print(sum,"is the factorial of",x)