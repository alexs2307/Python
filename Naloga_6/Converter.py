print("Hi this is a Ninja converter")

while True:
    print("Please enter a number of miles that you'd like to convert into kilometers. Enter only a number!")
    miles = float(input("miles:"))
    convert_ratio = 0.62137
    kilometers = miles / convert_ratio
    print(miles, "mi are:\n", kilometers, "km")
    choice = input("Would you like to convert again? (y/n):")
    if choice.lower() != "y" and choice.lower() != "yes":
        break
print("Thank you for using our Ninja converter ")
