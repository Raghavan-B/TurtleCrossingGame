# Turtle Crossing Game

This project is a Turtle Crossing game, inspired by the popular game Crossy Road. It serves as a capstone project, testing various concepts in object-oriented programming (OOP) and game development using Python's Turtle module.

## Overview

The Turtle Crossing game is a simple yet engaging game where the player controls a turtle that must cross a busy, multi-lane highway filled with randomly generated cars. The goal is to reach the other side of the screen without getting hit by a car. As the player progresses, the difficulty increases as the cars speed up.

## Features

- **Object-Oriented Design:** The game is structured using OOP principles, with multiple classes representing different elements of the game.
- **Progressive Difficulty:** As the player successfully crosses the road, the cars move faster, making the game more challenging.
- **Simple Graphics:** Utilizes the Turtle module for creating a visually simple yet effective gaming experience.
- **Game Over Detection:** The game ends when the turtle collides with a car.

## Installation

To run this game, you'll need Python installed on your system. You can install the required modules using the following command:

```bash
pip install turtle
```

## Usage

1. Clone this repository or download the files.
2. Run the main Python file to start the game.

```bash
python main.py
```

## Files Description

- **main.py:** The main file that initializes the game, sets up the screen, and manages the game loop.
- **player.py:** Contains the `Player` class that defines the turtle's movement and behavior.
- **car_manager.py:** Contains the `CarManager` class that handles the creation, movement, and collision detection of the cars.
- **scoreboard.py:** Contains the `Scoreboard` class that tracks the player's progress and displays the score.

## Concepts Covered

This project reinforces several key concepts:

- **Class Creation and Inheritance:** Understanding how to create and inherit classes.
- **Object Usage:** Managing objects created from classes within the game environment.
- **Turtle Coordinate System:** Utilizing the Turtle module's coordinate system to control object movement.
- **Game Engine Basics:** Implementing basic game mechanics such as collision detection and game loops.
