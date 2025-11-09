class AdventureEngine:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def load_scenes(self, scenes):
        self.scenes = scenes
        self.current_scene = list(scenes.keys())[0]  # Start with the first scene

    def get_current_scene(self):
        return self.scenes[self.current_scene]

    def make_choice(self, choice):
        if choice in self.scenes[self.current_scene]['choices']:
            self.current_scene = self.scenes[self.current_scene]['choices'][choice]
        else:
            raise ValueError("Invalid choice")

    def is_game_over(self):
        return self.current_scene not in self.scenes

    def reset_game(self):
        self.current_scene = list(self.scenes.keys())[0]  # Reset to the first scene