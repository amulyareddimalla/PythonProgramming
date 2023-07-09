'''num1=input("Enter a number: ")
num2=input("Enter another number: ")
result=float(num1)+float(num2)
print(result)'''

#intermediate calculator
n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
op=input("Enter operator you want to use: ")

if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("Invalid Operator")