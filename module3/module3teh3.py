gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")
