def add(n1, n2):
    return n1 + n2  

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(add(10, 5))     
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

n1 = float(input("Enter first number: "))
keep_going = True
while keep_going:
    operation = input("Enter operation (+, -, *, /): ")
    n2 = float(input("Enter second number: "))

    if operation == "+":
        result = add(n1, n2)
    elif operation == "-":
        result = subtract(n1, n2)
    elif operation == "*":
        result = multiply(n1, n2)
    elif operation == "/":
        result = divide(n1, n2)
    else:
        print("Invalid operation")
        continue

    print(f"{n1} {operation} {n2} = {result}")

    choice = input("Type 'y' to continue calculating with the result, or 'n' to start a new calculation: ")
    if choice == "y":
        n1 = result
    else:
        keep_going = False
        n1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        