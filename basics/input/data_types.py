#name
print("What us your name human?")
name = input()
print()
print("How old are you (in years)?")
age = int(input())
print()
print("How tall are you (in meters)?")
height = float(input())
print()
print("How much do you weigh (in kilograms)?")
weight = float(input())
bmi =  weight / height**2
print(f"{name} you are {age} years old and your bmi is {bmi:.2f}.")
