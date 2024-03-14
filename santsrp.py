Day:4


# ----> while loop
# ----> break using while loop
'''
# eg:1
# 1.) Iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
'''

'''
i = 20
while i<27:
    if i==27:
        print(i)
        break
     i+=1
 '''
'''
# ! ------> continue
# ---> Eg:1
i = 20
while i<31:
     i=i+1
     if i==27:
         continue
     print(i)
'''
# while to iterate from 12 to 22
# find the sum of all numbers
'''
i = 12
sum=0
while i<23:
     sum=sum+1
     print(sum)    
     i+=1
'''
'''
# ! Eg:6
# Find the average of value from 20 to 25

i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    count+=1
    i+=1
print=(sum/count)
'''
'''
# ! --------> Nested to all
#eg:1

for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)
'''
 # Eg:2       
 # * * * *  
 # * * * *    
 # * * * *  
 # * * * *

'''
for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()
'''
'''
rows = int(input("enter the rows: "))
cols = int(input("enter the cols:"))

for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()
'''
'''
sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum, end=" ")
    print()
'''
#! to print stars in right angled triangle

'''
for row in range(0, 6):
    for col in range(0, row):
        print("*", end=" ")
    print()
'''
'''
 # * * * * * *   
 # * * * * *   
 # * * * *     
 # * * *    
 # * *    
 # *    
for row in range (6, 0, -1):
     for col in range(0, row):
         print("*", end=" ")
     print()
'''
'''
for row in range(5, 0, 5):
    for col in range(row, row):
        print("*", end=" ")
    print()
'''
'''
# * * * * * *   
# * * * * *
# * * * * * *
# * * * * * *
# * * * * * *  

for row in range(5):
    for col in range(5):
        if col==0  or col==5-1  or row ==0  or  row==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''
for row in range(0, 5):
    for col in range(0, 6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

for row in range (0, 0):
    for col in range(6, 6):
        if (row==0 and col==6

# ----> List


# -----> Datatypes
# primary

# Number --> int, float complex
# String
# Boolean
# None

# Collection
# List
# tuple
# set
# dictionary

# ? ---> List

# 1.) if the collection of elements are sorrounded by the square brakets.
# to be list
# ! eg:
    # l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]
            
# characteristics of list
# 1.) list have to be sorrounded by []
# 2.) it is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) the elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous
'''

# To access the elements in list
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
# print(lst1)

# We have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side
            
# ? --> Positive indexing
# print(lst1[0])
# print(lst1[4])
# print(lst1[20]) --> error
'''
# ? -----> Negative indexing
# lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1[-1])
# print(lst1[-5])            
# ? ----> slicing
# lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# lst1[start_idex:end_index:step]

print(lst1[0:4])
print(lst1[6:8)         
 '''         
lst1 =[1, 4, 1, 7,89.7, 7.5, "p", "i"]
print(lst1[3:6])            


            
            
            








            
    
            


    
  
