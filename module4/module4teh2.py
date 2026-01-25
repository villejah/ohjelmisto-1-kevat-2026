inches = 0
while inches >= 0:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches >= 0:
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters:.2f} centimeters")
print("Program ended.")