import rpg

#To take itens
backpack = []

#All objects declations
billy = rpg.Enemy("Billy", "A fucking weirdo with a baseball bat")
jesse = rpg.Character("Jesse", "A sweet little stranger, an eminent danger")
kitchen = rpg.Room("Kitchen")

dinning_hall = rpg.Room("Dinning Hall")
ballroom = rpg.Room("Ballroom")
sword = rpg.Item("sword", "Galandor")

#The  descriptions of some objects
kitchen.set_description("A dank and dirty room buzzing with flies.")
dinning_hall.set_description("A large room with ornate golden decorations on each wall.")
ballroom.set_description("I don\'t know what this was supposed to be.")
sword.set_description("Pure simpathy")

#Linking the rooms
kitchen.link_room(dinning_hall, "south")
dinning_hall.link_room(kitchen, "north")
dinning_hall.link_room(ballroom, "east")
ballroom.link_room(dinning_hall, "west")

#Setting an item in the ballroom
ballroom.set_item(sword)

# Some actions with a friendly character
jesse.set_conversation("Hello there, do you want some food?")
jesse.describe()
jesse.talk()

# Some actions with an enemy
billy.set_conversation("You better run...")
billy.describe()
billy.talk()
billy.set_weakness(sword.get_name)

current_room = kitchen          

dead = False

while dead == False:
  # Show the current place
  print("\n")         
  current_room.get_details() 
  inhabitant = current_room.get_character()
  item = current_room.get_item()

  # Check if there's a character
  if inhabitant is not None:
    inhabitant.describe() 

  # Check if there's an item in the, allow the player take the it, if there's some
  if item is not None:
    item.describe()  
    print("Write \'take\' to put the item in your backpack") 
  print("Write \'exit\' if you want to close the game")
  command = input("> ") 

  # Allow the player to exit the game 
  if command == "exit":
    break
  elif command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command) 
  
  # Allow the player to talk with the character
  elif command == "talk":
    inhabitant.talk()

  # Allow the player to fight with a character
  elif command == "fight":
    print("What will you fight with?")
    fight_with = input()
   
  # Check if it's possible to fight
    if backpack == []:
      print("You have nothing to fight with :(")
      fight_with = " "

    for i in backpack:
      if i == fight_with:
        print("Here's your item!")
        break
    else:
      print("Sorry, you don\'t have this item")
      fight_with = " "

    if inhabitant.fight(fight_with) == True:
      print("You defeated " + inhabitant.get_name())

    else:
      print("You we're defeated by " + inhabitant.get_name())
      print("GAME OVER")
      dead = True

  # Take an item
  elif command == "take":
    backpack.append(item)
    print("The "+ item.get_name() + " is in your backpack")
    current_room.set_item(None)
    

    
    