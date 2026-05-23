


The server generates a unique Session ID.
It sends this ID to the user's browser as a cookie.
On the next request, the browser sends the cookie back.

##: Each request from a client must contain all the information needed to understand and process the request. The server does not store any "session" data about the client
# The REST architecture is designed in such a way that the client state is not maintained on the server. This is known as statelessness. 
# The context is provided by the client to the server using which the server processes the client’s request. 
# The session on the server is identified by the session identifier sent by the client

#The technique of sending a message from the REST client to the REST server in the form of an HTTP request and the server responding back with the response as HTTP Response is called Messaging
# . The messages contained constitute the data and the metadata about the message.
'''

polumorphism : different class  can have same method but they  can behave differently depending on the object calling it.
Encapsulation hides data for security, Abstraction hides complexity for ease of use.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error

'''
1. What is __init__?
#__init__ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. 
'''

'''
class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")

'''




2. What is the difference between Python Arrays and lists?
Arrays in python can only contain elements of same data type 
Lists in python can contain elements of different data types , more space,consume large memory
'''

#13. What are lists and tuples? What is the key difference between the two?

'''
3. Explain how can you make a Python Script executable on Unix?
Script file must begin with #!/usr/bin/env python
'''

'''
4. What is slicing in Python?
As the name suggests, ‘slicing’ is taking parts of.
Syntax for slicing is [start : stop : step] # by default step value is 1
Slicing can be done on strings, arrays, lists, and tuples.

'''

'''
6. What are unit tests in Python?
Unit test is a unit testing framework of Python.
Unit testing means testing different components of software separately. Can you think about why unit testing is important? 
Imagine a scenario, you are building software that uses three components namely A, B, and C. 
Now, suppose your software breaks at a point time. How will you find which component was responsible for breaking the software? 
Maybe it was component A that failed, which in turn failed component B, and this actually failed the software. 
There can be many such combinations.
'''

'''
1. The Code to Test (auth_logic.py)
#Python

def is_strong_password(password):
    # Requirement: Must be at least 8 characters long
    if len(password) < 8:
        return False
    return True

2. The Unit Test (test_auth.py)
#Python

import unittest
from auth_logic import is_strong_password

class TestAuth(unittest.TestCase):

    def test_short_password(self):
        # We expect this to be False
        self.assertFalse(is_strong_password("12345"))

    def test_long_password(self):
        # We expect this to be True
        self.assertTrue(is_strong_password("secure_pass_123"))

    def test_exact_limit(self):
        # Edge case: exactly 8 characters
        self.assertTrue(is_strong_password("12345678"))

if __name__ == '__main__':
    unittest.main()
    
'''
# ---------------------------------------------------------
'''
7. What is break, continue and pass in Python?
#break
#The break statement stops the loop entirely

for i in range(1, 10):
    if i == 5:
        break  # Stop the loop completely when we hit 5
    print(i)

# Output: 1, 2, 3, 4

# 2. continue : it skips the current iteration 
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3 and move to 4
    print(i)

# Output: 1, 2, 4, 5

#3. pass : The pass keyword represents a null operation in Python. It is generally used for the purpose of filling up empty blocks of code

def login_user():
    pass  # I will write the login logic later, but I don't want an error now
'''

# ---------------------------------------------------------------------------------------
"""
If you use a shallow copy on a nested list, the original gets "corrupted" because both lists share the same inner memory.

Python

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original) # Create shallow copy

shallow[0][0] = "X" # Change the NESTED list

print(f"Original: {original}") # Output: [['X', 2], [3, 4]]
# Oops! The original changed because the inner folders were shared.
 
The Solution (Using Deep Copy)
A deep copy creates an entirely new memory address for every single item, no matter how deep it is hidden.

Python

import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original) # Create deep copy

deep[0][0] = "X" # Change the NESTED list
print(f"Original: {original}") # Output: [[1, 2], [3, 4]]
print(f"Deep Copy: {deep}")     # Output: [['X', 2], [3, 4]]


"""

