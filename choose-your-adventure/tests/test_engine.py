import unittest
from adventure.engine import GameEngine

class TestGameEngine(unittest.TestCase):

    def setUp(self):
        self.engine = GameEngine()

    def test_initial_state(self):
        self.assertEqual(self.engine.current_scene, 'start')

    def test_process_choice_valid(self):
        self.engine.process_choice('go_north')
        self.assertEqual(self.engine.current_scene, 'north_scene')

    def test_process_choice_invalid(self):
        initial_scene = self.engine.current_scene
        self.engine.process_choice('invalid_choice')
        self.assertEqual(self.engine.current_scene, initial_scene)

    def test_transition_to_scene(self):
        self.engine.transition_to_scene('end_scene')
        self.assertEqual(self.engine.current_scene, 'end_scene')

if __name__ == '__main__':
    unittest.main()