class Choice:
    def __init__(self, description, next_scene):
        self.description = description
        self.next_scene = next_scene

class Choices:
    def __init__(self):
        self.choices = []

    def add_choice(self, description, next_scene):
        choice = Choice(description, next_scene)
        self.choices.append(choice)

    def get_choices(self):
        return self.choices

    def __str__(self):
        return "\n".join(f"{i + 1}. {choice.description}" for i, choice in enumerate(self.choices))