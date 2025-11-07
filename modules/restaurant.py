import os
import uuid

from evaluation import Evaluation

class Restaurant:
  all_restaurants:list[Restaurant] = []

  def __init__(self, name = '',type = ''):
    self._id = uuid.uuid4().__str__()
    self._name = name.title()
    self._type = type.capitalize()
    self._active = False
    self._evaluations: list[Evaluation] = []

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
    
    raise IndexError
      
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

  @classmethod
  def save_some_client_evaluation(cls):
    if(not cls.has_restaurants()):
      print("No restaurants registered")
      return
    
    id = input("Insert the restaurant id you want to add a client evaluation:\n")
    try:
      founded_restaurant = cls.find_by_id(id)

      client_name = input("Input the client that gave the feedback name:\n")
      nps_evaluation = int(input("Input the NPS (1-5) client evalutaion:\n"))

      if(not 0 <  nps_evaluation < 6):
        raise ValueError("nps out of range")

      evaluation = Evaluation(client=client_name, evaluation=nps_evaluation)
      founded_restaurant.save_client_evaluation(evaluation=evaluation)

      os.system('cls' if os.name == 'nt' else 'clear')

      print("Evaluation saved!")  
    except IndexError:
      print("Invalid restaurant id")
    except:
      print("Failed to add evaluation")

  def save_client_evaluation(self, evaluation:Evaluation):
    self._evaluations.append(evaluation)

  


restaraurant1 = Restaurant("Evandro", 'teste')
restaraurant1 = Restaurant("Evandro", 'teste2')


Restaurant.list_all()
Restaurant.save_some_client_evaluation()
