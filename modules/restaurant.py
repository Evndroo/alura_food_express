from modules.rating import Rating

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._ratings = []
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f"{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} | {'Status'}")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} |{restaurant.active}")

    @property
    def active(self):
        return '⌧' if self._active else '☐'
    
    def toggle_state(self):
        self._active = not self._active

    def receive_rating(self, customer, score):
        if 0 < score <= 5: 
            rating = Rating(customer, score)
            self._ratings.append(rating)

    @property
    def average_rating(self):
        if not self._ratings:
            return '-'
        soma_das_notas = sum(rating._rate for rating in self._ratings)
        quantidade_de_notas = len(self._ratings)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media