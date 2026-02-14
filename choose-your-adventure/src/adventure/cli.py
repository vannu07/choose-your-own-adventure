"""Command-line interface functions for the adventure game."""


def display_welcome():
    """Display the welcome message to the player."""
    print("Welcome to the Choose Your Own Adventure Game!")
    print("Get ready to embark on an exciting journey!")


def get_user_input(prompt):
    """Get input from the user with the given prompt."""
    return input(prompt)


def display_scene(scene_description):
    """Display the scene description to the player."""
    print(scene_description)


def display_choices(choices):
    """Display the available choices to the player."""
    print("What would you like to do?")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")


def get_choice(num_choices):
    """Get a valid choice from the player within the given range."""
    while True:
        try:
            choice = int(get_user_input("Enter the number of your choice: "))
            if 1 <= choice <= num_choices:
                return choice
            print(f"Please enter a number between 1 and {num_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_message(message):
    """Display a message to the player."""
    print(message)
