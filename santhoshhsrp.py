#Day-7

# ------> Assement
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# 2.)dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}



#d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#d1.update(d2)
#print(d1)


# 2.)Python program to determine if
# the given Sets Are Disjiont
# or Not without Using Inbuilt-in Functions


#set1 = {'Python', 'Java', 'Data Science'}
#set2 = {'ML', 'AI', 'R Language', 'Python'}
#set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
#c = 0
#flag=0
#for val in range(3):
 #   c=c+1
  #  if c==1:
   #     for val in set1:
    #        if val in set2 or val in set3:
     #           flag=1
      #          break
    #if c==2:
     #   for val in set2:
      #      if val in set1 or val in set3:
      #          flag=1
      #          break
    #if c==3:
    #     for val in set3:
    #         if val in set2 or val in set1:
    #             flag=1
    #             break


#if flag==0:
#    print("Disjiont")
#else:
 #   print("Jiont")


# 3.)
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#l3 = []
#for val in range (len(list1)):
#    ans = list1[val]+list2[val]
 #   l3.append(ans)
#print(l3)

#i=0
#while i<len(list1):
 #   l3.append(list1[i]+list2[i])
 #   i+=1
#print(l3)


# Hacker rank --> Caesar Cipher

# ! Functions
# DEF
#Function is a block of code which is used to perform a specific Functionality
# Function can be created using def keyword

#Function has a 3 parts
#Function declaration
#Function defanition
#Function call


#def greet(): # function defanition
 #   print("Greetings User!!")

#greeet()
#greeet()
#greeet()
#greeet()
#greeet()
#greeet()
#greeet() # function calling


# ! Eg:2
# ? Function with parameter
#def adding():
 #   a = int(input())
  #  b = int(input())
   # c = int(input())
   # d = a+b+c
   # print(d)
#adding()
#adding()


# ! Eg:2
# ? Function with parameter
def greeeting(name):
    print("Welcome", name)

for val in range(3):
     username = input("Enter the name: ")
     greeting(username)












            
