# DAY-8
# 1.) Write a python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary (n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4:  16, 5: 25}

# ! Eg:2
# ? Function  with parameter
#def greeting(name): a name is parameter
 #    print("Welcome", name)

# for val in range(3):
#     username = input("Enter the name: ")
#     greeting(username_) # username is argument

# ! Eg:3
#def profile(name, age, place):
 #    txt ="My name is {}. Iam {} years old. Iam from {}."
  #   print(txt.format(name, age, place))
#profile("sid", 29, "cbe")

# ! Eg:4
# ? Function with return statement

# def f1():
#     z = 8
# f1()
# print(z) # error --> cannot use outside the function

#def f1(a, b):
 #   c = a*b
  #  return c
# print(f1(6,8))
#obj = f1(6,8)
#obj = f1(4, 6)


# def gracemark():
#     print(obj+4)
#      print(obj+4)
# gracemark()
# gracemark()

# 123
#def palindrome(n):
 #   string = str(n)
  #  rev = str(n)[::-1]
#    if string==rev:
 #       print(n, "Palindrome")
 #   else:
  #      print("Not palindrome")
#a = int(input("Enter the value: "))
#palindrome(a)

# ? Based on the declaration of parameter and args
# ? functions are divided into 5 catagories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * Positional args
# The position of parameter ahve to be same as position as arguments
# Eg:1
#def def profile(name, phone, mark):
 #       txt = "My name is {}. My phone number is {}. I got {} marks."
  #      print(txt.format(name, phone, mark))

# * keyword args
# ! Eg:1
#To overome the disadvantage of position args, we use keyword args
#def profile(name, phone, mark):
#    txt = "My name is {}. My phone number is {}. I got {} marks."
 #   print(txt.format(name, phone, mark))
#profile(name="sid", mark=96, phone=234567890)

# profile(name="sid", 1234567, mark=98) # error -> positional args follow
# profile(123456789, name="sid",mark=98 # error -> name has multiple value
#profile("sid", mark=98, phone=123456789)


# * Default args
# The method of assigning the argument to the parameter while declaring the
# ! function
# ! Eg:1
#def profile(name, phone, kadapa):
 #   txt = "My name is {}. My phone number is {}. I am from {}."
  #  print(txt.format(name, phone, kadapa))

#profile("sid", 8767676767, "Guntur")

# ! Exception
#def profile(name, phone, kadapa): # error --> coz default args should not follow
 #   if place == "kadapa" or place == "kadapa" or place == "KADAPA":
  #      print("you are not eligible to Signup")
   # txt = "My name is {}. My phone number is {}. I am from {}."
   # print(txt.format(name, phone, kadapa))
   # print(txt.informat(name, phone, kadapa))


#! Variable length parems
# ! Eg:1

#def profile(name):
 #   print("My name is santhu
# name = "sid", "name1", "name2"
#def profile(*name):
 #   for val in name:
  #      print("My name is",val)
#profile("sid", 'name2', 'name3')

# ! Eg:2
#def profile(age, *name):
 #   for val in name:
  #      print("My name is",val, "my age is", age)
#profile(28, "sid", 'name2', 'name3')

# * keyword variable length args
# kwards --> whish is used to provide the args in the form of key value pair.
# ! Eg:1
#def price(price_list):
 #   price(price_list)

# price(shirt=1000, iphone=80000)

# d1 = {"a":100, "b":200, "c":300}
# d1 = dict(a=100, b-200, c=300)
# print(d1)

# n =5
# {1:1, 2:4, 3:9, 4:16, 5:25}

#n = int(input("Enter the number: "))
#d1 = {}
#for val in range(1, n+1):
#    d1[val] = val*2
 #   print(d1)

#def dict1(n):
 #   d1 = {}
  #  for val in range(1, n+1):
   #     d1[val] = val**2
  #  print(d1)
#dict1(5)

# ! --------> object oriented programming
# The panadigms of object oriented programming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# Class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# ? Eg:1
#class c1:
 #   name1 = "sanhu"
  #  print(name1)

