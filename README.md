# tech201_functions
tech201_functions

# Functions

### D R Y
### Don't Repeat Yourself

we embed functions in a code to make them reusable

how to write a function
define a function and then the function name
the colon says that the print statement is linked to the function
```python
def print_something():
    print("Something has been printed")
# outside the function you have to call print_something to get it to do what we want
print_something()
```

this function has no arguments it just prints out a string
we want to use arguments to make the function more usefully
```python
def print_something(print_string):
     print(print_string)
print_something("this is my variable")

print_something("this is the second time i called this function")
```
#### In Java: we use
#### public void print_string(string_text)

name your arguments clearly so that it gives context to what you want
```python
def greetings(name):
     print("Hello, my name is " + name)

greetings("Luke")
greetings("Ahimba")
greetings("John")
greetings("Sally")
```
# The return statement
the functions go blue once we start to use/ call them
```python
def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))
```
# Default arguments
we can overwrite the default arguments in the print statements at the end  
```python
def addition(int1=2, int2=5):
    return int2 + int2

print(addition())
print(addition(10, 10))
print(addition()) # this just shows that the previous line doesn't replace default values in the code unless declared
```
# Multiple arguments
this creates a tuple the star means i can have as many arguments inside function
```python
def multi_args(*multiargs):
     print(type(multiargs))
# for reach element in the tuple we have created, print it out
     for arg in multiargs:
         print(arg) # print each argument
multi_args(1, 2, 3, 4, 5, 6)

   ```

# Type Hints
they will tell us if something is not right with the code
eg. (name: str):, or (num: int):
```python


def greeting(name: str):
    print("Hello, my name is " + name)

greeting(29992) # this causes an error because it is an int but the type hint limits it to a string
```

# this will return the type of the output
```python
def division(num1: int, num2: int) -> float: # type hint for return float
    return num1 / num2

print(type(division(4, 53)))
```

# division
```python
def division(num1: int = 5, num2: int = 2) -> float: # type hint for return float
     return num1 / num2

print(division())
```
# Function best practices

* Name your functions clearly using lower case and underscores  
* All arguments should be clear in their need and where possible include their expected type  
* Remember the return statement or your function will return none  
* Keep things small to preserve readability and simplicity  
* Use comments in your functions/methods to give instructions on how to use them  
* Consider using type hints to avoid type errors when you run your code   

# A Simple Calculator
```python
def addition(num1: int, num2: int) -> float:
    return num1 + num2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(addition(num1, num2))
```
```python
def subtraction(num1: int, num2: int) -> float:
    return num1 - num2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(subtraction(num1, num2))
```
```python
def multiplication(num1: int, num2: int) -> float:
    return num1 * num2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(multiplication(num1, num2))
```
```python
def division(num1: int, num2: int) -> float: 
    return num1 / num2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(division(num1, num2))
```

# Convert Values
```python
def convert(num1, num2: float = 100) -> float:
    return num1 / num2
num1 = int(input("Enter the number of centemetres you would like to convert to metres: "))
num2 = 100
print("Your converted value is")
print(convert(num1, num2))


num1 = int(input("Enter the number of metres you would like to convert to feet: "))
num2 = 3.280839895
print("Your converted value is")
print(convert(num1, num2))
```