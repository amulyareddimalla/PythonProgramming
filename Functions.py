'''def hello_user(name,age):
    print("hello " + name+  " you are " +str(age)+ "!")
#print("first result")
hello_user("Amulya",28)
#print("Third result")'''

'''def cube(num):
    return num*num*num
result=cube(5)
print(result)'''

def max_num(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3
print(max_num(999,99,9))

