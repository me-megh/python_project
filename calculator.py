print("Welcome biggner level project")
def adding(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

def display():
    print("1. adding")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    
def calculator():
    print("welcome to my calculator")
    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))
    display()
    choice=input("Enter which opreation you want to perform 1/2/3/4")
    if(choice == '1'):
        print(f"{num1}+{num2}={adding(num1,num2)}")
    elif(choice =="2"):
        print(f"{num1}-{num2}={subtract(num1,num2)}")
    elif(choice =="3"):
        print(f"{num1}*{num2}={multiply(num1,num2)}")
    elif(choice =="4"):
        print(f"{num1}/{num2}={divide(num1,num2)}")
    else:
        print("Invalid input! Please choose a valid operation.")
  
calculator()