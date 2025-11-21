

from modules.menu.menu_item import MenuItem
from modules.restaurant import Restaurant


restaurant1 = Restaurant('praça', 'Gourmet')
restaurant1.receive_rating('Evandro', 10)
restaurant1.receive_rating('User 1', 8)
restaurant1.receive_rating('User 2', 2)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()