#This is code to find the factorial of a number using recursion
x=int(input("Enter the you want the factorial for: "))

# The below function calls upon itself until it reaches the base case where it now send back the info to get the answer
def fact (n):
    if n==0: #Base Case 
        return 1
    return n * fact(n-1) #Recursive case

ans= fact (x)

print(ans,"is the factorial of",x)