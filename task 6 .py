## printing first command (hello world):

print("Hello, World!")

## Printing Variables:

name = "sahil"
age = 24
print("Name:", name)
print("Age:", age)

## Formatting Strings (f-strings):

name = "sahil"
age = 24
print(f"Name: {name}, Age: {age}")

## Concatenating Strings:

name = "sahil"
age = 35
print("Name: " + name + ", Age: " + str(age))

## Using Format Specifiers:

name = "rahul dravid"
age = 40
print("Name: {}, Age: {}".format(name, age))

##Printing Multiple Items:

a = 10
b = 20
c = 30
print(a, b, c)

## while loop func

i=1
while(i<=3):
        print('hello')
        i=i+1

## for loop func

for x in 'sahil':
        print(x)

## range func

for x in range(5):
        print(x)


## increment func

for x in range (1,9,2):
        print(x)

## decrement func

for x in range (9,1,-2):
        print(x)

##  if else loop func

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

## variable types:-
##int func
x = 5
print(x)

## float func
y = 3.14
print(y)

## string func
name = "sahil"
print(name)

##boolean 
is_active = True
print(is_active)

##list func
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  

## count func(tuple)
my_tuple = (1, 2, 2, 3, 2, 4)
count = my_tuple.count(2)
print(count)  

##Single-line Comments:


# This is a single-line comment


##Multi-line Comments (Docstrings):

'''
This is a multi-line comment or docstring.
It can be used to provide detailed explanations.
'''
## data types

x = 42
print(type(x))  

y = "Hello"
print(type(y))  

z = [1, 2, 3]
print(isinstance(z, list)) 

##string methods

s = "hello world"
print(s.capitalize())  # Output: "Hello world"

##str upper and lower func

s = "Hello World"
print(s.upper())  
print(s.lower())  

## parameter & parameters

def greet(name="sahil"):
    print(f"Hello, {name}!")

greet() 
greet("sahil")  

def add_numbers(x, y):
    result = x + y
    return result

sum_result = add_numbers(3, 5)
print(sum_result)  


