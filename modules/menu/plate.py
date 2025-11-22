

from modules.menu.menu_item import MenuItem


class Plate(MenuItem):

  def __init__(self, name, price):
    super().__init__(name, price)