#9. What are global, protected and private attributes in Python?
'''
 In Python, these all are  refer to Access Modifiers. we have three type of accss modifier.
 # 1 . public/ global 
 # variables which is defined in the global scope. To use the variable  
 inside a function, we use the global keyword.

 # Ex:
class Car:
    def __init__(self):
        self.brand = "Acer" # Public

my_car = Car()
print(my_car.brand) # Works fine!

# private :  
# these variables start with single underscore as a prefix . They can still be accessed and modified from outside the class 
class Car:
    def __init__(self):
        self._engine_temp = 90 # Protected

my_car = Car()
print(my_car._engine_temp) # Still works, but it's considered "bad manners."


#3 . private : 
# these variables start with double underscore as a prefix .If you try to access it directly from outside, Python will throw an error.
class BankAccount:
    def __init__(self):
        self.__pin = 1234 # Private

account = BankAccount()
# print(account.__pin) # This will CRASH the program!


class BankAccount:
    def __init__(self):
        self.__pin = 1234 # Private

account = BankAccount()
# print(account.__pin) # This will CRASH the program!
'''



# 9 . What are modules and packages in Python?
# Modules: simply Python files with a .py extension and can have a set of functions, classes, or variables defined and implemented. 
# package : collection of modules called packages



# 7. What are the differences between pickling and unpickling?
# pickling converiong pythonobject to binary form  pickle.dump()
                                                    #pickle.load()


# 10. What are lambda functions?
# Lambda is a  anonymous functions . it can accept any number of parameters.
#  usually used where functions are required only for a short period. 
# define the logic in a single line without giving it a name.
"""
square = lambda x: x * x
print(square(5))
"""

"""
map() :  Modify every item.
filter(): Select items that match a rule.
sorted(): Rearrange items in order.
"""


#

# list and dict comprehension.
"""
my_list = [2, 3, 5, 7, 11]
squared_list = [x**2 for x in my_list]    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]
squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
"""


3 #decorator
Adding extra functionality to the existing function , 
supppose currently i am working on one function without explicitly modifying its source code.few decorator example are retry , authentication  
"""def login_required(func):
    def wrapper(*args, **kwargs): ## "I'll hold whatever you give me!
        print("[System]: Checking if user is logged in...")
        # *args catches "Alex" and puts it in a tuple: ("Alex",)
        # then func(*args) unpacks it back to the profile function
        return func(*args, **kwargs)
    return wrapper

@login_required
def home():
    print("Welcome Home!")

@login_required
def profile(username):
    print(f"Welcome to {username}'s profile!")

# Both work perfectly because of *args and **kwargs!
home()
profile("Alex")
"""
# --------------------------------------------
"""
# 12 .*argas , **args

Example: Imagine a "Sum" function. You don't know if the user wants to add 2 numbers or 100 numbers.


def add_everything(*args):
    return sum(args) 

print(add_everything(1, 2, 3, 4)) # Output: 10
"""

"""
"*args and **kwargs are special keywords in Python that allow a function to accept a variable number of arguments.

*args stands for 'arguments' and collects extra positional inputs into a tuple.

**kwargs stands for 'keyword arguments' and collects named inputs into a dictionary.

"Think of *args as a way to handle a list of items. For example, if I'm writing a function to calculate_total(), I might not know if the user is passing 2 prices or 20. The * operator 'packs' those individual numbers into a single tuple that I can loop through."

**kwargs (The Named Tool)
"On the other hand, **kwargs is for named data. If I'm building a user_profile function, one user might provide an email, while another provides a phone number and a bio. **kwargs packs these into a dictionary, allowing me to handle optional settings without breaking the function signature."
"""


















x  = "quick brown fox jumps over the lazy dog"
# rev = reversed(x)
# print('>>',rev)
# op = ''.join(rev)
# print(op)

# print(x[::-1])

x= 5
for i in range(x):
    print(i)



