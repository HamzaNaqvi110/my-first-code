
num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))

operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print ("Result:", result)

else:
    print("Invalid operator")