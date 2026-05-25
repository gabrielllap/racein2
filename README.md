# Race in 2

A simple 2D racing game made with Python and Pygame.  
Players race to the finish line while avoiding obstacles on the road.

---

# Features

- Single Player mode
- Local Multiplayer mode
- VS AI mode
- Obstacle collision system
- Timer system
- Leaderboard saved in a text file
- Smooth car movement
- Winner screen

---

# Technologies Used

- Python
- Pygame

---

# Game Modes

## 1. Single Player
Control the red car and try to reach the finish line as fast as possible.

## 2. Local Multiplayer
Two players can play on the same keyboard.

- Player 1 controls the red car
- Player 2 controls the blue car

## 3. VS AI
Play against an AI-controlled opponent that follows the player and moves automatically.

---

# Controls

## Player 1 Controls

| Key | Action |
|-----|--------|
| W | Move Up |
| S | Move Down |
| A | Move Left |
| D | Move Right |

## Player 2 Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

---

# How the Game Works

## Main Menu
When the game starts, a menu is displayed with 3 options:

- Single Player
- Local Multiplayer
- VS AI

The player chooses a mode using the mouse.

---

## Player Movement
Cars move using keyboard controls.  
The game updates movement every frame using the Pygame game loop.

---

## Obstacles
Road cones are placed on the map as obstacles.

If a car touches an obstacle:
- The car is pushed backward
- The player loses time

---

## Collision System
In multiplayer and AI mode:
- Cars can collide with each other
- Cars push away from one another when they overlap

---

## AI System
In VS AI mode:
- The AI car automatically moves forward
- The AI follows the player's X position

---

## Timer System
The game tracks the total race time:
- Timer starts when the match begins
- Timer stops when a player wins

---

## Win Condition
A player wins when their car reaches the finish line at the top of the map.

The winner message is displayed on the screen.

---

# Leaderboard System

The game saves scores inside:

```txt
leaderboard.txt
```

The leaderboard stores:
- Player name
- Finish time

Only the latest 5 scores are displayed in the game.

---

# Project Structure

```bash
project-folder/
│
├── racegame.py
├── leaderboard.txt
│
├── assets/
│   ├── redcar.png
│   ├── bluecar.png
│   └── roadcon.png
```

---

# Installation

## 1. Install Python
Download Python from:

https://www.python.org/

---

## 2. Install Pygame

```bash
pip install pygame
```

---

## 3. Run the Game

```bash
python racegame.py
```

---

# Author

Created using Python and Pygame.
