import tkinter as tk
import random
from turtle import color

# creating win
win = tk.Tk()

# define win dimension
win.geometry("650x400")

# make win resizable (default = true)
win.resizable(width=True, height=True)

# setting a background color
win.config(bg="#FDE6E5")

# setting the win title
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
            hint = "The number lies between {} & {}".format(choice, upper)
        result += "\n\nHint:\n" + hint
        
    else:
        result = "You guess it coreectly in {} tries".format(retry_attempt)
        guess_button.configure(state="disabled")
        result += "\n\nHint:\n" + "Click 'Play' to start a new round"
    
    update_result(result)

# heading
title = tk.Label(win, text="Guessing Game", font=("Allura", 35, "bold"), fg="#543404", bg="#FDE6E5")

# result and hint
result = tk.Label(win, text="Click Play to start game", font=("Arial", 12, "normal"), fg = "White", bg="#065569", justify=tk.LEFT)

# play button
play_button = tk.Button(win, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
 
# Guess Button
guess_button = tk.Button(win,text="Guess", font=("Arial", 13), state='disabled', fg="#13d675", bg="Black", command=play_game)
 
# Exit Button
exit_button = tk.Button(win, text="Exit Game", font=("Arial", 14), fg="White", bg="#b82741", command=exit)

# entry text box
guessed_number = tk.StringVar()
number_enter = tk.Entry(win, font=("Arial", 11), textvariable=guessed_number)

# label positioning
title.place(x=170, y=50)
result.place(x=180, y=210)
 
# Place the buttons
exit_button.place(x=300, y=320)
guess_button.place(x=350, y=147) 
play_button.place(x=170, y=320)
 
# Place the entry field
number_enter.place(x=180, y=150)
 
# Start the window
win.mainloop()