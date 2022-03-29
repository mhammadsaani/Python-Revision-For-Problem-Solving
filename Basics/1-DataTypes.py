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