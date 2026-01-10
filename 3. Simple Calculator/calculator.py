#Simple Calculator

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

addition = num1 + num2
Soustraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"Addition : {num1 + num2}")
print(f"Soustraction : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")
print(f"Division : {num1 / num2}")