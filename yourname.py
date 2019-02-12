#String Interpolation


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Thanks! Your name is " + first_name + " " + last_name)
full_name = (f"Or, interpolated, your name is {first_name} {last_name}")
print(full_name)