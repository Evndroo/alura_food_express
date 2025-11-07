import os
import uuid

class Restaurant:
  all_restaurants:list[Restaurant] = []

  def __init__(self, name = '',type = ''):
    self._name = name.title()
    self._type = type.capitalize()
    self._active = False
    self._id = uuid.uuid4().__str__()

    Restaurant.all_restaurants.append(self)
  
  def __str__(self):
    return f"{self._id}{''.ljust(2)} | {self._name.ljust(25)} | {self._type.ljust(25)} | {self.get_visible_active()}"
        
  def get_visible_active(self):
    return f'[{'X' if self._active else ' '}]'

  @property
  def active(self):
    return self._active
  
  def change_state(self):
    self._active = not self._active

  @classmethod
  def has_restaurants(cls):
    return cls.all_restaurants.__len__() != 0

  @classmethod
  def list_all(cls):
    if(not cls.has_restaurants()):
      print("No restaurants registered")
      return
    
    print(f'{'ID'.ljust(38)} | {'Restaurant name'.ljust(25)} | {'Type'.ljust(25)} | {'Status'}')
    for restaurant in cls.all_restaurants:
      print(restaurant)

  @classmethod
  def find_by_id(cls, id):
    for restaurant in cls.all_restaurants:
      if(restaurant._id == id):
        return restaurant
      
  @classmethod
  def find_index_by_id(cls, id):
    for index, restaurant in enumerate(cls.all_restaurants):
      if(restaurant._id == id):
        return index

  @classmethod
  def change_some_state(cls):
    if(not cls.has_restaurants()):
      print("No restaurants registered")
      return

    id = input("Insert the restaurant id you want to change state:\n")
    try:
      founded_restaurant = cls.find_by_id(id)
      print(founded_restaurant)
      action = "disabled" if founded_restaurant.active else 'enabled'
      founded_restaurant.change_state()
      os.system('cls' if os.name == 'nt' else 'clear')

      print(f"Restaurant {action}!")
    except IndexError:
      print("Invalid restaurant id")
    except Exception as e:
      print(f"Error enabling restaurant: {e}")
  
  
  @classmethod
  def delete(cls):
    if(not cls.has_restaurants()):
      print("No restaurants registered")
      return        

    id = input("Insert the restaurant id you want to delete:\n")
    try:
      del cls.all_restaurants[cls.find_index_by_id(id)]
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Successfully deleted!")
    except IndexError:
      print("Invalid restaurant id")
    except Exception as e:
      print(f"Error deleting restaurant: {e}")
  
  @classmethod
  def register(cls):
    name = input("Input the restaurant name: ")
    type = input("Input the restaurant kind: ")
    Restaurant(name, type)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Successfully registered!")




  


restaraurant1 = Restaurant("Evandro", 'teste')
restaraurant1 = Restaurant("Evandro", 'teste2')

