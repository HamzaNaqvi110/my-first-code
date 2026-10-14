a = int(input ("Enter your first number: "))
b = int (input ("Enter your second number: "))
operator = input ("Enter your opperator('+', '/', '*', '-'): ")
Result = a + b
if operator == "+":
    print ("Result:", Result)
elif operator == "-":
    Result = a - b
    print ("Result:", Result)   
elif operator == "*":
    Result = a * b
    print ("Result:", Result)
elif operator == "/":
    if b == 0:
        print ("Error:can't divide by zero")
    else:
        Result = a / b
        print ("Result:", Result)
else:
    print ("Invalid operator")