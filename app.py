import requests
import json

url = "http://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)
if(response.status_code == 200):
    response_json: list = response.json()
    restaurants = {}

    for restaurant in response_json:
        restaurant_name = restaurant['Company']
        if(restaurant_name not in restaurants):
            restaurants[restaurant_name] = []

        restaurants[restaurant_name].append({
            "item": restaurant['Item'],
            "description": restaurant['description'],
            "price": restaurant['price']
        })


else:
    print(f'O erro foi {response.status_code}')


for restaurant_name, menu_list in restaurants.items():
    print(f"Creating {restaurant_name} file ({menu_list.__len__()} menu items)")
    file_name = f"{restaurant_name}.json"

    with open(file_name, 'w') as restaurant_file:
        json.dump(menu_list, restaurant_file, indent=4)