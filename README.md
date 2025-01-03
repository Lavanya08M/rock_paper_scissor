# Rock-Paper-Scissors Game

This repository contains a simple Python implementation of the classic Rock-Paper-Scissors game. The user can play against the computer, with the computer's choice being randomly generated. The program tracks the total games played, as well as wins for both the user and the computer.

---

## Features

- **Interactive Gameplay**: Input your choice of "Rock", "Paper", or "Scissors".
- **Random Computer Opponent**: The computer makes a random choice each round.
- **Score Tracking**: Tracks and displays wins, losses, and ties.
- **Game Summary**: Provides a summary of the results when the game ends.
- **Replay Prompt**: The user can play multiple rounds or quit the game.

---

## How to Run the Program

1. **Prerequisites**:
   - Python 3.x installed on your system.

2. **Download the Code**:
   - Clone the repository or download the script file.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Execute the script using the command:
     ```
     python rock_paper_scissors.py
     ```

---

## Game Instructions

1. When prompted, type one of the following choices:
   - `Rock`
   - `Paper`
   - `Scissors`
   - Or type `Q` to quit the game.

2. The computer's choice will be displayed.

3. The program determines the winner based on the classic rules:
   - Rock beats Scissors.
   - Scissors beats Paper.
   - Paper beats Rock.
   - Same choices result in a tie.

4. After quitting, the program provides a summary of the results.

---

## Example Gameplay

```
Type Rock/Paper/Scissors or Q to quit: rock
Computer guess: scissors
You won!

Type Rock/Paper/Scissors or Q to quit: paper
Computer guess: rock
You won!

Type Rock/Paper/Scissors or Q to quit: q
You won 2 times.
Computer won 0 times.
"You are the Winner."
Thank you! For Playing.
Good Bye!
```

---

## Code Structure

The program is organized into two main functions:

1. **`main()`**:
   - Handles the game loop, user input, and determining the winner for each round.

2. **`print_summary()`**:
   - Displays the summary of the game results when the user quits.

---

## Contributions

Feel free to contribute by suggesting improvements, reporting bugs, or creating pull requests. 

---
