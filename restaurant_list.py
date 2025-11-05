import os

restaurants = []


def register():
  name = input("Input the restaurant name: ")
  restaurants.append({
    'name': name,
    'active': False
  })
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Successfully registered!")

def list():
  if(restaurants.__len__() == 0):
    print("No restaurants registered")
    return

  for index, restaurant in enumerate(restaurants):
    print(f"{index+1}. {restaurant['name']} - [{'X' if restaurant['active'] else ' '}]")

def enable():
  index = int(input("Insert the restaurant id you want to enable:\n"))
  try:
    restaurants[index-1]['active'] = True
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Restaurant enabled!")
  except IndexError:
    print("Invalid restaurant id")
  except Exception as e:
    print(f"Error enabling restaurant: {e}")

def delete():
  index = int(input("Insert the restaurant id you want to delete:\n"))
  try:
    del restaurants[index-1]
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Successfully deleted!")
  except IndexError:
    print("Invalid restaurant id")
  except Exception as e:
    print(f"Error deleting restaurant: {e}")
