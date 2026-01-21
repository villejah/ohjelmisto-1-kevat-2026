talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

grams_per_lot = 13.3
lots_per_pounds = 32
pounds_per_talent = 20

total_grams = (talents * pounds_per_talent * lots_per_pounds * grams_per_lot
               + pounds * lots_per_pounds * grams_per_lot + lots * grams_per_lot)
kilograms = int(total_grams // 1000)
remaining_grams = round(total_grams % 1000, 2)

print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams} grams.")
