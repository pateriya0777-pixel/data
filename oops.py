# Generator is a special type of function in Python that allows you to return a sequence of values one at a time, 
# instead of all at once.
#1. How will you check if a class is a child of another class?

class Parent(object):
   pass   
 
class Child(Parent):
   pass   
  
# Driver Code
print(issubclass(Child, Parent))    #True 
print(issubclass(Parent, Child))    #False
===================

6. Is it possible to call parent class without its instance creation?

# If the parent class has a method decorated with @classmethod or @staticmethod,
1. 
class Parent:
    @staticmethod
    def say_hello():
        print("Hello from Parent Class!")

Parent.say_hello()

# 2. super() is used inside a child class to call the parent's __init__ or other methods.
#  It looks up the method in the parent class automatically.
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        # Calling parent __init__ without creating a Parent instance
        super().__init__(name) 
        self.age = age

c = Child("Shashank", 25)
print(c.name)
'''

#3 You can also call the parent method by explicitly naming the class and passing self.
'''

class Parent:
    def greet(self):
        print("Parent greeting")

class Child(Parent):
    def greet(self):
        Parent.greet(self) # Calling parent method directly
        print("Child greeting")
        '''
'''
class Student:
    school_name ="Gvt School"
    def __init__(self,f_name,l_name,account_no):
        self.f_name = f_name
        self.l_name = l_name
        self.account_no = account_no
    def getname(self):
        print("hello",self.f_name, self.l_name)
    @classmethod
    def class_method(cls):
        print(cls.school_name)
    @staticmethod
    def info():
        print("this is static method")

obj = Student("shashank","Pateria",111)
print(obj.account_no)
obj.getname()
Student.class_method()
Student.info()

'''

method needs to access or modify data that belongs to the entire class, rather than a specific object.

#Interview Tip: "I use instance methods for behaviors that depend on the specific state of an individual object."
# Interview Tip: "I use class methods when I need to access data that is common to all instances, or to create 'Factory' methods."
#Interview Tip: "I use static methods for logic that is logically related to the class but doesn't require any information from the class or its instances."
'''



# Parent class
class A:
   def __init__(self, a_name):
       self.a_name = a_name
   
# Intermediate class
class B(A):
   def __init__(self, b_name, a_name):
       self.b_name = b_name
       # invoke constructor of class A
       A.__init__(self, a_name)
       
   def display_names(self):
       print("A name : ", self.a_name)
       print("B name : ", self.b_name)

#  Driver code
obj1 = B('child', 'parent') 
# print(obj1.a_name)
obj1.display_names()  

#==============
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calls the Parent constructor
        self.model = model

#======================



li = [10, 29, 83, 65, 86, 99, 54]

# Initialize with the first element
my_max = li[0]
my_min = li[0]

for x in li:
    if x > my_max:
        my_max = x  # New maximum found
    if x < my_min:
        my_min = x  # New minimum found

print(f"Manual Max: {my_max}")
print(f"Manual Min: {my_min}")
'''

'''
def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if (list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list



list = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list))

'''



#Program to display the Fibonacci sequence up to n-th term
''' # 0,1,1,2,3,5,8,13
no = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if no <= 0:
   print("Please enter a positive integer")
elif no == 1:
   print("Fibonacci sequence upto",no,":")
   print(n1)
else:
   while count < no:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


#mul = lambda a,b:a*b
#print(mul(2,5))



s = [1,2,3,4,6,7,5,4,5,7,66,]
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
for k,v in d.items():
    print('{} occour {} times'.format(k,v))


# Get the second largest number in a list in linear time
numbers = [66, 55,88, 2.6, 7, 74, 2.8, 90.8, 52.8, 4, 3, 2, 5, 7]
if (numbers[0] > numbers[1]):
    m, m2 = numbers[0], numbers[1]
else:
    m, m2 = numbers[1], numbers[0]
for x in numbers[2:]:
    if x>m2:
        if x>m:
            m2 = m
            m = x
        else:
            m2 = x
print(m2)

