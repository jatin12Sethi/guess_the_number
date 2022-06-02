import tkinter as tk
import random
from turtle import color

# creating window
win = tk.Tk()

# define window dimension
win.geometry("700x400")

# make window resizable (default = true)
win.resizable(width=True, height=True)

# setting a background color
win.config(bg="#FDE6E5")

# setting the window title
win.title("Guess the Number")

# making the main GUI
# setting the lower and upper bound
lower = int(input("Enter the lower bound:\t"))
upper = int(input("Enter the upper bound:\t"))


target = random.randint(lower, upper)
retry_attempt = 0

def update_result(text):
    result.configure(text=text)
    
# creating new game
def new_game():
    guess_button.configure(state="normal")
    global target, retry_attempt
    target = random.randint(lower, upper)
    retry_attempt = 0
    update_result(text="Guess a number between\n1 and 100")

# continue or terminate
def play_game():
    global retry_attempt
    
    choice = int(number_enter.get())
    
    if choice != target:
        retry_attempt += 1
        
        result = "Your guess is incorrect. Try Again!"
        if target < choice:
            hint = "The number lies between 0 & {}".format(result)
            
        else:
            hint = "The number lies between {} & 1000".format(choice)
        result += "\n\nHint:\n" + hint
        
    else:
        result = "You guess it coreectly in {} tries".format(retry_attempt)
        guess_button.configure(state="disabled")
        result += "\n\nHint:\n" + "Click 'Play' to start a new round"
        