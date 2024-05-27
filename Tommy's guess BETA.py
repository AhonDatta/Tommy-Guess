
# Installing engine

import random 

# Personal information

Name = input("Enter your name :  ")
age = int(input("Enter your age :  "))


# Creating random

if (age < 12) :
    print("Your difficulty is easy :) ")
    num = random.randint(1,10)
    print("System has guessed a number between 1 to 10.")
elif (age >= 12) :
    print("Your difficulty is medium :)")
    num = random.randint(20,35)
    print("System has guessed a number between 20 to 35. ")
elif (age >= 18) :
    print("Your difficulty is hard :( ")
    num = random.randint(1,60)
    print("System has guessed a number between 1 to 60. ")
    
print("You have 2 chances only !")

number = int(input("System has guessed a number, enter that number :  "))

# Condition

if (number == num) :
    print("You are correct !")
    print("The number is ", num)
elif (number < num) :
    print("Your number is smaller than that number...")
    print("You have last chance !")
    number2 = int(input("Enter that number :  "))
    if (number2 == num) :
        print("You are correct !")
        print("The number is ", num)
    elif (number2 < num) :
        print("Sorry ! Better luck next time :(")
    elif (number2 > num) :
        print("Sorry ! Better luck next time :(")
    else :
        print("Something is wrong :(")
elif (number > num) :
    print("Your number is bigger than that number...")
    print("You have last chance !")
    number3 = int(input("Enter that number :  "))
    if (number3 == num) :
        print("You are correct !")
        print("The number is ", num)
    elif (number3 < num) :
        print("Sorry ! Better luck next time :(")
    elif (number3 > num) :
        print("Sorry ! Better luck next time :(")
    else :
        print("Something is wrong :(")
else :
    print("Sorry ! Something is wrong...")
    
print("The number was ", num)

# Finishing

print("Thank you for using Tommy's guess BETA")
print("It was created by Ahon Datta ( Rishi )")