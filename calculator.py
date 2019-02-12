#Calculator

print("Welcome to the calculator.")
first_number = input("First number: ")
operand = input("Operand, +, -, *, or /: ")
second_number = input("Second number: ")

if operand == "+":
    print(int(first_number) + int(second_number))
elif operand == "-":
    print(int(first_number) - int(second_number))
elif operand == "*":
    print(int(first_number) * int(second_number))
elif operand == "/":
    print((round(int(first_number) / int(second_number))))