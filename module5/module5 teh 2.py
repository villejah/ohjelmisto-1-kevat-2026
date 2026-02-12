numbers = []

user_input = input("Enter a number: ")

while user_input != "":
    numbers.append(float(user_input))
    user_input = input("Enter a number: ")

numbers.sort(reverse=True)

print("The greatest numbers in descending order:")
for number in numbers[:5]:
    print(number)
