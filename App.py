import os

restaurants = [
            {'name': 'Zio', 'category': 'Japanese', 'activated': True},
            {'name': 'Depot temático', 'category': 'Medieval', 'activated': False},
            {'name': 'Incantori', 'category': 'Harry Potter', 'activated': False},
            {'name': 'Barneys hamburger', 'category': 'Hamburger', 'activated': True},
            {'name': 'Mammo', 'category': 'Italian', 'activated': True},
            {'name': 'Gretta Café', 'category': 'Cafe', 'activated': True},
            {'name': 'Manu', 'category': 'Gastronomic', 'activated': False},
            {'name': 'Mc Donald', 'category': 'Hamburger', 'activated': True},
            {'name': 'Madero', 'category': 'Hamburger', 'activated': False},
            {'name': 'Oriental', 'category': 'Asian', 'activated': True},
            {'name': 'Outback', 'category': 'buffet-style service', 'activated': True},
            {'name': 'Divino fogão', 'category': 'lunch', 'activated': False}
            ]

def display_title():
    print("""
██████████████████████████████████████████████████████████████████████████
█▄─▄████▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
██─██▀██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    """)

def display_options():
    print('1. Register Restaurant')
    print('2. List Restaurants')
    print('3. Open/Close Restaurant')
    print('4. Exit\n')

def finish_app():
    display_subtitle('Thanks to visit Labor Express!')

def return_to_main():
    input('\nPress Enter to return to main menu...')
    main()

def invalid_option():
    print('Invalid option!')
    return_to_main()

def display_subtitle(text):
    os.system('cls') # os.system('clear') for mac
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def register_new_restaurant():
    display_subtitle('Register a new Restaurant')
    name_restaurant = input('Name of Restaurant: ')
    category_of_restaurant = input(f'Category of {name_restaurant}: ')
    data_restaurant = {'name': name_restaurant, 'category': category_of_restaurant, 'activated': False} #Regra de negocio, sempre quando for registrar um novo restaurante ele deve estar desativado
    restaurants.append(data_restaurant)
    print(f'Restaurant {name_restaurant} successfully registered!\n')
    return_to_main()

def estate_restaurant():
    display_subtitle('Toggle Restaurant estate')
    name_restaurant = input('Choose the restaraunt you want to toggle: ')
    restaurant_find = False
    
    for restaurant in restaurants:
        if restaurant['name'] == name_restaurant:
            restaurant['activated'] = not restaurant['activated']
            restaurant_find = True
            message = f'Restaurant {name_restaurant} successfully toggled!' if restaurant['activated'] else f'Restaurant {name_restaurant} successfully deactivated!'
            print(message)
            break
    if not restaurant_find:
        print(f'Restaurant {name_restaurant} not found!')
    return_to_main()

def list_restaurants():
    display_subtitle('List of Restaurants')
    
    print(f' {"Name".ljust(20)} | {"Category".ljust(20)} | {"State of service".ljust(20)}')
    
    for restaurant in restaurants:
        name_restaurant = restaurant['name']
        category_restaurant = restaurant['category']
        activated_restaurant = 'Open' if restaurant['activated'] else 'Closed'
        print(f'- {name_restaurant.ljust(20)} | {category_restaurant.ljust(20)} | {activated_restaurant.ljust(20)}')

    return_to_main()

def choose_option():
    try:
        user_option = int(input('Choose an option: '))
        
        if user_option == 1:
            register_new_restaurant()
        elif user_option == 2:
            list_restaurants()
        elif user_option == 3:
            estate_restaurant()
        elif user_option == 4:
            finish_app()
        else:
            invalid_option()
    except ValueError:
        invalid_option()

def main():
    os.system('cls')  # os.system('clear') for mac
    display_title()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
