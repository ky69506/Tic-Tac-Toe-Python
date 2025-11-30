# 🎮 Tic-Tac-Toe Game

This is a simple, console-based Tic-Tac-Toe game written in Python using Object-Oriented Programming (OOP). It allows two players to compete against each other, tracking their scores across multiple rounds.

---

## 🌟 Features

* **Two-Player Mode:** Designed for two human players to compete.
* **Custom Names & Symbols:** Each player can choose their own name and playing symbol (X, O, or any other single letter).
* **Score Tracking:** The game keeps score for each player and announces the winner of each round.
* **Clear Menus:** Includes a main menu (Start/Quit) and an end-game menu (Play Again/Quit).
* **Clean Interface:** The screen is cleared after each turn to display the updated board clearly.
* **Input Validation:** The game validates user input to prevent errors (e.g., choosing an occupied cell, invalid symbols, or out-of-range moves).

---

## 🚀 How to Run

To run this game, you only need a Python 3 interpreter.

1.  **Save the File:** Save the code in a file with a `.py` extension (e.g., `main.py`).
2.  **Open Terminal:** Open your terminal or Command Prompt.
3.  **Navigate to Directory:** Use the `cd` command to navigate to the folder where you saved the file.
4.  **Run the Script:** Type the following command and press Enter:

```bash
python main.py
```

Or, if you need to specify Python 3:

```bash
python3 main.py
```

---

## 🏗️ Code Structure

The code is divided into several classes to separate responsibilities:

* **`clear_screen()` (Function):**
    * A simple helper function that uses `os.system` to clear the console screen (works on Windows, Linux, and macOS).

* **`Menu` (Class):**
    * Contains `static` methods to display the menus (main and end-game) and get the user's choice.

* **`Player` (Class):**
    * A data class to store player information: `name`, `symbol`, and `score`.

* **`Board` (Class):**
    * Manages everything related to the game board.
    * `reset()`: Clears the board for a new game.
    * `display()`: Prints the current state of the board to the console.
    * `place_symbol()`: Places a player's symbol on a specific cell.
    * `check_win()`, `is_full()`: Checks for win or draw conditions.

* **`Game` (Class):**
    * The main class that connects everything.
    * `setup_players()`: Asks players for their names and symbols.
    * `play_turn()`: Manages the current player's turn and validates their move.
    * `game_loop()`: The loop that runs a single round of the game until a win or draw.
    * `start()`: The main program loop that shows menus and handles replaying.

* **Execution (`Game().start()`):**
    * The final line of the script, which creates an instance of the `Game` class and starts the game.
