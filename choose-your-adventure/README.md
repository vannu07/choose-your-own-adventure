# Choose Your Own Adventure Game

## Overview
This project is a simple command line "choose your own adventure" game where players make choices that affect the outcome of the story. The game is structured into scenes, each with its own narrative and choices.

## Project Structure
```
choose-your-adventure
├── src
│   ├── adventure
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── cli.py
│   │   ├── engine.py
│   │   ├── scenes.py
│   │   ├── choices.py
│   │   └── data
│   │       └── stories
│   │           └── starter_story.yaml
├── tests
│   ├── test_engine.py
│   └── test_scenes.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation
To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Running the Game
To start the game, execute the following command:

```
python -m adventure
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.