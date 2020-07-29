
# Map, Filter, Reduce, Lambda & Recursion
# Tasks Today:
# 1) Lambda Functions
#      a) Syntax
#      b) Saving to a Variable
#      c) Multiple Inputs
#      d) Passing a Lambda into a Function
#      e) Returning a Lambda from a Function
#      f) In-Class Exercise #1
# 2) Map
#      a) Syntax
#      b) Using Lambda's with Map
#      c) In-Class Exercise #2
# 3) Filter
#      a) Syntax
#      b) Using Lambda's with Filter
#      c) In-Class Exercise #3
# 4) Reduce
#      a) Syntax
#      b) Using Lambda's with Reduce
#      c) In-Class Exercise #4
# 5) Recursion
#      a) Implementing a Base
#      b) Writing a Factorial Function
#      c) In-Class Exercise #5
# 6) Generators & Iterators
#      a) Yield Keyword
#      b) Inifinite Generator
#      c) In-Class Exercise #6
# 7) Exercises
#      a) Exercise #1 - Filtering Empty Strings
#      b) Exercise #2 - Sorting with Last Name
#      c) Exercise #3 - Conversion to Farhenheit
#      d) Exercise #4 - Fibonacci Sequence

Lambda Functions
Lambda functions... or "Anonymous Functions" are referring to inline functions with no name. The keyword lambda denotes the no name function, and executes within a single line. Without saving it to a variable; however, it is not able to be used, unless passed in either as a paramater or within list comprehension.
Written as "(keyword lambda) (one or more inputs) (colon) (function to be executed)"

Syntax
In [1]:
#"(keyword lambda) (one or more inputs) (colon) (function to be executed)"  "Anonymous Functions" run function
# reg function
def addTwo(x):
 return x + 2

print(addTwo(4))


#lambda in () so pthon knows it is a callable function
# function  parameter after : return function
print((lambda x: x+2) (4))

# if we want this function to be availave later on in the program you have to put it ina  see nect cell
6
6
Saving to a Variable
In [2]:
f = lambda x,y : x + y +2
f(3,5)
Out[2]:
10
Multiple Inputs
In [3]:
#multiple inputs wuth no varailbr
(lambda x,y,z:  x*y*z)(3,5,8)

# milti inputs with a variablr
x = lambda x,y,z : x*y*z
x(3,5,8)
Out[3]:
120
Passing a Lambda into a Function
In [4]:
# signify the function anme
def multiply(f,num):
    """
    Our parameter list wwill use a lambda\
    function and a number
    """
    return f(num)

 #             f          num  see function definittion above
multiply(lambda x: x * x, 4)
Out[4]:
16
Returning a Lambda from a Function
In [5]:
#returning a lam function from a function
def multiply_test(num):
    return num* 4

print(multiply_test)#this gives you the memory location of multiply
      
print(help(multiply_test)) 

#our inner 
def returnFunc():
    def multiply(num):
        return num *2
    return multiply

#    outer function
f = returnFunc()
# print(f(4))

#print(returnFunc())# If you run this without the parameter you get the memory location of miltiply
#  
#<function returnFunc.<locals>.multiply at 0x0000018899300948>
#same as
print(returnFunc()(4))

def returnLam(b,c):
    return lambda x,a: x + a + b + c

#calling lambda function inside of another function
r = returnLam(4,5) # without the brackets yuo get the memoty location returned to you
print(r(5,5))
<function multiply_test at 0x00000181E95A2168>
Help on function multiply_test in module __main__:

multiply_test(num)
    #returning a lam function from a function

None
8
19
If Statements within Lambdas
In [6]:
#lambda x: True if (condition) else False

#first part ttue if the condition is true, otherwise false
f = lambda num : num *2 if num > 10 else num + 2

#with an ifelse  
f = lambda num : num * 2 if num > 10 else num + 2  if num > 12 else num + 3 

print(f(8))

print(f(10))

print(f(12))
11
13
24
In-Class Exercise #1
Write an anonymous function that cubes the arguments passed in and assign the anonymous function to a variable 'f'.

In [7]:
#(keyword lambda) (one or more inputs) (colon) (function to be executed)

f = lambda x : x**3
print (f(3))
27
Map
The map function allows you to iterate over an entire list while running a function on each item of the list. This is why the map function works well with lambda's, because it simplifies things and you write less lines of code.
The syntax for a map function is "map(function to be used, list to be used)"
However, you must be careful, as the map function returns a map object, not a list. To turn it into a list we use the list() type conversion.

