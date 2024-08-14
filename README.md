# Restaurant Management Console Application

This Python script is a console-based application designed to manage a list of restaurants. The application allows users to perform various tasks such as registering new restaurants, listing all registered restaurants, and toggling the state (open/close) of a restaurant.

## Features

- **Display Title:** A stylized ASCII title is shown at the start of the application.
- **Display Options:** A menu of options is presented to the user.
- **Register New Restaurant:** Allows the user to register a new restaurant. New restaurants are registered as "closed" by default.
- **List Restaurants:** Displays a list of all registered restaurants, along with their category and current state (open/closed).
- **Toggle Restaurant State:** Allows the user to toggle the state (open/close) of a specific restaurant.
- **Exit Application:** Ends the application with a thank you message.

## Functions

- **display_title():** Displays the title of the application.
- **display_options():** Displays the main menu options.
- **finish_app():** Displays a thank you message and ends the application.
- **return_to_main():** Returns the user to the main menu after an action is completed.
- **invalid_option():** Handles invalid menu selections by the user.
- **display_subtitle(text):** Displays a subtitle with a border of asterisks.
- **register_new_restaurant():** Prompts the user to register a new restaurant, which is added to the list as closed by default.
- **estate_restaurant():** Allows the user to toggle the state of a restaurant between open and closed.
- **list_restaurants():** Lists all restaurants with their name, category, and current state.
- **choose_option():** Prompts the user to choose an option from the menu and directs them to the corresponding function.
- **main():** The main function that clears the screen, displays the title and options, and manages the user’s interaction with the application.

## Dependencies

This script requires the 'os' module, which is included in Python's standard library.

## Usage

This script can be used as a basic management tool for handling a list of restaurants, especially useful for small projects or as a learning exercise for understanding basic Python functionalities.
