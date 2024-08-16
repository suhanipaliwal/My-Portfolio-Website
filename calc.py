# Addition Function
def add(num1, num2):
    return num1 + num2
 
# Subtraction function
def subtract(num1, num2):
    return num1 - num2
 
# Multiplication function
def multiply(num1, num2):
    return num1 * num2
 
# Division Function
def divide(num1, num2):
    return num1 / num2
  
# User's input
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
 
print("Choose the operation you want to perform -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")

choice = int(input("Select the operation from 1, 2, 3, 4 :"))

if choice == 1:
    print(first, "+", second, "=",
                    add(first, second))
 
elif choice == 2:
    print(first, "-", second, "=",
                    subtract(first, second))
 
elif choice == 3:
    print(first, "*", second, "=",
                    multiply(first, second))
 
elif choice == 4:
    print(first, "/", second, "=",
                    divide(first, second))
else:
    print("Invalid input")
