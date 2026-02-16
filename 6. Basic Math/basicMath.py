import random

def addition(a,b):
    return a + b

def sous(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

operation = random.choice(['+', '-', '*'])
nb1 = random.randint(1,10)
nb2 = random.randint(1,10)

print(f"Nombre 1 : {nb1}")
print(f"Nombre 2 : {nb2}")
print(f"Opération : {operation}")

if operation == "+":
    print(f"Somme = {addition(nb1,nb2)}")
elif operation == "-":
    print(f"Reste = {sous(nb1,nb2)}")
else:
    print(f"Produit = {mult(nb1,nb2)}")