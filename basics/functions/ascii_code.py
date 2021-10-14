print("Program Started!")
print()
print("Please enter a standard character:")
character = input()
print()
if  len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("One character only!")
print()
print("Program Ended!")
