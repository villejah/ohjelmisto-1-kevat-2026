numbers = []
user_input = "start"

while user_input != "":
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input != "":
        number = float(user_input)
        numbers.append(number)

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")
