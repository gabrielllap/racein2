# 🏎️ Race In 2

Race In 2 is a fast-paced 2D racing game built with **Python** and **Pygame**. Players race toward the finish line while avoiding obstacles, competing against another player locally, or challenging an AI opponent.

## Features

- 🎮 **Three Game Modes**
  - Single Player
  - Local Multiplayer (1 vs 1)
  - Player vs AI

- 🚗 **Car Selection**
  - Choose from 4 unique cars:
    - Red
    - Blue
    - Green
    - Pink

- 🛣️ **Obstacle System**
  - Randomly generated road cones create challenges during each race.

- ⏱️ **Timer & Leaderboard**
  - Track your completion time in Single Player mode.
  - Best times are automatically saved to a local leaderboard.

- 🤖 **AI Opponent**
  - Race against a computer-controlled driver with randomized movement speed.

- 🏆 **Winner Screen**
  - Displays the race winner and allows returning to the main menu.

## Controls

### Player 1 (WASD)

| Key | Action |
|------|--------|
| W | Move Up |
| S | Move Down |
| A | Move Left |
| D | Move Right |

### Player 2 (Arrow Keys)

| Key | Action |
|------|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

## Requirements

- Python 3.8+
- Pygame

Install Pygame:

```bash
pip install pygame
```

## Project Structure

```text
project/
│
├── racegame.py
├── leaderboard.txt
│
└── assets/
    ├── redcar.png
    ├── bluecar.png
    ├── greencar.png
    ├── pinkcar.png
    └── roadcon.png
```

## Running the Game

```bash
python racegame.py
```

## How to Play

1. Launch the game.
2. Select a game mode from the main menu.
3. Choose your car.
4. Race from the bottom of the track to the finish line at the top.
5. Avoid road cones that slow your progress.
6. Reach the finish line before your opponent to win.

## Leaderboard

Single Player completion times are saved in:

```text
leaderboard.txt
```

The game automatically sorts and displays the top 10 fastest times.

## Built With

- Python
- Pygame
