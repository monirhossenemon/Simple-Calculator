#Simple Calculator
def calculator(num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return  num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return " Can't divide by Zero"
    else:
        return "Invalid Operator"
        
#User Input
while True:
    try:
        num1 = float(input("Enter 1st number: ")) 
        num2 = float(input("Enter 2nd number: "))    
        op = input("Enter a operator(+,-,*,/): ")  
        result = calculator(num1,num2,op)
        print(" Result:",result)
        print()
    except ValueError:
        print( "Enter valid Number")
        print()
        
    choice = input("Continue?(Yes or No): ")    
    if choice.lower() != "yes":
        break
    print()
