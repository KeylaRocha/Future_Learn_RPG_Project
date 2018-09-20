class Character():

  # Create the character
  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description 
    self.conversation = None

  # Define the character a name
  def set_name(self, item_name):
    self.name = item_name
  
  def get_name(self):
    return self.name

  # Define the character description
  def set_description(self, item_description):
    self.description = item_description

  def get_description(self):
    print(self.description)

  # Describe this character
  def describe(self):
    print( self.name + " is here!" )
    print( self.description )

  # Define what this character will say when talked to
  def set_conversation(self, conversation):
    self.conversation = conversation

  # Talk to this character
  def talk(self):
    if self.conversation is not None:
      print("[" + self.name + " says]: " + self.conversation)
    else:
      print(self.name + " doesn't want to talk to you")

  # Fight with this character(friendly characters don't fight)
  def fight(self, combat_item):
    print(self.name + " doesn't want to fight with you")
    return True

class Enemy(Character):
  # Create the enemy
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description) #Call Character class constructor
    self.weakness = None

  # Define a weakness for the enemy
  def set_weakness(self, enemy_weakness):
    self.weakness = enemy_weakness
  
  def get_weakness(self):
    print("Your enemy weakness is: " + self.weakness)
    
  # Fight with the enemy
  def fight(self, combat_item):
    if combat_item == self.weakness:
      print("You fend " + self.name + " off with the " + combat_item )
      return True
    else:
      print(self.name + " crushes you, puny adventurer")
      return False