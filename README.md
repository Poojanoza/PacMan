
# Pac-Man Game in Python with Pygame

This project is a Pac-Man game built from scratch using Python and the Pygame library. The game features basic mechanics of the classic Pac-Man, including ghost AI, power-ups, and collision detection.

## Features
- **Classic Pac-Man Gameplay**: Control Pac-Man, collect pellets, avoid ghosts, and eat power-ups to become invincible.
- **Ghost AI**: Ghosts have different movement patterns to chase or evade Pac-Man.
- **Multiple Levels**: The game supports different levels that are stored in a separate board file.
- **Lives System**: Pac-Man has 3 lives before the game ends.
- **Score Tracking**: Keep track of your score by eating pellets and defeating ghosts.
- **Sound Effects**: Optional sound effects for game events like eating pellets, power-ups, or getting caught by a ghost.

## Technologies Used
- **Python**: The main programming language.
- **Pygame**: A popular library for creating games in Python.
- **Math**: For handling game mechanics like angles and distances.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame (install using pip)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Poojanoza/PacMan.git
   cd pacman-game
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python pacman.py
   ```

### Folder Structure
```
Pacman/
│
├── assets/
│   ├── player_images/   # Pac-Man sprites
│   ├── ghost_images/    # Ghost sprites (Blinky, Pinky, Inky, Clyde)
│   └── sounds/          # Sound files (optional)
│
├── board.py            # Contains board layouts for different levels
├── pacman.py           # Main game file
└── README.md           # This file
```

### Controls
- **Arrow Keys**: Move Pac-Man (Up, Down, Left, Right)
- **Space Bar**: Restart the game after Game Over or Victory.

## How to Add Sounds
You can add sound effects by placing sound files in the `assets/sounds/` folder and loading them in the `pacman.py` file using `pygame.mixer.Sound()`.

## Contribution
Feel free to fork this project and submit pull requests for improvements!

