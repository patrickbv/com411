print("Program Started!")
print()
print("Please enter an ASCII code:")
code = int(input())
print()
if code >= 32 and code <= 126:
    print(f"The character represented by the ASCII value {code} is {chr(code)}")
else:
    print("The character cannot be displayed")
print()
print("Program Ended!")