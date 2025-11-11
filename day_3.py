print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_input=input(""" You're at a cross road. Where do you want to go?
                  Type "Left" or "Right" """).lower()
if user_input=='left':


    user_input1 = input("""You've come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across.""").lower()

    if user_input1 == "wait":
        user_input2 = input("""You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?""").lower()
        if user_input2 == "yellow":
            print("You win")
        elif user_input2=='red':
            print("game over")
        elif user_input2=='blue':
            print("game over")
        else:
            print("you entered the wrong door.game over")
    else:
        print("game over")

else:
    print("game over")