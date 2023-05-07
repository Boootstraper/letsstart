first = input("enter first number:")
first= int(first)
operator = input("enter operator (+,-,*,/) :")
second = input("enter second number:")
second = int(second)
if operator == "+":
    print(first + second)
if operator == "-":
    print(first - second)
if operator == "*":
    print(first * second)
else:
    print("invalid operation, plz try again")
