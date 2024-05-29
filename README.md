# Snake Game

This is a Python implementation of the classic Snake game from the Nokia 3310, using the Turtle graphics package. In this game, you control a snake that moves around the screen, eating food to grow longer. The objective is to avoid running into the walls or the snake's own body while trying to grow as long as possible.

## Features

- Classic Snake gameplay inspired by the Nokia 3310 version.
- Simple and intuitive controls using the keyboard.
- Realistic snake movement and collision detection.
- Score tracking to keep track of the highest score.
- Minimalistic graphics using the Turtle package.

## Installation

To run this game, you need to have Python installed on your system. Additionally, you need the Turtle package, which is included in the standard Python library.

## How to Play

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the directory containing the game files.
3. Run the game by executing the following command:

   ```bash
   python main.py
   ```

### Controls

- Move Up: `Up Arrow` key
- Move Down: `Down Arrow` key
- Move Left: `Left Arrow` key
- Move Right: `Right Arrow` key

### Objective

- The objective of the game is to eat the food that appears on the screen to grow longer.
- Avoid running into the walls or the snake's own body.
- Try to achieve the highest score possible.

## Code Overview

The game consists of several main components:

- `snake_game.py`: The main script that initializes the game and runs the game loop.
- `snake.py`: Contains the Snake class, responsible for creating and controlling the snake.
- `food.py`: Contains the Food class, responsible for creating and placing the food on the screen.
- `scoreboard.py`: Contains the Scoreboard class, responsible for displaying and updating the score.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This game was created using the Turtle graphics package, a standard Python library for creating graphics.
- Inspired by the original Snake game on the Nokia 3310.

Enjoy playing the Snake Game! Feel free to report any issues or suggest enhancements.
