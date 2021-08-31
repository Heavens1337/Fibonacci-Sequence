print("Welcome! This program takes an input and runs through "
      "the Fibonacci Sequence up to the input without exceeding it.")

limit = input("Please input your desired limit --> ")

current_number = 3

preceding_number_one = 1
preceding_number_two = 2


print("Current number: 1")
print("Current number: 2")

while current_number <= int(limit):
    current_number = preceding_number_one + preceding_number_two
    preceding_number_one = preceding_number_two
    preceding_number_two = current_number
    print(current_number)

print("The numbers have reached the point where if the program were to continue, it would "
      "\ngo over your defined limit.")
