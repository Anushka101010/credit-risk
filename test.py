print ("hello")
print ("in this program I will add two numbers")
a = "hello"
print (a)
even_num = "2"
print (even_num)

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

# implicit typecasting
a = 367 
b = 364.8
print (type(a))
print (type(b))
c = a/b
print (c)
print (type(c))

# explicit typecasting
a = "479"
b = 54.66
print (type(a))
print (type(b))
a = int(a)
print ("after conversion",type(a))
c = a+b
print (c)
print (type(c))

# exercises practice
# write a program to display a person's name, age and address in three different lines.
name = "anushka"
age = "22"
address = "654 lake street"
print (name)
print (age)
print (address)

# write a program to swap two variables
method 1
x = 12
y = 13
temp = x
print (temp)
x = y
print (x)
y = temp
print (y)
print ("value of x is",x)
print ("value of y is",y)

# method 2
a = 30
b = 40
# left,right = right,left
a,b = b,a
print (b)
print (a)

# write a program to convert float into integer
a = 438.57
print (type(a))
a = int(a)
print ("after conversion",type(a))
print (a) 

# write a program to take details from a student for ID-Card and then print it in different lines
name = input("type your name here: ")
grade = input("enter the grade of the student: ")
age = int(input("enter the age of the student: "))
email = input("enter the email of the student: ")
ph_no = input ("enter the ph_no here: ")
print ("Student Identity Card")
print ("name: ",name)
print ("grade: ",grade)
print ("age: ",age)
print ("email: ",email)
print ("ph_no: ",ph_no)

#write a program to take on user input as integer and then convert it to float.
a = int(input("enter a number here: "))
print (a)
print (type(a))
a = float(a)
print ("after conversion",a)
print (type(a))