Syntax
In [8]:
#map(function to be used, list to be used or interable (list, dict, tuple,set))"
#normally the usage of map haappend witha pre-s=definrf funvtuon---but we can use lambdas as well

# instead of running through two for loops
def squared(num, num2):
    if num < 10 and num2 <10:
        return num**2, num2** 2
    else:
        return num,num2
# this only works if the lists are the same size because of the AND statement    
more_nums = [4,10,3,2,6]


##RUN THIS THROUGH PYTHON TUTOR GREAT VISUALIZATION link in slack

squared_nums_map = list(map(squared,more_nums, numbers))
print(squared_nums_map, numbers)

#get a list of tuples back reading number from each list a t the same timer???
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-d7fac64c0c12> in <module>
     14 ##RUN THIS THROUGH PYTHON TUTOR GREAT VISUALIZATION link in slack
     15 
---> 16 squared_nums_map = list(map(squared,more_nums, numbers))
     17 print(squared_nums_map, numbers)
     18 

NameError: name 'numbers' is not defined
Using Lambda's with Map
In [ ]:
#Syntax map(lambda x: x+2, list)
#using lambda in map happens in line (or inone lime usuallu)
#list(map(lambda x : x *2, nums))
#map bcaicall ineterates theoh the list like a for loop
numbers = [4,11,20,3,15]

squared_nums = list(map(lambda x : x **2 if x < 10 else x, numbers))
print(squared_nums)
In-Class Exercise #2
Use the map function to double each number and minus it by one in the list by using a lambda function

In [ ]:
#reg function
def double_nums(num):
    num = num*2 - 1
    return num

nums = [4,2,6,8]
double_nums_map = list(map(double_nums,nums))
print(double_nums_map)


# lambda function
double_nums = list(map(lambda x: x * 2 - 1, nums))
print(double_nums)
Filter()
Filter's are similar to the map function, where you're able to pass a function argument and a list argument and filter out something from the list based on the conditions passed. Similar to the map function, it returns a filter object, so you need to type convert it to a list()

Syntax
In [ ]:
# #Filter's are similar to the map function, where you're able to pass a function argument
# and a list argument and filter out something from the list based on the conditions passed.
# Similar to the map function, it returns a filter object, so you need to type convert it to a list()

names = ['Bob', 'Andy', 'Max', 'Evan', 'Anjelica']
def a_names (name):
    if name[0].lower() =='a':
        return True
    else:
        return False
    
new_names_list = list(filter(a_names, names))
print(new_names_list)
Using Lambda's with Filter()
In [ ]:
new_names_lamb = list(filter(lambda name: True if name[0].lower() == 'a' else False, names))
print(new_names_lamb)
In-Class Exercise #3
Filter out all the numbers that are below the mean of the list.
Hint: Import the 'statistics' module

In [5]:
from statistics import mean

nums = [2,7,4.2,1.6,9,4.4,4.9]
def below_mean(num):
    if num < mean(nums):
        #nums.remove(num[0])
        return True
    else:
        return False
        
new_nums_list = list(filter(below_mean, nums))
print(new_nums_list)

#print(mean(nums))
below_avg= list(filter(lambda x: True if x <= 4.72 else False, nums))
print(below_avg)
[2, 4.2, 1.6, 4.4]
[2, 4.2, 1.6, 4.4]
Reduce()
Be very careful when using this function, as of Python 3 it's been moved to the 'functools' library and no longer is a built-in function.
The creator of Python himself, says to just use a for loop instead.

Syntax
In [88]:
from functools import reduce

#reduce(function ,iterable) #it iterates throught the list 
list_1 = [2,4,6,8,10]
def subtractNums(num1,num2):
    return num1 - num2

result = reduce(subtractNums, list_1)
print(result)
    
def addNums(num1, num2):
    return num1 + num2

result_add = reduce(addNums, list_1)
print(result_add)
-26
30
Using Lambda's with Reduce()
In [ ]:
from functools import reduce
result_lam = reduce(lambda x,y : x+ y, list_1)
print(result_lam)
In-Class Exercise #4
Use the reduce function to multiply the numbers in the list below together with a lambda function.

In [87]:
from functools import reduce
my_list = [1,2,3,4]

def multiplyNums(num1,num2):
    return num1 * num2
result = reduce(multiplyNums, my_list)
print(result)


