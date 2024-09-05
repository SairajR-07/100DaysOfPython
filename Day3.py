print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice=input('You\'r at a crossroad, where you want to go? Type "Left" or "Right". ')
if choice=="Left":
    choice2=input('You\'ve come to a lake ,There is an island in the middle of the lake. Type "wait" for wait for a boat. Type "swim" to swim across.')
    if choice2=="wait":
       choice3= input("You arrived at the island, There a house with 3 doors One red, one Yellow, one blue.. which colour do you choose?")
       if choice3=="red":
           print("Its a room full of fire..<<Game Over>>..")
       elif choice3=="yellow":
           print("You Found a Treasure .!!! YOU WIN !!!")
       elif choice3=="blue":
           print("You enter a room full of beast..<<Game Over>>..")
       else:
           print("You choose a door that doesnt exist..<Game Over>>..")
    else:
        print("You got attacked by angry trout..<<Game Over>>..")
else:
    print("You fell in to a hole..<<Game Over>>..")
