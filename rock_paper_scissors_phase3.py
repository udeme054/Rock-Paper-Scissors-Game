# Rock Paper Scissors Game
# Phase 3: Application Execution (complete game: Phases 1 + 2 + 3)

import tkinter as tk
import random

# ---------- Phase 1: Game Initialization ----------
root = tk.Tk()
root.geometry("450x400")
root.title("Rock Paper Scissors")
root.configure(bg="lightblue")

title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue",
)

prompt_label = tk.Label(
    root,
    text="Choose: rock, paper, or scissors",
    font=("Arial", 12),
    bg="lightblue",
)

user_input = tk.Entry(root, font=("Arial", 14), justify="center")

options = ["rock", "paper", "scissors"]
comp_pick = random.choice(options)

# This variable holds the game result and is bound to the result Entry field
Result = tk.StringVar()


# ---------- Phase 2: User Interactions ----------
def play():
    global comp_pick

    user_pick = user_input.get().strip().lower()

    if user_pick not in options:
        Result.set("Invalid choice! Type rock, paper, or scissors.")
        return

    if user_pick == comp_pick:
        outcome = "It's a draw!"
    elif user_pick == "rock" and comp_pick == "scissors":
        outcome = "You win!"
    elif user_pick == "scissors" and comp_pick == "paper":
        outcome = "You win!"
    elif user_pick == "paper" and comp_pick == "rock":
        outcome = "You win!"
    else:
        outcome = "Computer wins!"

    Result.set(f"Computer chose {comp_pick}. {outcome}")

    # New computer choice for the next round
    comp_pick = random.choice(options)


def Reset():
    global comp_pick
    user_input.delete(0, tk.END)
    Result.set("")
    comp_pick = random.choice(options)


def Exit():
    root.destroy()


# ---------- Phase 3: Application Execution ----------

# Step 1: Create an entry field to display the game result.
#         Bind it to the Result variable using textvariable.
result_entry = tk.Entry(
    root,
    textvariable=Result,
    font=("Arial", 12, "bold"),
    justify="center",
)

# Step 2: Define the PLAY button and bind it to the play() function
play_button = tk.Button(
    root,
    text="PLAY",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=play,
)

# Step 3: Define the RESET button and bind it to the Reset() function
reset_button = tk.Button(
    root,
    text="RESET",
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="white",
    command=Reset,
)

# Step 4: Define the EXIT button and bind it to the Exit() function
exit_button = tk.Button(
    root,
    text="EXIT",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=Exit,
)

# Step 5: Place the buttons and the result entry field at their positions
title_label.place(x=75, y=20)
prompt_label.place(x=110, y=85)
user_input.place(x=125, y=125, width=200)
result_entry.place(x=50, y=190, width=350, height=35)
play_button.place(x=40, y=270, width=100, height=40)
reset_button.place(x=175, y=270, width=100, height=40)
exit_button.place(x=310, y=270, width=100, height=40)

# Step 6: Run the application
root.mainloop()