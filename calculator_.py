def calculator(a,b,Operator):
      
    if (Operator == "+"):
        print("The addition of two numbers is : ",a + b)
    elif (Operator == "-"):
        print("The Subtraction of two numbers is : ",a - b)
    elif (Operator == "*"):
        print("The Multiplication of two numbers is : ",a * b)
    elif (Operator == "/"):
        print("The Division of two numbers is : ",a / b)
    elif (Operator == "%"):
        print("The Remainder of a numbers is : ",a % b)

    if Operator in op:
        return 1
    else:
        print("Try Again!!! , you entered a invaid operator")    


op = {"+","-","*","/","%"}
Operator = input("Enter a operator :")
a = int(input("Enter a first no : "))
b = int(input("Enter a second no : "))
Choice = int(input("Enter a choice : "))
print("1.Enter for Addition")
print("2.Enter for Subtraction")
print("3.Enter for Multiplication")
print("4.Enter for Division")
print("5.Enter for Remainder")
calculator(a,b,Operator)