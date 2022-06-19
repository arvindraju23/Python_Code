import random
l=["Rock","Scissor", "Paper"]

'''
Rock Vs Paper -> Paper Wins
Rock Vs Scissor -> Rock Wins
Paper Vs Scissor -> Scissor Wins
'''

while True:
    Computer_Count=0
    User_Count=0
    UserChoice=int(input('''
    
You wants to play the Game?
1. Yes
2. No | Exit

    '''))

    if UserChoice==1:
        for a in range(1,6):
            UserInput=int (input('''
            
1. Rock
2. Scissor
3. Paper  
            
      '''))
            if UserInput==1:
               UserChoice="Rock"
            elif UserInput==2:
                UserChoice="Scissor"
            elif UserInput==3:
                UserChoice="Paper"
            else:
                print("Invalid Choice")

            Computer_choice=random.choice(l)
            # print(UserChoice)
            # print(Computer_choice)

            if Computer_choice==UserChoice:
                print("Computer Chosen ", Computer_choice)
                print("You have Chosen ", UserChoice)
                print("Game Draw")

            elif(UserChoice=="Rock" and Computer_choice=="Scissor") or (UserChoice=="Paper" and Computer_choice=="Rock") or (UserChoice=="Scissor" and Computer_choice=="Paper"):
                print("Computer Chosen" , Computer_choice)
                print("You have Chosen", UserChoice)
                print ("You Won the round")
                User_Count +=1

            else:
                print("Computer Chosen" , Computer_choice)
                print("You have Chosen", UserChoice)
                print("Computer Won the round")
                Computer_Count +=1

        if User_Count==Computer_Count:
          print("Finally Game Draw")
          print("Your Score is: ", User_Count)
          print("Computer Score is: ", Computer_Count)

        elif User_Count>Computer_Count:
          print ("Finally You Won The Game")
          print ("Your Score is: ", User_Count)
          print("Computer Score is: ", Computer_Count)

        else:
          print("Finally Computer The Game")
          print("Your Score is: ", User_Count)
          print("Computer Score is: ", Computer_Count)
    else:
        break
