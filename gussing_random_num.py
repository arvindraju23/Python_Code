import random
c_number=random.randrange(1,101)
userInput=int(input("Enter Your Number: "))
if userInput>c_number:
    print("Computer Random Number is: " , c_number)
    print("Your Gussing number is High")
elif c_number>userInput:
    print("Computer Random Number is: ", c_number)
    print("Your gussing number is Low")
else:
    print("Computer Random Number is: ", c_number)
    print("Your guessing number is equal to random number")