"""Game engine for managing the adventure game state and logic."""


class AdventureEngine:
    """Main game engine for managing scenes and player choices."""

    def __init__(self):
        """Initialize the game engine with empty scenes and no current scene."""
        self.scenes = {}
        self.current_scene = None

    def load_scenes(self, scenes):
        """Load scenes into the engine and set the starting scene."""
        self.scenes = scenes
        self.current_scene = list(scenes.keys())[0]  # Start with the first scene

    def get_current_scene(self):
        """Get the current scene data."""
        return self.scenes[self.current_scene]

    def make_choice(self, choice):
        """Process a player's choice and transition to the next scene."""
        if choice in self.scenes[self.current_scene]['choices']:
            self.current_scene = self.scenes[self.current_scene]['choices'][choice]
        else:
            raise ValueError("Invalid choice")

    def is_game_over(self):
        """Check if the game has reached an ending scene."""
        return self.current_scene not in self.scenes

    def reset_game(self):
        """Reset the game to the starting scene."""
        self.current_scene = list(self.scenes.keys())[0]  # Reset to the first scene
