# Write a program to print your name.
print("Sachin Patel K")

# Write a program for a Single line comment 
# multi-line comments.
'''This is code for Multi Line Commenting 
Now a days, many crowdfunding platforms already exist and they take huge chunk of money from investors and contributes and leave them with empty promises. Crowdfunding using blockchain changes the traditional way to deal with business funding. Generally when people need to raise a cash to begin a business, they have to design strategy, statistical surveying, and models, and afterward present the thoughts around to attract people or organizations. These subsidizing sources included banks, angel investors'''

# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a = 10
b = True
c = 2.890
d = "Hello World"           
e = 'A'

print("Type of a =",type(a))
print("Value of b =",type(b))
print("Value of c =",type(c))
print("Value of d =",type(d))
print("Value of e =",type(e))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a = 10 
# This is Global Value
def a():
    print("Global Value of a is: ",a)
def b():
    a=5
    print("Local Value of a in function b is : ",a)
def c():
    a = 14
    print("Again th value of A is changed inside c function :",a)
print('global value of a: ',a)
a()
print('global value of a: ',a)
b()
print('global value of a: ',a)
c()


