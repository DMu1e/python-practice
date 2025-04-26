# This is code on how to add numbers in a list of numbers
x= int(input("How many numbers do you want in the list: "))

list=[] #Initialises the list 

for i in range(x): #Allows us to added as many numbers as the user inputed
    list.append(int(input()))

sum_list=0

for i in list: #Adds every number on the list
    sum_list=sum_list+i

print("The sum of the list of numbers is:",sum_list)
    