# Midterm Project

print("Ola Umeh")
print("ogu1@miami.edu")
print("CSC 115")
print("Computer Science")


validProgramLoopInputs = ["yes", "Yes", "no", "No"]
programLoop = input("Do you want to begin the program? En ")

# Input validation for the variable validProgramLoopInputs
while programLoop not in validProgramLoopInputs:
    programLoop = input("Invalid input. Do you want to begin the program? Enter yes or no: ")


# Loops the program at the end of each problem
while programLoop != 9 :

    # Displays the menu options for the user to choose from
    programOption = int(input("This Python program displays Roman Numerals and Predicts Population. \n"
                              "Enter option 1 to display Roman Numerals. \n"
                              "Enter option 2 to Predict Population \n"
                              "Enter 9 to Exit the program. \n"
                              "Enter number here: "))
    # Input validation for the variable programOption

    while programOption not in validInputs:
        programOption = int(input("Invalid input.\nEnter option 1 to display Roman Numerals. \n"
                                  "Enter option 2 to Predict Population. \n"
                                  "Enter 9 to Exit the program. \n"
                                  "Enter number here: "))
    else:
        # Executes each of the menu options correctly
        if programOption == 1:
            romanNumerals = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
            userNumber = int(input("Enter a number between 1 - 10."))
            # Input validation for the variable userNumber
            while userNumber not in range(11):
                userNumber = int(input("Invalid input. Enter a number between 1 - 10. "))
            # Outputs the correct result for the Roman Numeral Problem
            print(f'The roman numeral for {userNumber} is: {romanNumerals[userNumber]}')
            programLoop = input("Do you want to continue the program?")
        elif programOption == 2:
            startNumber = int(input("Enter the starting number of organisms: "))
            dataOutput = []
            # Input validation for the variable startNumber
            while startNumber < 0:
                startNumber = int(input("Invalid input. Re-enter the starting number of organisms:"))
            averageDailyIncrease = int(input("Enter the average daily increase: "))
            # Input validation for the variable averageDailyIncrease
            while averageDailyIncrease not in range(1, 101):
                averageDailyIncrease = int(
                    input("Invalid Input. Re-enter the average daily increase as a percentage: "))
            daysLeft = int(input("Enter the number of days the organism will be left to multiply: "))
            # Input validation for the variable daysLeft
            while daysLeft not in range(2, 31):
                daysLeft = int(input("Invalid Input. Re-enter the number of days the organism will be left to \n"
                                     "multiply between 2 - 30 days: "))
            # Correctly calculates the average increase in population
            for i in range(daysLeft):
                population = startNumber
                dataOutput.append(population)
                population = startNumber + (startNumber * (averageDailyIncrease / 100))
                startNumber = population
            # Outputs the result of average increase in population correctly
            print(f'Day Approximate          Population')
            for i in range(daysLeft):
                print(f'{i + 1}.                       {dataOutput[i]}')
            programLoop = input("Do you want to continue the program?")
        else:
            print("Program complete.")
            exit()
else:
    print("Program complete.")
    exit()