result_lam = reduce(lambda x,y : x * y, my_list)
print(result_lam)
24
24
Recursion
Recursion means that a function is calling itself, so it contanstly executes until a base case is reached. It will then push the returning values back up the chain until the function is complete. A prime example of recursion is computing factorials... such that 5! (factorial) is 5*4*3*2*1 which equals 120.

Implementing a Base Case
In [ ]:
#Recursion means that a function is calling itself
#A prime example of recursion is computing factorials... such that 5! (factorial) is 5*4*3*2*1 which equals 120.

def addNums(num):
    # set base case here
    if num <= 1:
        print ("addNums(1) = 1")
        return num
    else:
        print(f"addNums({num}) = {num} + addNums({num-1})") # prints out the values that are being passed into the function       
        return num + addNums(num-1)#once we hit the basecase , num<=1 , we starting adding the numbers up starting
                                   #at 1 and going up
                                

addNums(5)
Writing a Factorial Function
In [ ]:
# 5! = 5 *4*3*2*1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
    
factorial(5)
In-Class Exercise #5
Write a recursive function that subtracts all numbers to the argument given.

In [ ]:
# # 5! = 5 *4*3*2*1
# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# factorial(5)


##RUN THIS TROUGH PYTHON TUTOR
def subtraction(num):
    if num <= 1:
        return 1
    else:
        return num - subtraction(num-1)
    
subtraction(10)
Generators
Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops. They are created using functions and the yield statement.

Yield Keyword
The yield keyword denotes a generator, it doesn't return so it won't leave the function and reset all variables in the function scope, instead it yields the number back to the caller.

In [9]:
#Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops.
#They are created using functions and the yield statement.The yield keyword denotes a generator, it doesn't return so it won't leave the function
#and reset all variables in the function scope, instead it yields the number back to the caller.


#under the hood is the yole d gining up the print out
def my_range(stop, start, step = 1):
    while start < stop:
        yield start
        start += step
for i in my_range(20, start = 2):
    print(i)
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
Infinite Generator
In [ ]:
# bad, never create infinite loops
In-Class Exercise #6
Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.

In [6]:
# #under the hood is the yole d gining up the print out
# def my_range(stop, start, step = 1):
#     while start < stop:
#         yield start
#         start += step # without this you could have an infinite loop ALWAYS INCREMENT
#                         # AFTER YOUR YIELD
# for i in my_range(20, start = 2):
#     print(i) 
    
##USE THIS FORMAT < BEST WAY TO NOT GET INFINIT LOOP    
def squared(stop,start,step = 1):
    while start <= stop:
        yield start
        start += step

for i in squared(10, start = 1):
    print(i**2)
1
4
9
16
25
36
49
64
81
100
Exercises
Exercise #1
Filter out all of the empty strings from the list below

Output: ['Argentina', 'San Diego', 'Boston', 'New York']

In [31]:
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

# Filter's are similar to the map function, where you're able to pass a function argument 
# and a list argument and filter out something from the list based on the conditions passed.
# Similar to the map function, it returns a filter object, so you need to type convert it to a list()
# you end up with just the values where the condition executes to True

# def non_empty(place):  

#     if place.strip() != "": #append pnly places that are not empty strings
#         return True
#     else:
#         False
# new_places_list = list(filter(non_empty,places))
# print(new_places_list)


new_places_list = list(filter(lambda place: True if place.strip() != "" else False, places))
print(new_places_list)
['Argentina', 'San Diego', 'Boston', 'New York']
Exercise #2
Write an anonymous function that sorts this list by the last name...
Hint: Use the ".sort()" method and access the key"

Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

In [105]:
#THE SORT METHOD SORTS UPPERCASE  FIRST THEN SORTS THE LOWERCASE AFTER

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
sorted_list = sorted(authors, key=lambda x: x.lower().split()[-1])
print(sorted_list)
['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
Exercise #3
Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

In [104]:
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

def convert_Temp(place):
    far_temp= (9/5) * place[1] + 32
    return place[0],far_temp
convert_temp_map = list(map(convert_Temp,places))
print(convert_temp_map)


convert_temp = list(map(lambda x: (x[0], (9/5) * x[1] + 32), places ))
print(convert_temp)
[('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
[('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
Exercise #4
Write a recursion function to perform the fibonacci sequence up to the number passed in.

Output for fib(5) => 
Iteration 0: 1
Iteration 1: 1
Iteration 2: 2
Iteration 3: 3
Iteration 4: 5
Iteration 5: 8

In [133]:
#wikipedia definition F{n}=F{n-1}+F{n-2} for n > 2


def fibonacci(num):
    if num <= 2:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
print(fibonacci(7))
21