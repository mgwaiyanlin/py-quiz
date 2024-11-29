# file = open("coffee-machine.txt")
# contents = file.read()

# print(contents)

with open("coffee-machine.txt", mode="w") as file:
    file.write("Writing new line...")
    print("Finished writing new line...")

