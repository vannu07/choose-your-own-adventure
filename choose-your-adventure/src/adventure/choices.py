"""Module for managing choices in the adventure game."""


class Choice:  # pylint: disable=too-few-public-methods
    """Represents a single choice in the game."""

    def __init__(self, description, next_scene):
        """Initialize a Choice with a description and next scene."""
        self.description = description
        self.next_scene = next_scene


class Choices:
    """Manages a collection of choices available to the player."""

    def __init__(self):
        """Initialize an empty Choices collection."""
        self.choices = []

    def add_choice(self, description, next_scene):
        """Add a choice to the collection."""
        choice = Choice(description, next_scene)
        self.choices.append(choice)

    def get_choices(self):
        """Return the list of all choices."""
        return self.choices

    def __str__(self):
        """Return a formatted string representation of all choices."""
        return "\n".join(f"{i + 1}. {choice.description}" for i, choice in enumerate(self.choices))
