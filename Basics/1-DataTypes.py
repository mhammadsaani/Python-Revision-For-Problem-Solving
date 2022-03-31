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


