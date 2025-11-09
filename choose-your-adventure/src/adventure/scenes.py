class Scene:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

    def display(self):
        print(self.description)
        for index, choice in enumerate(self.choices):
            print(f"{index + 1}: {choice['text']}")

    def get_next_scene(self, choice_index):
        return self.choices[choice_index]['next_scene']


class SceneManager:
    def __init__(self):
        self.scenes = {}

    def add_scene(self, scene_id, scene):
        self.scenes[scene_id] = scene

    def get_scene(self, scene_id):
        return self.scenes.get(scene_id)

    def display_scene(self, scene_id):
        scene = self.get_scene(scene_id)
        if scene:
            scene.display()
            return scene
        else:
            print("Scene not found.")
            return None