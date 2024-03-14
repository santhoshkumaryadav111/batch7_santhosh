Day:3


#length=int(input())
#breadth=int(input())
#if length==breadth:
#      print("its a square")
#else:
#    print("its not square")

# ! Eg:4
#python program to check whether the
#given integer is a multiple of both 5 and 7
'''
n=int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :

 #  Cost price (in Rs)      Tax
 # > 100000                 15 % + discount 6%
 #  > 50000 and <= 100000   10%
  # <= 50000                5%

  # price=int(input("enter the price: "))
  # amount=0
  #if price>=100000:
  #     discount=100000*(6/100)
   #    value=price-discount
    #   amount=value*(15/100)
   #    total=value+amount
   # else:
   #     tax=price*(5/100)
    #    total=price+tax
   #  print("The anroad cost of bike is: ",total)   


# !--------->  if elif else
# Eg:1
'''
a=7
b=9
c=30

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("c is greater")
'''



# A school has following rules for grading system:
# a. Below 25 -F
# b. 25 to 45 -E
# c. 45 to 50  D
# d. 50 to 60 - c
# e. 60 to 80 -B
# f. 45 Above 50 -A
'''
mark=int(input("Enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:   
   print("D")
else:
    print("Fail")
    '''
'''
# ! code to check the given char is vowel or consonent
char=input("enter the char: ")

#if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    #print("is a vowels")
#else:
    #print("consonent")

 # ? or
'''
'''
str1="santhosh"
if char in str1:
     print("vowel")
else:
     print("consonent")
    
# ! -----------> looping

looping can be implemented using
for loop
while loop
'''
'''
# ! ---> for loop
# ? for loop is used for iteration, if we know  the number of times the loop have to run
# ? it is used to iterate the iterables eg(string, list, tuple, etc...)

# todo --> syntax for loop

# ! for syntax in c
# for(i-0;i<10;i++){
#     printf("hello");
# }
'''
# ! for syntax in python
# for userdefined_variable in range(start, end, step);
#     statement
#     statement
#     statement
'''
# ? Eg:1
# To print the value from 1 to 10 using for loop
'''
'''
for i in range(0, 10): #(n, n-1)
     print(i)
     print("hello")
'''
'''
# ? Eg:2
#for val in range(1, 15, 2):
#     print(val)

for val in range(1, 15, 3):
     print(val)
'''
'''
# ? Eg:3
# to decrement the value

for val in range(10, 0, -1):
    print(val)
 for val in range(10, 0, -1):
    print(val) # no output
'''
'''    
# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
for val in range(1, 10+1):
     print('7','x',val,'-',val*7)
'''
'''
     # --> Method:2
       ans="7x{}- {}"
     #print(ans,format(val, val*7))
'''
'''
     # --> Method:3
     print(f"7 x {val}-{val*/}")
'''
'''
# ?Eg:5
# break --> used to terminate the loop

for val in range(1, 10):
     if val ==9:
          break
     print(val)
'''
'''
# ? Eg:6
for val in range(1, 10):
     if val ==6:
         print(val)
         break
'''
'''
# | continue
# Eg:1
for val in range(1, 10):
     if val ==6:
          continue
     print(val)
'''
'''
# ! practice problems
# ? print the even number between 20 to 40
for i in range(20, 40, 2):
      print(i)
'''
# Method 2
for  i in range(20, 41):
       if(i%2 ==0):
            continue
       print(i)
      



 
