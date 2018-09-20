from random import randint

class Item():
  # Create the item
  def __init__(self,item_type = None, item_name = None):
    self.type_of_object = item_type
    self.name = item_name
    self.description = None
    self.possible_strength = ["weak", "normal", "strong", "legendary"]
    self.strength = self.possible_strength[randint(0,3)]
    
  # ' Define a name for the item
  def set_name(self, item_name = " "):
    self.name = item_name
  
  def get_name(self):
    return self.name

  # Defife what kind of item the character will be dealing with
  def set_type(self, item_type = " "):
    self.type_of_object = item_type
  
  def get_type(self):
    return self.type_of_object

  def set_description(self, item_description = " "):
    self.description = item_description
  # Describe the item
  def describe(self):
    print("--- " + self.name + " ---")
    print(self.description)
    print("Your " + self.name + " " + self.type_of_object + " is " + self.strength)

  def get_strength(self):
    print("Your " + self.name + " " +self.type_of_object + " is " + self.strength)