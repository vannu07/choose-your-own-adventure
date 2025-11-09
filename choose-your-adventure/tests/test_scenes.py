import unittest
from adventure.scenes import Scene

class TestScenes(unittest.TestCase):

    def setUp(self):
        self.scene = Scene("Test Scene", "This is a test scene.")

    def test_scene_title(self):
        self.assertEqual(self.scene.title, "Test Scene")

    def test_scene_description(self):
        self.assertEqual(self.scene.description, "This is a test scene.")

    def test_scene_choices(self):
        self.scene.add_choice("Go left", "left_scene")
        self.assertIn("Go left", self.scene.choices)

    def test_scene_transition(self):
        self.scene.add_choice("Go right", "right_scene")
        self.assertEqual(self.scene.transition("Go right"), "right_scene")

if __name__ == '__main__':
    unittest.main()