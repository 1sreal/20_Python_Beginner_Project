def add(a, b):
    result = a + b
    print(str(a)+"+"+str(b)+"="+str(result))

def sub(a,b):
    result = a - b
    print(str(a)+"+"+str(b)+"="+str(result))

def mul(a,b):
    result = a * b
    print(str(a)+"+"+str(b)+"="+str(result))

def div(a, b):
    result = a / b
    print(str(a)+"+"+str(b)+"="+str(result))

print(" A. Addition\n B. Subtaction\n C. Multiplication\n D. Division\n E. Exit\n")
choice = input("Which operation are we performing today?\n")
if (choice.lower()) == a:
    print("Addition")
    a = int(input("First number: "))
    b = int(input("Second numer: "))
    add(a,b)
elif (choice.lower()) == b:
    print("Subtraction")
    a = int(input("First number: "))
    b = int(input("Second numer: "))
    sub(a,b)
elif (choice.lower()) == c:
    print("Multiplication")
    a = int(input("First number: "))
    b = int(input("Second numer: "))
    mul(a,b)
elif (choice.lower()) == d:
    print("Division")
    a = int(input("First number: "))
    b = int(input("Second numer: "))
    div(a,b)
elif (choice.lower()) == e:
    print("Thanks for your time.")
