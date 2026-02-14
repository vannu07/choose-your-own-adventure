"""Module for managing scenes in the adventure game."""


class Scene:
    """Represents a single scene in the adventure game."""

    def __init__(self, description, choices):
        """Initialize a scene with a description and available choices."""
        self.description = description
        self.choices = choices

    def display(self):
        """Display the scene description and available choices."""
        print(self.description)
        for index, choice in enumerate(self.choices):
            print(f"{index + 1}: {choice['text']}")

    def get_next_scene(self, choice_index):
        """Get the next scene ID based on the player's choice."""
        return self.choices[choice_index]['next_scene']


class SceneManager:
    """Manages all scenes in the game."""

    def __init__(self):
        """Initialize an empty scene manager."""
        self.scenes = {}

    def add_scene(self, scene_id, scene):
        """Add a scene to the manager with the given ID."""
        self.scenes[scene_id] = scene

    def get_scene(self, scene_id):
        """Get a scene by its ID."""
        return self.scenes.get(scene_id)

    def display_scene(self, scene_id):
        """Display a scene by its ID, or show an error if not found."""
        scene = self.get_scene(scene_id)
        if scene:
            scene.display()
            return scene
        print("Scene not found.")
        return None
