from modules.menu.menu_item import MenuItem

class Beverage(MenuItem):
  def __init__(self, name: str, price: float, size: str):
    super().__init__(name, price)
    self._size = size