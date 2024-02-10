import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero :/"
    else:
            return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot compute the square root of a negative number."
    else:
        return math.sqrt(x)
    
def modulus(x, y):
    if y == 0:
        return "Cannot compute the modulus dividing by zero."
    else:
        return x % y
        
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Modulus")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if choice in ('1', '2', '3', '4', '5', '7'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice == '6':
            num = float(input("Enter number: "))
        
        
        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", divide(num1, num2))
        elif choice == '5':
            print("Result: ", exponentiate(num1, num2))
        elif choice == '6':
            print("Result: ", square_root(num))
        elif choice == '7':
            print("Result: ", modulus(num1, num2))

    break
else:
    print("Invalid Input")