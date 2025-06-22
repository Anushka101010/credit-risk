# print ("hello")
# print ("in this program I will add two numbers")
# a = "hello"
# print (a)
# even_num = "2"
# print (even_num)

"""datatypes
1. text-type: string (str)
2. numeric: integer (int), floating point (float), complex
3. sequence-type: list, tuple, range
4. mapping-type: dictionaries (dict)
5. set-type: set, frozenset
6. boolean-type: bool
7. binary-types: bytes, bytearray, memoryview"""

name = input("Enter your name here:")
print (name)
age = int(input("enter age:"))
print (age)
height = float(input("what's your height?"))
print (height) 
exp1 = eval(input("enter your equation here:"))
print (exp1)

name = "john"
print (type(name))
exp3 = 5*4
print (type(exp3))

a = 367
b = 364.8
print (type(a))
print (type(b))
c = a/b
print (c)
print (type(c))