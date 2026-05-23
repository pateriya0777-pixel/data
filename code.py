

# 1 .reverse the string 

s  = "quick brown fox jumps over the lazy dog"
# rev = reversed(s)
# op = ''.join(rev)
# print(op)

# op = ''
# for i in range((len(s)-1),-1,-1):
#     op = op + s[i]
# print(op)

# s  = "quick brown fox jumps over the lazy dog"
# i  = len(s)-1
# op = ''
# while i >= 0:
#     op = op + s[i]
#     i = i-1
# print(op)

### -------------------------------------------------------------------------------
# 2. reverce order of words present in the given string
#
'''
s  = "quick brown fox jumps over the lazy dog"
sp = s.split()
op = sp[::-1]
fop = ' '.join(op)
print(fop)
'''

# 3 reverce internal content of each word     # 
'''
s  = "quick brown fox jumps over the lazy dog"
sp = s.split()
op = []
for i in sp:
    op.append(i[::-1])
fop = " ".join(op)     
print(fop)
'''

'''
s  = "quick brown fox jumps over the lazy dog"
sp = s.split()
op = ''
for i in sp:
    op = op + ' ' + (i[::-1])
fop = "".join(op)
print(fop)
'''
# 4 reverce every second word
# s = "zeoro one two three four five six seven eight"
# sp = s.split()
# li = []
# for i in range(len(sp)):
#
#     if i % 2 == 0:
#         li.append(sp[i])
#     else:
#         li.append(sp[i][::-1])
# print(li)
#
'''
s = 'abcdefghijklmnopqrstuvwxyz'
ev = []
odd = []
for i in range(len(s)-1):
    if i % 2 == 0:
        ev.append(s[i])
    else:
        odd.append(s[i])
print('ev',ev)
print('odd',odd)
'''
'''

li = [10, 29, 83, 65, 86, 99, 54]

# Initialize with the first element
li = [10, 29, 83, 65, 86, 99, 54]
minn = li[0]
maxx = li[0]
for x in li:
    if x > maxx:
        maxx = x
    if x < minn:
        minn = x
print(maxx)
print(minn)

    


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

'''




#mul = lambda a,b:a*b
#print(mul(2,5))



''''
a = "shashank"
a = [*a]
#or [*"shahshak"]
print(a)
'''



#max min using
''''
no = int(input("enter number"))
list = []
for i in range(no):
    x = int(input("please enter list element"))
    list.append(x)
print("max is",max(list))
print("min is",min(list))

'''


#remove duplicate usng list comprehention
''''
li  = [34,87,24,86,11,34,66,76,34,87,24,86]
s_list  = []
[s_list.append(i) for i in li if i not in s_list]
print(s_list)

'''

'''
li  = [34,87,24,86,11,34,66,76,34,87,24,86]
sum = 0
sum(i for i in li)
print(sum)
'''
# sum all the element
''''
li  = [34,87,24,86,11,34,66,76,34,87,24,86]
sum = 0
for i in range(0,len(li)):
    sum =  sum + li[i]
print(sum)
'''

# sum all the element
''''
li  = [1,2,3,4,5]
mul = 1
for i in range(0,len(li)):
    mul =  mul * li[i]
print(mul)
'''
#5.Program to generate a number list between two ranges.
'''
for i in range(0,101):
    print(i)
    
'''
#How to reverse the List using slice
''''
tu  = (1,2,3,4,5)
print(tu[::-1])
'''

#7.How to flatten a list of lists with a list comprehension
'''
li = [[5,6,7,'C#'], ['C++',2,3]]
flatten = [j for i in li for j in i]
print(flatten)
'''

#8.How to Intersect two list
'''
li1 = ['C++',2,3,6,7,5,'C#']
li2 = ['C++',5,6,7,'C#']
i_sect = [i for i in li1 if i in li2]
print(i_sect)
'''
#9.Program to shuffle a list and print
'''
from random import shuffle
listnum = ['Rust','go','C++',2,3,6,7,5,'C#']
shuffle(listnum)
print(listnum)
'''
#10. Program to convert a list into string
'''
list= ['Rust','go','C++','C#']
st = " ".join(list)
print(st)
'''

