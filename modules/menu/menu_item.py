class MenuItem:
  def __init__(self, name: str, price: float):
    self._name = name
    self._price = price

  def __str__(self):
    return f'{self._name} ({round(self._price, 2)})'
  
  

