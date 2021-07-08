



def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2




number1=int(input("Enter first number: "))
print(f"+ \n- \n* \n/")
operator=input("Enter operator: ")
number2=int(input("Enter second number: "))
if operator=="+":
    print("Addition =:",add(n1=number1,n2=number2))
if operator=="-":
    print("Subtraction =:",sub(n1=number1,n2=number2))
if operator=="*":
    print("Multiplication =:",mul(n1=number1,n2=number2))
if operator=="/":
    ("Division =:",div(n1=number1,n2=number2))