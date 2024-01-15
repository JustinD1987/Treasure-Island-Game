print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Which direction do you want to go? Left or Right? ")

if direction == "Left" or direction == "left":
  swim = input("You have reached a lake. Do you want to swim or wait? ")
  if swim == "Wait" or swim == "wait":
    house_door = input("You have reached a house with three doors. Which door do you want to go through? Red, Blue or Yellow? ")
    if house_door == "Yellow" or house_door == "yellow":
      print("Congratulations! You have found the treasure! ")
    elif house_door == "Red" or house_door == "red":
      print("You have been burned by fire. Game Over. ")
    elif house_door == "Blue" or house_door == "blue":
      print("You have been eaten by beasts. Game Over. ")
    else:
      print("Game Over.")
  else:
    print("You have been attacked by a trout. Game Over.")
else:
  print("You have fallen into a hole. Game Over.")