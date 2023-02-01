# Functions

# D R Y
# Don't Repeat Yourself

# # we embed functions in a code to make them reusable

# how to write a function
# define a function and then the function name
# the colon says that the print statement is linked to the function

# def print_something():
#     print("Something has been printed")
# # outside of the function you have to call print_something to get it to do what we want
# print_something()


# this function has no arguments it just prints out a string
# we want to use arguments to make the function more usefully

# def print_something(print_string):
#     print(print_string)
# print_something("this is my variable")
#
# print_something("this is the second time i called this function")

# In Java:
# public void print_string(string_text)

# name your arguments clearly so that it gives context to what you want

# def greetings(name):
#     print("Hello, my name is " + name)
#
# greetings("Luke")
# greetings("Ahimba")
# greetings("John")
# greetings("Sally")

# The return statement
# the functions go blue once we start to use/ call them
# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))

# Default arguments
# we can overwrite the default arguments in the print statements at the end
# def addition(int1=2, int2=5):
#     return int2 + int2
#
# print(addition())
# print(addition(10, 10))
# print(addition())

# Multiple arguments
# this creates a tuple the star means i can have as many arguments inside function
# def multi_args(*multiargs):
#     print(type(multiargs))
# # fo reach element in the tuple we have created, print it out
#     for arg in multiargs:
#         print(arg) # print each argument
# multi_args(1, 2, 3, 4, 5, 6)



# Type Hints
# they will tell us if something is not right with the code
# eg. (name: str):, or (num: int):
# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting(29992)

# this will return the type of the output
# def division(num1: int, num2: int) -> float: # type hint for return float
#     return num1 / num2
#
# print(type(division(4, 53)))

# division
# def division(num1: int = 5, num2: int = 2) -> float: # type hint for return float
#     return num1 / num2
#
# print(division())

# Function best practices

# Name your functions clearly using lower case and underscores
# all arguments should be clear in their need and where possible include their expected type
# remember the return statement or your function will return none
# keep things small to preserve readability and simplicity
# use comments in your functions/methods to give instructions on how to use them
# consider using type hints to avoid type errors when you run your code
