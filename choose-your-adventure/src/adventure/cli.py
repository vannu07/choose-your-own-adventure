def display_welcome():
    print("Welcome to the Choose Your Own Adventure Game!")
    print("Get ready to embark on an exciting journey!")
    
def get_user_input(prompt):
    return input(prompt)

def display_scene(scene_description):
    print(scene_description)

def display_choices(choices):
    print("What would you like to do?")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

def get_choice(num_choices):
    while True:
        try:
            choice = int(get_user_input("Enter the number of your choice: "))
            if 1 <= choice <= num_choices:
                return choice
            else:
                print(f"Please enter a number between 1 and {num_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_message(message):
    print(message)