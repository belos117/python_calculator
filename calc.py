#!/bin/python3
#A simple calculator to perform an operation on two numbers
print ("Welcome to my simple calculator")                  
first_num = input ("Enter first number :")
second_num = input ("Enter second number :")
operation = input ("Choose the operation you want to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n:")

def addition():                                                
    add = int(first_num) + int(second_num)
    return add                                                                                                        
def subtraction():
    sub = int(first_num) - int(second_num)                     
    return sub

def multiplication():
    mul = int(first_num) * int(second_num)
    return mul                                             
def division():                                                
    div = int(first_num) / int(second_num)                     
    return div

if operation in ["1", "Addition"]:                             
    print ("The sum of " + first_num + " and " + second_num + " is " + str(addition()))
elif operation in ["2", "Subtraction"]:                        
    print ("The difference between " + first_num + " and " + second_num + " is " + str(subtraction()))
elif operation in ["3", "Multiplication"]:
    print ("The product of " + first_num + " and " + second_num + " is " + str(multiplication()))
elif operation in ["4", "Division"]:
    print ("The value of " + first_num + " divided by " + second_num + " is " + str(int(division())))
else:
    print ("Your Selection is invalid")