#Tip Calculator

print("Welcome to the tip calculator.")
bill_amount = input("Bill amount: ")
tip_percentage = input("Desired tip percentage: ")

def calculate_tip(bill,percentage):
    tip_percentage = float(percentage) / 100
    tip_amount = float(bill) * float(tip_percentage)
    return tip_amount

def print_tip_amount(tip_amount):
    print("You should tip $" + str(tip_amount))

tip = calculate_tip(bill_amount,tip_percentage)
print_tip_amount(tip)