#11.How to get the square of each list element between two range
'''
li = list(range(0 ,10))
sq = [i**2 for i in li]
print(sq)
'''


'''
# 12. Program to get the difference between two List using comprehension
li1 = [1,2,3,4,5]
li2 = [11,22,33,44,5]
diff = [i for i in li1 if i not in li2]
print(diff)
'''
#string datatype

""""
s = 'aabbccddef'

unique = ''
for i in s:
    if i not in unique:
      unique = unique + i
print(unique)

for i in unique:
    count = 0
    for char in s:
        if i == char:
            count +=1
    print("{} occoursm {} times".format(i,count))

"""

'''
s = [1,2,3,4,6,7,5,4,5,7,66,]
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
for k,v in d.items():
    print('{} occour {} times'.format(k,v))
'''


#21) Can you write a program to find the average of numbers in a list in Python?
'''
no = int(input('enter any number'))
li = []
sum = 0
for i in range(no):
    x = int(input("enter numbers"))
    li.append(x)
    sum = sum + x
    avg = sum /3
print(li)
print(avg)
'''
#22) Write a program to reverse a number in Python?
'''
n = 12345
rev = 0
while n >0:
    dig = n % 10
    rev = rev *10 + dig
    n = n // 10
print(rev)
'''
#total numbers
'''
n = 12345
tot = 0
while n >0:
    dig = n % 10
    tot = tot  + dig
    n = n // 10
print(tot)

'''
#palindrome or not
'''
n = 151
temp = n
rev = 0
while n >0:
    dig = n % 10
    rev = rev *10 + dig
    n = n // 10
if temp == rev:
    print("this ispalindrome")
else:
    print("not a palindrome")
print(rev)
print(type(rev))
print(type(n))
'''

#25) Write a Python Program to Count the Number of Digits in a Number?
'''
n = 12345
count = 0
while n>0:
    count = count +1
    n = n//10
print(count)
'''
#26) Write a Python Program to Print Table of a Given Number?
'''
n = int(input("ener any no."))
for i in range(1,11):
    print(i,i*n)

'''

'''
n = int(input("ener any no."))
for i in range(2,n):
    if n % i == 0:
        print("not a prime no")
        break
else:
    print("prime no") 


'''


#perfect no
'''
no = int(input("enter no"))
temp = no
sum = 0
for i in range(1,no):
    if no % i == 0:
        sum = sum + i
if sum == no:
    print("perfect")
else:
    print(("not"))
'''


#arm
'''
n = int(input("entr no"))
sum = 0
temp = n
while temp >0:
    dig = temp % 10
    sum =sum + dig**3
    temp  = temp//10

if n == sum:
    print("arm")
else:
    print("not")

'''
#list swap values


#genertor
'''
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n = n+1
obj = topten()
for i in obj:
    print(i)
'''
#rev str using gen

#
# def rev_str(my_str):
#     st = ''
#     leng = len(my_str)-1
#     for i in range(leng,-1,-1):
#         yield my_str[i]
# obj = rev_str("quick brown fox jumps over the lazy dog")
# for i in obj:
#     print(i)
#
# dic = {"name" : "shahsnak","age":24}
# (dic["name"]) = "shashank paterya"
# print(dic["name"])

#
# list = [5,4,3,2,1]
# # list.sort()
# list.insert(1,9)
# list.sort()
#
# print(list)


'''





#decorator
'''


def deco_fun(fun):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return inner 


@deco_fun
def div(a,b):
    print(a/b) 
div(2,4)

"""


How it works
Generators use the yield keyword instead of return.

return: Sends a value back and kills the function.

yield: Sends a value back and pauses the function, remembering where it left off.

Python
"""
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Function "pauses" here
        count += 1


counter = count_up_to(3)

# print(next(counter))  # Output: 1
# print(next(counter))  # Output: 2
# print(next(counter))  # Output: 3

for i in counter:
    print(i)


