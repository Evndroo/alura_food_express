import os
from modules.restaurant import Restaurant


def colect_options():
  try:
    option = int(input("\nChoose option: \n"))
    define_path_by_option(option)
  except:
    define_path_by_option("invalid")

def show_options():
  print("Select a option\n")
  print("1. Create restaurant")
  print("2. Change restaurant state")
  print("3. List restaurants")
  print("4. Delete restaurant")
  print("5. Leave system")
  colect_options()

def restart():
  input("\nClick enter to show options\n")
  os.system('cls' if os.name == 'nt' else 'clear')

  show_options()

def define_path_by_option(option: int):
  os.system('cls' if os.name == 'nt' else 'clear')

  match option:
    case 1:
      Restaurant.register()
      restart()
      # return
    case 2:
      Restaurant.change_some_state()
      restart()
      # return
    case 3:
      Restaurant.list_all()
      restart()
      # return
    case 4:
      Restaurant.delete()
      restart()
      # return
    case 5:
      print("Closing app...")
      return

def main():
  show_options()

if(__name__ == '__main__'):
  main()