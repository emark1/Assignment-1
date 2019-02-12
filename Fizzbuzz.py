#Fizz Buzz

number = input("Please enter a number: ")

if int(number) % 3 == 0 and int(number) % 5 == 0:
    print("Fizzbuzz!")
elif int(number) % 5 == 0:
    print("Buzz")
elif int(number) % 3 == 0:
    print("Fizz")