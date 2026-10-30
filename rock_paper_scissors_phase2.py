# Rock Paper Scissors Game
# Phase 2: User Interactions (builds on Phase 1)

import tkinter as tk
import random

# ---------- Phase 1: Game Initialization ----------
window = tk.Tk()
window.geometry("400x400")
window.title("Rock Paper Scissors")
window.configure(bg="lightblue")

title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue",
)
title_label.pack(pady=20)

prompt_label = tk.Label(
    window,
    text="Choose: rock, paper, or scissors",
    font=("Arial", 12),
    bg="lightblue",
)
prompt_label.pack(pady=10)

user_input = tk.Entry(window, font=("Arial", 14), justify="center")
user_input.pack(pady=10)

options = ["rock", "paper", "scissors"]
comp_pick = random.choice(options)

# Label used to show the computer's pick and the result of the game
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="lightblue",
    fg="darkgreen",
)
result_label.pack(pady=15)


# ---------- Phase 2: User Interactions ----------

# Step 1: Define a function called play() to handle the game logic
def play():
    global comp_pick

    user_pick = user_input.get().strip().lower()

    # Check that the user typed a valid choice
    if user_pick not in options:
        result_label.config(
            text="Invalid choice! Type rock, paper, or scissors.",
            fg="red",
        )
        return

    # Step 2: Conditional statements to determine the winner
    if user_pick == comp_pick:
        outcome = "It's a draw!"
    elif user_pick == "rock" and comp_pick == "scissors":
        outcome = "You win! Rock blunts scissors."
    elif user_pick == "scissors" and comp_pick == "paper":
        outcome = "You win! Scissors cut paper."
    elif user_pick == "paper" and comp_pick == "rock":
        outcome = "You win! Paper covers rock."
    else:
        outcome = "Computer wins!"

    result_label.config(
        text=f"Computer chose: {comp_pick}\n{outcome}",
        fg="darkgreen",
    )

    # Pick a new computer choice ready for the next round
    comp_pick = random.choice(options)


# Step 3: Define a function called Reset() to reset the game
def Reset():
    global comp_pick
    user_input.delete(0, tk.END)      # clear the input field
    result_label.config(text="")      # clear the result
    comp_pick = random.choice(options)  # new computer choice


# Step 4: Define a function called Exit() to exit the application
def Exit():
    window.destroy()


# ---------- Buttons so the functions can be tested ----------
play_button = tk.Button(window, text="Play", font=("Arial", 12), width=10, command=play)
play_button.pack(pady=5)

reset_button = tk.Button(window, text="Reset", font=("Arial", 12), width=10, command=Reset)
reset_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", font=("Arial", 12), width=10, command=Exit)
exit_button.pack(pady=5)

window.mainloop()