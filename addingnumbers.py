#Adding two numbers

print("Hello. We will add two numbers together.")
first_number = input("Please enter the first number: ")
second_number = input("Thank you. Please enter the second number: ")

def show_answer(no1,no2,answer):
    print(f"{no1} plus {no2} is {answer}")

def add_numbers(no1,no2):
    answer = int(no1) + int(no2)
    return answer

answer = add_numbers(first_number,second_number)
show_answer(first_number,second_number,answer)