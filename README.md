# Rock Paper Scissors Game 

A single-player Rock Paper Scissors game built with Python and Tkinter. The player types a choice, the computer picks at random, and the game shows who won.

## Game Rules

- Rock blunts scissors, so **rock wins**.
- Scissors cut paper, so **scissors win**.
- Paper covers rock, so **paper wins**.
- If both choices are the same, the round is a **draw**.

## Features

- Simple graphical interface built with Tkinter
- Random computer choice every round
- Result displayed in a dedicated result field
- Input validation for invalid choices
- **PLAY**, **RESET**, and **EXIT** buttons

## Technologies Used

- Python 3
- `tkinter` for the graphical user interface
- `random` for the computer's choice

## Project Structure

| File | Description |
|---|---|
| `rock_paper_scissors_phase1.py` | Phase 1: Game initialization (window, title, input field, computer pick) |
| `rock_paper_scissors_phase2.py` | Phase 2: User interactions (`play()`, `Reset()`, `Exit()` functions) |
| `rock_paper_scissors_phase3.py` | Phase 3: Application execution (final, complete game) |

## Development Phases

1. **Game Initialization:** import the libraries, create the window with a size, title, and background color, add the title label, the prompt, and the input field, and generate the computer's choice (`comp_pick`).
2. **User Interactions:** define `play()` with conditional statements to decide the winner, `Reset()` to restart the game, and `Exit()` to close the application.
3. **Application Execution:** add the result entry field (bound to the `Result` variable), create the PLAY, RESET, and EXIT buttons, place the widgets in the window, and start the app with `root.mainloop()`.

## Requirements

- Python 3.8 or higher
- Tkinter (included with the standard Python installation on Windows and macOS)

On some Linux systems, Tkinter must be installed separately:

```bash
sudo apt install python3-tk
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/rock-paper-scissors-game.git
   ```

2. Open the project folder:

   ```bash
   cd rock-paper-scissors-game
   ```

3. Run the final version of the game:

   ```bash
   python rock_paper_scissors_phase3.py
   ```

## How to Play

1. Type `rock`, `paper`, or `scissors` in the input field.
2. Click **PLAY** to see the computer's choice and the result.
3. Click **RESET** to clear the game and start again.
4. Click **EXIT** to close the application.

## Author

**Udeme Jackson**
GOMYCODE Student

## Acknowledgements

This project was completed as a Lab Phase project at GOMYCODE.

