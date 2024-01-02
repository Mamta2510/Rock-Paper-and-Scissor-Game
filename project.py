from tkinter import *
import tkinter.font as font
import random

# player_score = 0
# computer_score = 0
# options = [('rock',0), ('paper',1), ('scissors',2)]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


# Function for when a button is clicked
def on_button_click(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    computer_score_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    player_score_label.config(text=f"Player chose: {player_choice}\n{result}")


game_window = Tk()
game_window.title("Rock Paper Scissors Game")

app_font = font.Font(size = 12)

#Displaying Game Title
game_title = Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), fg = 'grey')
game_title.pack()

#Label to dispay, who wins each time
winner_label = Label(text = "Let's Start the Game...", fg = 'green', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, pady = 5, command = lambda: on_button_click("rock"))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, pady = 5, command = lambda: on_button_click("paper"))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, pady = 5, command = lambda: on_button_click("scissors"))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)




#Displaying Score and players choise
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'You Selected : ---', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'You Score : -', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

game_window.geometry('700x300')
game_window.mainloop()