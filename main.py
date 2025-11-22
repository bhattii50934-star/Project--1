''' PROJECT 1: SNAKE, WATER, GUN GAME 
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user. ''' 




import random      # ik module ko import kia 

'''1 for snake 
-1 for water
0 for gun
'''      
# Randomly computer ik ko store krlaga 

computer = random.choice([-1, 0, 1]) 
# As a string s, w, g
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

#reverseDict islia bnai hka nichy print ma {reverseDict[you]} rakha you ma jo b hoga wo reverseDict ma jhaga 1,-1,0 oska motabik output ma print hoga snake, water and gun

you = youDict[youstr]   # youstr ma jo b user enter kraga s,w,g wo youDict ma jahga oska motabik ossa value milage 1,-1,0 you ma save hojage

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you ==1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You Lose!")
    
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer ==0 and you ==1):
        print("You win!")
    elif(computer ==0 and you ==1):
        print("You lose!")
    
    else:
        print("Something went wrong")































