import os
import restaurant_list


def colect_options():
  try:
    option = int(input("\nChoose option: \n"))
    define_path_by_option(option)
  except:
    define_path_by_option("invalid")

def show_options():
  print("Select a option\n")
  print("1. Create restaurant")
  print("2. Enable restaurant")
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
      restaurant_list.register()
      restart()
    case 2:
      restaurant_list.enable()
      restart()
    case 3:
      restaurant_list.list()
      restart()
    case 4:
      restaurant_list.delete()
      restart()
    case 5:
      print("Closing app...")

      return
    case _:
      print("\nInvalid option")

def main():
  show_options()

if(__name__ == '__main__'):
  main()