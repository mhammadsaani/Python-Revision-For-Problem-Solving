# Numbers

# - Integers
a = 5
print(type(a))\

# - Floats
b = 3.45
print(type(b))

# Complex
c = complex(2, 3)
print(c)
print(type(c))


# Boolean
f_bool = False
print(type(f_bool))

t_bool = True
print(type(t_bool))


# String 

singleQuote = 'Hey, I am Single Quote'
doubleQuote = "Hey, I am Double Quote"
tripleQuote = """Hey, I am triple Quote"""
char = '$'
print(singleQuote, doubleQuote, tripleQuote, char)

print(len(singleQuote))
print("Hey , I am 5th index in singleQuote", singleQuote[5])


# Immutibility

# singleQuote[0] = 'B' # This will give an error
# print(singleQuote)

# Assigning a completely new value to a string does not mean that you have modified the value

print("ID before " , id(singleQuote))
singleQuote = "Hey, I am updated Value"
print("ID after reassinging ", id(singleQuote))


# In Python 3.x, all strings are unicode. But, older versions of Python (Python 2.x) support only ASCII characters. To use unicode in Python 2.x, preceding the string with a # u is must. For example:

string = u"This is unicode"
print(string)


# NoneType

val = None
print(val)
print(type(val))

# Important things about None
# None is not a default value for the variable that has not yet been assigned a value.
# None is not the same as False.
# None is not an empty string.
# None is not 0


### String Formatter %s is used

string = 'Formating'
print("Hey, this is a test %s" %string)

print("Hey this is simple string %s" %"formating")

print("Testing both ways %s and %s" %('way1', string))

# Inserting Integers %i is used

print("%i + %i" %(2, 3))


# Inserting float %f is used, %.2f is used to limit to 2 zeros


print("%.2f + %.2f" %(2.3, 5.3))

### Important, When two strings have more values, string which comes first in dictionary has smaller value


# Conditional

num = 5
if (num == 5):
  print("Hey")
else:
  print("Bye")



# def calculator(operation, n1, n2):
#     return operation(n1, n2)  # Using the 'operation' argument as a function


# # 10 and 20 are the arguments.
# result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# # The lambda multiplies them.
# print(result)

# print(calculator(lambda n1, n2: n1 + n2, 10, 20))


# operation = lambda n1, n2: n1*n2

# print(operation(10, 20))

# def calculator(operation, n1, n2):
#   return operation(n1, n2)


# print(calculator(operation, 10, 20))


# llist = [1, 2, 3, 4, 5]

# doubleList = map(lambda n: n * 2, llist)
# print(list(doubleList))

# greaterThree = list(filter(lambda n: n > 2, llist))
# print(greaterThree)


# def factorial(n):
#     if (n == 2):
#         return 2
#     return n * factorial(n-1)

# print(factorial(5))

# x = [1, 2, 3, 4]
# for i in range(len(x)):
#   print(x[i])


# for i in x:
#   print(i)


# def fib(n):
#   if n < 3:
#     return 1
#   fristNum = 0
#   secondNum = 1
#   finalAns = 0
#   for i in range(n - 2):
#     temp = fristNum + secondNum
#     fristNum = secondNum
#     secondNum = temp
#     finalAns = temp
#   return finalAns


### lists .extent(), range()

a = [1, 2, 3]
a.sort()


# List Comprehension : List comprehension is a technique that uses a for loop and a condition to create a new list from an existing one.

# Expression For Loop and Condition 

test = [1, 2, 3]
test2 = [4, 5, 6]

doubleList = [i * 2 for i in test if i == 4]
print(doubleList)
test3 = [(n1, n2) for n1 in test for n2 in test2 if (n1+n2)%2 != 0]

print(test3)


### Tuple

a = ("Hey", 1)
print(type(a))

### Dictionary

dictionary = {1: 1, 
2: 2}
print(dictionary)

dict()