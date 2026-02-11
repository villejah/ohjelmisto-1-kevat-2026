import random
dice_count = int(input("How many dice to roll: "))

total = 0

for _ in range(dice_count):
    roll = random.randint(1, 6)
    total += roll

print(f"Sum of the dice: {total}")