'''
'''
# def fibb():
def decor_result(res_function):
    def distinction(marks):
        for i in marks:
            if i >= 75:
                # print("got distinct")
                pass
        print("got distinct")

        res_function(marks)
    return distinction

    '''
'''
@decor_result
def result(marks):
    for i in marks:
        if i >= 33:
            pass
        else:
            print('fail')
    else:
        print('pass')
# result([78,99,88,76,81])
'''

#
#print rev str is on vowel place
# Author by book name
# 2.book by aythor
#
# stri = "aterito"
# rev_str = stri[::-1]
# li = list(stri)
# li_rev = list(rev_str)
# s = 'aeiou'
# vw_li = list(s)
# op_li = []
# for i ,j in zip (li,rev_str):
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" and j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
#         temp = i
#         i = j
#         j = i
#         op_li.append(i)
#     else:
#         op_li.append(i)
#
# final_rev = ''.join(op_li)
# print(final_rev)

#min max one for loop
"""



#Get the second largest number in a list in linear time
# numbers = [66, 55,88, 2.6, 7, 74, 2.8, 90.8, 52.8, 4, 3, 2, 5, 7]
# if (numbers[0] > numbers[1]):
#     m, m2 = numbers[0], numbers[1]
# else:
#     m, m2 = numbers[1], numbers[0]
# for x in numbers[2:]:
#     if x>m2:
#         if x>m:
#             m2 = m
#             m = x
#         else:
#             m2 = x
# print(m2)



# find index no where value of two consecutive no is 9
# n = [4, 3, 6, 7]
#
# for i,j in zip(n,n[1:]):
#     if i + j == 9:
#         print(n.index(i),n.index(j))
#         print(i,j)

'''
list = [1, 2, 4, 5, 9, 8]
result= []
k =6
for i in range(len(list)):
    for j in range(i+1 ,len(list)):
        if list[i] +list[j] == k:
            result.append((list[i] ,list[j]))
print(result)


# Rename 'list' to 'items' to avoid overriding the built-in Python list function
items = ["banana", "apple", "banana", "mango", "mango", "mango"]

counts = {}
result = {}

for item in items:
    # Track how many times we've seen this item
    counts[item] = counts.get(item, 0) + 1
    
    # Logic for the key name
    if counts[item] == 1: 
        key = item
    else:
        key = f"{item}{counts[item]}"
    
    # Store the length in the result dictionary
    result[key] = len(item)

print("Frequency Tracker:", counts)
print("Final Result Dict:", result)


'''

# Goal: Count how many times each letter appears in a single word.
word = "banana"
freq = {}

for char in word:
    freq[char] = freq.get(char, 0) + 1

print(freq) 
# Output: {'b': 1, 'a': 3, 'n': 2}
# 
# '''

"""

#Goal: Categorize words into lists based on how many characters they have.
words = ["apple", "pear", "peach", "kiwi"]
grouped = {}

for w in words:
    length = len(w)
    if length not in grouped:
        grouped[length] = []  # Create an empty list for this length
    grouped[length].append(w) # Add the word to that list

print(grouped)
# Output: {5: ['apple', 'peach'], 4: ['pear', 'kiwi']}
"""

"""
Goal: Treat "Apple" and "apple" as the same item while generating unique keys.
items = ["Banana", "banana", "BANANA"]
counts = {}
result = {}

for item in items:
    clean_item = item.lower()  # Normalize to lowercase
    counts[clean_item] = counts.get(clean_item, 0) + 1
    
    if counts[clean_item] == 1:
        key = clean_item
    else:
        key = f"{clean_item}{counts[clean_item]}"
        
    result[key] = len(item)

print(result)
# Output: {'banana': 6, 'banana2': 6, 'banana3': 6}
# 
# """


"""
Goal: Create a subset of a dictionary based on a specific rule.
fruits = {'banana': 6, 'apple': 5, 'mango': 5, 'watermelon': 10}

# Dictionary Comprehension (The elegant way)
filtered_fruits = {k: v for k, v in fruits.items() if v > 5}

print(filtered_fruits)
# Output: {'banana': 6, 'watermelon': 10}
# """