#BLACKMIND EDU TECH
#Foundation Fortess 2026 - Day 6
#Calculator Application -Version 2.0

print("===============================================================")
print("BLACKMIND CALCULATOR")
print("VERSION  2.0")
print("===============================================================")

#Display  available operations
print("1. Addition (+)")
print("2. Subtraction (-)")

#Ask the user to choose an operation
choice = input("choose operation (1 or 2): ")

#Receive two numbersfrom a user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if choice == "1":
    #Perform addition
    result = first_number + second_number
elif choice == "2":
    #Perform subtraction
    result = first_number - second_number
else:
    print("Invalid choice. Please select a valid operation.")
    result = None

#Perform addition
#result = first_number + second_number


#Display the result
print("---------------------------------------------------------------")
print("Operational Result: ", result)
print("---------------------------------------------------------------")
print("Thank you for using Blackmind Calculator. Have a great day!")