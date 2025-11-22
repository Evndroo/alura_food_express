

from modules.menu.menu_item import MenuItem
from enum import Enum

class BeverageSize(Enum):
  SMALL= 1
  MEDIUM= 1
  LARGE= 1
  EXTRA_LARGE= 1


class Beverage(MenuItem):

  def __init__(self, name, price, size: BeverageSize):
    super().__init__(name, price)
    self._size = size