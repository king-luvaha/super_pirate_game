# 🏴‍☠️ Super Pirate Game

A feature-rich top-down 2D adventure game inspired by _Mario_, built with **Python** and **Pygame**. Battle enemies, collect coins, cast spells, and unlock new levels in an immersive retro-style world with animated tiles, particles, pathfinding, and more.

---

## 📸 Screenshots

_(Add your game screenshots here to visually showcase the overworld, level, UI, etc.)_

---

## 🚀 Features

- 🎮 Top-down RPG-style gameplay
- 🌍 Overworld map with unlockable paths and level progression
- 🧠 AI-driven enemies with patrol, chase, and ranged attack logic
- 💰 Coin collection, heart-based health system, and power-ups
- 🎯 Level goals, traps (like spikes), animated water, and falling objects
- 🎮 Smooth animations, particle effects, and screen transitions
- 💥 Combat system with enemies and projectiles
-  💖 Heart-based health system with UI animation
- 🌊 Animated water, palm trees, clouds, and particles
- 📦 Clean file structure with reusable components
- 🔁 Modular design using classes like `Sprite`, `AnimatedSprite`, `Enemy`, `UI`, `Overworld`, and more

---

## 🛠 Requirements

Ensure you have the following installed:
- Python 3.9 or higher
- [Pygame](https://www.pygame.org/news) `pip install pygame`

---

## 📦 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/king-luvaha/super_pirate_game.git
cd super_pirate_game
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install pygame
```

4. **Run the game:**

```bash
python main.py
```

---

## 🎮 How to Play

### Controls

| Key          | Action      |
| ------------ | ----------- |
| `Arrow Keys` | Move around |
| `Space`      | Attack      |
| `Return`     | Enter Level |

---

## 🗂 Project Structure

```
super_pirate_game/
├── assets/               # Game assets (graphics, audio, data)
│   ├── audio/
│   ├── data/
│   │   ├── levels/
│   │   ├── overworld/
│   │   └── tilesets/
│   └── graphics/
│       ├── effects/
│       ├── enemies/
│       ├── items/
│       ├── level/
│       ├── map/
│       ├── objects/
│       ├── overworld/
│       ├── player/
│       ├── tilesets/
│       └── ui/
├── data.py               # Manages player data like coins and health
├── debug.py              # Debugging tools
├── enemies.py            # Enemy AI logic
├── groups.py             # Custom sprite groups for rendering
├── level.py              # Level logic and game loop
├── main.py               # Main entry point
├── overworld.py          # Overworld map and node system
├── player.py             # Player logic and animations
├── settings.py           # Game configuration
├── sprites.py            # Sprite definitions
├── support.py            # Asset loading utilities
├── timer.py              # Timer management
└── ui.py                 # UI elements like hearts and coin counter
```

---

## 🧪 Development Tips

- **Level Maps**: Built using Tiled (.tmx). Customize your `assets/data/levels/` or `assets/data/overworld/`.
- **Assets**: You can swap out graphics in the `assets/graphics` folder without breaking functionality.
- **Game Over**: Triggered automatically when player health reaches 0. Use `R` to retry or `B` to go back to the overworld.

---

## 🧠 Gameplay Summary

- Start on the **overworld map** and move the icon between unlocked nodes.
- Press `Return` to enter a level.
- In the level:
    - Move, avoid obstacles, defeat enemies, and collect coins.
    - Gain 1 heart for every 100 coins collected.
- If your health reaches 0, the game will quit itself.


___

## 💡Tips

- The game saves your current level and unlocked level via the `Data` class.
- Customize levels by editing TMX files in `assets/data/levels/`.
- Add new enemy behaviors or items in `enemies.py` and `sprites.py`.

---

## 📌 Todo / Future Improvements

-  Add main menu and pause menu
-  Add save/load system
-  Add more enemy types and boss fights

---

## 📜 License

This project is open-source and available under the MIT License.

---
