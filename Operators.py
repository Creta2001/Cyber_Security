# 1. Write a function for arithmetic operators(+,-,*,/)
def arithmetic(a,b):
    sum = float(a) + float(b)
    diff =float(a) - float(b)
    mul = float(a) * float(b)
    div = float(a) / float(b)
    print("Sum of Two numbers is: ",sum)
    print("Difference of two numbers is : ",diff)
    print("Product of two numbers is : ",mul)
    print("Division of two numbers is :",div)
arithmetic(7,3)


# 2. Write a method for increment and decrement operators(++, --)
a = 0
a+=1
a=a+1
print("The value of a is",a)
print("Incremental ++\n")
for i in range (0,5):
    print(i)
for i in range(5,0,-1):
    print(i)

# 3. Write a program to find the two numbers equal or not.
aa=int(input("Enter the 1st Number:"))
bb=int(input("Enter the 2nd Number:"))
if aa==bb:
    print("Both Numbers are Equal.")
else:
    print("Numbers are Not Equal.")


# 4. Program for relational operators (<,<==, >, >==)
ra = 11
rb = 23
print(ra < rb)  #This operator(<) returns True if the left operand is less than the right operand.
print(ra <= rb) #This operator(<=)returns True if the left operand is less than or equal to the right operand.
print(ra > rb)  #This operator(>) returns True if the left operand is greater than the right operand.
print(ra >= rb) #This operator(>=)returns True if the left operand is greater than or equal to the right operand.   
print(ra == rb) #This operator(==)returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.
print(ra != rb) #This operator(!=)returns True if both the operands are not equal.


# 5. Print the smaller and larger number
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
if num1>num2:
    print(f'{num1} is larger')
else:
    print(f'{num2} is larger')
if num1<num2:
    print(f'{num1} is smaller')
else:
    print(f'{num2} is smaller')