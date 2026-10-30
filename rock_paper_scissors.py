# Rock Paper Scissors Game
# Phase 1: Game Initialization

# Step 1: Import the necessary libraries
import tkinter as tk
import random

# Step 2: Initialize the game window with dimensions and a title
window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors")

# Step 3: Set the background color of the window
window.configure(bg="lightblue")

# Step 4: Create a label for the game title and display it
title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue",
)
title_label.pack(pady=20)

# Step 5: Prompt the user to choose between rock, paper, or scissors
prompt_label = tk.Label(
    window,
    text="Choose: rock, paper, or scissors",
    font=("Arial", 12),
    bg="lightblue",
)
prompt_label.pack(pady=10)

# Step 6: Create an input field for the user to enter their choice
user_input = tk.Entry(window, font=("Arial", 14), justify="center")
user_input.pack(pady=10)

# Step 7: Generate a random selection for the computer
options = ["rock", "paper", "scissors"]

# Step 8: Assign the randomly generated selection to the variable comp_pick
comp_pick = random.choice(options)

# Keeps the window open and waiting for the user
window.mainloop()