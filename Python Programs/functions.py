'''
#functions
def func():
    print("It's a function")
func()
def func1(n1,n2):
    print("Num1=",n1,"Num2=",n2)
func1(10,20)
def func2(n1,n2):
    return n1+n2
print("value returned",func2(10,20.2))
def func3(n1,n2):
    n3=float(n1)+n2
    return n3
print("value returned",func3('10',20.2))
'''
'''
#1 positional arguments
def func1(n1,n2,n3,n4):
    print("Num1=",n1,"Num2=",n2,"Num3=",n3,"Num4=",n4)
func1(1,2,3,4)
'''
'''
#2 keyword arguments
def func2(n1,n2,n3,n4):
    print("Num1=",n1,"Num2=",n2,"Num3=",n3,"Num4=",n4)
func2(n4=1,n1=2,n2=3,n3=4)
'''
#3 default arguments
def func3(collegename="GIETU",name,rollno,branch):
    print(name,rollno,branch,collegename)
func3("Prateek",6,"CST","CST")

'''
#4 Variable number of arguments
def func4(*var):
    for i in var:
        print(i,end=' ')
func4(10,20,30)
print()
func4(10,20,30,40,50)
print()
func4(10,20,30,60.9,70.8,60)
print()
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return sum1
print(add(10,20,30))
print(add(10,20,30,40,50))
print(add(10,20,30,60.9,70.8,60))
'''


    


