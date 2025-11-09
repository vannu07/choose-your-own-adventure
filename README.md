# 🎲 choose-your-own-adventure

![Game GIF](https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif)

A lightweight, extensible command-line "choose your own adventure" game template in Python — enhanced README with icons and an animated preview.

Badges
- ![Python](https://img.shields.io/badge/python-3.8%2B-blue)
- ![License](https://img.shields.io/badge/license-MIT-green)

Quick Preview
- Run the game: `python -m adventure` (entry: [`adventure.__main__`](choose-your-adventure/src/adventure/__main__.py))
- Main CLI helpers: see [`adventure.cli.display_welcome`](choose-your-adventure/src/adventure/cli.py)
- Game engine: see [`adventure.engine.AdventureEngine`](choose-your-adventure/src/adventure/engine.py)

What’s inside
- Source: [choose-your-adventure/src/adventure](choose-your-adventure/src/adventure)
  - Command line UI: [`adventure.cli.display_welcome`](choose-your-adventure/src/adventure/cli.py), [`adventure.cli.get_choice`](choose-your-adventure/src/adventure/cli.py)
  - Engine: [`adventure.engine.AdventureEngine`](choose-your-adventure/src/adventure/engine.py)
  - Scenes: [`adventure.scenes.Scene`](choose-your-adventure/src/adventure/scenes.py), [`adventure.scenes.SceneManager`](choose-your-adventure/src/adventure/scenes.py)
  - Choices model: [`adventure.choices.Choice`](choose-your-adventure/src/adventure/choices.py)
  - Story data: [starter_story.yaml](choose-your-adventure/src/adventure/data/stories/starter_story.yaml)
- Tests: [choose-your-adventure/tests/test_engine.py](choose-your-adventure/tests/test_engine.py), [choose-your-adventure/tests/test_scenes.py](choose-your-adventure/tests/test_scenes.py)
- Project config: [choose-your-adventure/pyproject.toml](choose-your-adventure/pyproject.toml), [choose-your-adventure/requirements.txt](choose-your-adventure/requirements.txt)

Setup

1. Install dependencies:
```sh
pip install -r choose-your-adventure/requirements.txt
```

2. Run the game:
```sh
python -m adventure
```
(See entrypoint at [`choose-your-adventure/src/adventure/__main__.py`](choose-your-adventure/src/adventure/__main__.py).)

Adding your own animated preview
- Add an animated GIF to `choose-your-adventure/assets/preview.gif` and update the top image link.
- Or replace the example GIF URL with your hosted GIF.

Contributing
- Report bugs or propose features via issues / PRs.
- Run tests: `pytest choose-your-adventure/tests`

License
- MIT

Enjoy! 🎮