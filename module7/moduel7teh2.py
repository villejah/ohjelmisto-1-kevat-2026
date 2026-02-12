names = set()

name = input("Enter a name: ")

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

    name = input("Enter a name: ")

print("All names entered:")
for n in names:
    print(n)