# ? Eg:2
 # class person:
  #    name = "sindhu"

  #c = person()
  #print(c.name)

# c = person() # c as object
# The process of creation of an object is called as installation
# print(c.name)
    

# ? Eg:3
# create of a method
# when the function is created with a class is called as method

#class person:
#    def display(person):
#        print("Hello welcome to classes")

#p = person()
#p.display()
    
# ? Eg:4
# ! Method without parameter
#class person:
 #   def display(person, name, age):
  #      print(name, age)

#p = person()
#p.display("santhu", 20)


# ! Eg:5
#class person:
 #   name3 = "sidhu" #attribute or static variable
#
 #   def display(person):
  #      print(person.name3)

#p = person()
#p.first_name()
#p.full_name()


#class person1:
 #   fname3 = "sidhu" #attribute or static variable
  #  lname = "T"

   # def first_name(self):
    #    print(self.fname+" "+self.lname)

#p = person()
#p.first_name()
#p.full_name()


# ? Eg:6
# constructors --> _init_()
# This is a special method which has the ability to execute itself without
# calling it manually through the process of instantiation

#class profile:
 #   def __init__(self): # constructor method
  #      print("hey")

#p = profile() #execution of constructor through this process
#p.__init__()


#! Multilevel inheritance
# ? Eg:1
#class voice:
 #   def sound(self):
  #      print("all the animals have their own voice
#class dog(voice):
 #   def dog_voice(self):
  #      print("bark")
#class cat(dog):
 #   def cat_voice(self):
  #      print("meow")
#class parrot(cat)

# ! multiple inheritance
# ? It has multiple parent and 1 child

#   def function(self):
 #       print("used to Airplans")
        
#class while_petrol:
 #   def function_o(self):
  #      print("used for Bike, cars")

#class premium_petrol:
 #   def function_p(self):
  #      print("sports cars, bikes")

#class petrol(while_petrol, organic_petrol, premium_petrol):
 #   def defanition(self):
  #      print("petorl types")

#p= petrol()
#p.defanition()
#p.function_o()
'''
# ! Eg:2
class addition:
    def add(self, a, b):
        print(a+b)
        
class subtract:
    def add(self, a, b):
        print(a-b)
        
class multiply:
    def mul(self, a, b):
        print(a*b)
        
class division(addition, subtract, multiply):
    def add(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)

'''
# ! Heirarical inheritance
#class catagory:
 #   def cat_name(self, weight):
  #      print(weight)


   #  def display(self, colour, taste):
    #     print(colour, taste)

#class Tomato(catagory):
 #   def tomato_specs(self):
  #      color='black"
   #     taste = "neutral taste"
    #    self.display(colour, taste)

#class carrot(catagory):
 #   def carrot_specs(self):
  #      color="green"
   #     taste = "sweet"
    #    self.display(colour, taste)


#c = carrot()
#c.carrot_specs()
#c.weight("30gms")


# ! Hybrid inheritance
# ? The combination of above 4 inheritance is called Hybrid inheritance
#class c2(c1):
 #   def m2(self):
  #      print("class2")
#class c3(c2):
 #   def m3(self):
  #      print("class3")
#class c4(c3):
 #   def m4(self):
  #      print("class4")
#class c4:
 #   def m4(self):
  #      print("class4")
#class c5:
 #   def m5(self):
  #      print("class5")
#class c6(c5, c3):
 #   def m6(self):
  #      print("class 4")
#obj = c6()
#obj.m3()


# ! -------> polymorphism
# poly - many, morph --> form
#A function which has the ability to perform more than 1 functionality
#then it is considered to be as polymorphism

# * polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop()
# and more...

# * polymorphism in operators
# +
#print(8+8)
#print("k"+'1')
#print([1,2,3]+[5,6])

# *
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
def f1(*args):
l1 = [1,2,3,4]
print(l1*10)


  

  



    
    






