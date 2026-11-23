""" num = 2 ** 3
print(num) """

""" num1 = 5 % 2
print(num1) """

#Control Flow: If, Else, Elif, For Loop, While Loop, Break, Continue, Pass
""" num1 = int(input("Enter a number: "))

if num1 > 0:
    print("The number is greater than zero.")
else:
    print("The number is less than 0.") """

#For Loop
""" for i in range(1,7):
    print("Count:", i) """
    
#While Loop
password = "Blackmind"
attempts = 0
while attempts < 3:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1
        print("wrong password. You have", 3 - attempts, "attempts left.")