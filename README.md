# 🎲 choose-your-own-adventure

![Game GIF](https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif)

A lightweight, extensible command-line "choose your own adventure" game template in Python — enhanced README with icons and an animated preview.

Badges
- ![Python](https://img.shields.io/badge/python-3.8%2B-blue)
- ![License](https://img.shields.io/badge/license-MIT-green)

Quick Preview
- Run the game: `python -m adventure` (entry: `src/adventure/__main__.py`)
- View the repo: https://github.com/vannu07/choose-your-own-adventure
- Live GitHub Pages (after deploy): https://vannu07.github.io/choose-your-own-adventure

What’s inside
- Source: `src/adventure`
  - Command line UI: `src/adventure/cli.py`
  - Engine: `src/adventure/engine.py`
  - Scenes: `src/adventure/scenes.py`
  - Choices model: `src/adventure/choices.py`
  - Story data: `src/adventure/data/stories/starter_story.yaml`
- Tests: `tests/`
- Project config: `pyproject.toml`, `requirements.txt`

Setup

1. Install dependencies:
```sh
pip install -r requirements.txt
```

2. Run the game:
```sh
python -m adventure
```

Adding your own animated preview
- Add an animated GIF to `assets/preview.gif` and update the top image link if desired.

Contributing
- Report bugs or propose features via issues / PRs.
- Run tests: `pytest`

License
- MIT

Enjoy! 🎮