# Conversion  utility problem

def GetInput():
    Number = ""
    DNumber = 0
    ValidInput = False
    # Validation
    while (not ValidInput): # EXAMPLE OF CONDITION-CONTROLLED ITERATION
        Number = input(": ")
        # Type check - no input is valid
        if (Number == ""):
            ValidInput = True
        elif Number.isnumeric():
            ValidInput = True
            DNumber = int(Number)
        if (ValidInput == False):
            print("Invalid input.")
    return DNumber


# Subroutine to convert feet to inches
def FeetToInches(Feet):
    Inches = Feet * 12
    return Inches


# Subroutine to convert inches to feet
def InchesToFeet(Inches):
    Feet = Inches / 12
    return Feet


# Subroutine to offer the conversion choice to the user
def Menu():
    MenuChoice = 0
    # Iterate until quit is chosen
    while (MenuChoice != 3):
        print("1. Feet to inches")
        print("2. Inches to feet")
        print("3. Quit")
        MenuChoice = GetInput()
        # Action menu choice
        if (MenuChoice == 1):
            print("Enter value for feet")

            Feet = GetInput()
            Convert = FeetToInches(Feet)

            print(f"{Feet} inches equals {Convert} feet")
        elif (MenuChoice == 2):
            print("Enter value for inches")
            Inches = GetInput()
            Convert = InchesToFeet(Inches)

            print(f"{Inches} inches equals {Convert} feet")
        elif (MenuChoice == 3):
            print("Goodbye.")
        else:
            print("Invalid input.")
        print("-------------------------")


# Main program
Menu()