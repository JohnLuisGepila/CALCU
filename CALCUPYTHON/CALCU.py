#CREATE A SIMPLE PYTHOM CALCU

print("Select an operators: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLICATION")
print("4. DIVIDE")

operator = input()

if operator == "1": 
    num1 = input("ENTER A NUMBER: ")
    num2 = input("ENTER THE SECOND NUMBER: ")
    print("The sum is " + str(float(num1) + float(num2)))

elif operator == "2":
    num1 = input("ENTER A NUMBER: ")
    num2 = input("ENTER THE SECOND NUMER: ")
    print("The difference is " + str(float(num1) - float(num2)))


elif  operator == "3":
    num1 = input("ENTER A NUMBER: ")   
    num2 = input("ENTER THE SECOND NUMBER: ")
    print("The product is " + str(float(num1) * float(num2)))

elif operator == "4":
    num1 = input("ENTER A NUMBER: ")   
    num2 = input("ENTER THE SECOND NUMBER: ")
    print("The result is " + str(float(num1) / float(num2)))

else:
    print("ERROR")    