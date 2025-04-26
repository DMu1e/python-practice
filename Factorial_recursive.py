#This is code to find the factorial of a number using recursion
def fact (n):
    if n==0:
        return 1
    return n * fact(n-1)

