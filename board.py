from tkinter import *
import random
import time

def new_game():
    global player
    global test_spots
    global first_play
    global prev_comp_row
    global prev_comp_column

    label.config(text=(players[0]+ " Turn"))

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
        
    player = players[0]
    test_spots = [["", "", ""],
                  ["", "", ""],
                   ["", "", ""]]
    
    first_play = True
    prev_comp_row = 0
    prev_comp_column = 0
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] and buttons[row][0]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] and buttons[0][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] and buttons[0][0]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] and buttons[0][2]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False
    
def check_winner_human():
    for row in range(3):
        if test_spots[row][0] == test_spots[row][1] == test_spots[row][2] and test_spots[row][0] == players[0]:
            return True
    
    for column in range(3):
        if test_spots[0][column] == test_spots[1][column] == test_spots[2][column] and test_spots[0][column] == players[0]:
            return True
        
    if test_spots[0][0] == test_spots[1][1] == test_spots[2][2] and test_spots[0][0] == players[0]:
        return True
    
    elif test_spots[0][2] == test_spots[1][1] == test_spots[2][0] and test_spots[0][2] == players[0]:
        return True
    
    else:
        return False
    
def check_winner_computer():
    for row in range(3):
        if test_spots[row][0] == test_spots[row][1] == test_spots[row][2] and test_spots[row][0] == players[1]:
            return True
    
    for column in range(3):
        if test_spots[0][column] == test_spots[1][column] == test_spots[2][column] and test_spots[0][column] == players[1]:
            return True
        
    if test_spots[0][0] == test_spots[1][1] == test_spots[2][2] and test_spots[0][0] == players[1]:
        return True
    
    elif test_spots[0][2] == test_spots[1][1] == test_spots[2][0] and test_spots[0][2] == players[1]:
        return True
    
    else:
        return False
    
def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            check = check_winner()
            
            if check is False:
                player = players[1]
                label.config(text=(players[1]+ " turn"))
            
            elif check is True:
                label.config(text=(players[0]+ " wins"))

            elif check == "Tie":
                label.config(text=("Tie"))

        else:
            buttons[row][column]['text'] = player
            check = check_winner()
            
            if check is False:
                player = players[0]
                label.config(text=(players[0]+ " turn"))
            
            elif check is True:
                label.config(text=(players[1]+ " wins"))

            elif check == "Tie":
                label.config(text=("Tie"))

def next_turn_computer(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        
            buttons[row][column]['text'] = player
            test_spots[row][column] = player

            check = check_winner()
            
            if check is False:
                player = players[1]
                label.config(text=(players[1]+ " turn"))
            
            elif check is True:
                label.config(text=(players[0]+ " wins"))
                return

            elif check == "Tie":
                label.config(text=("Tie"))

            computer_pick()

            check = check_winner()
            
            if check is False:
                player = players[0]
                label.config(text=(players[0]+ " Turn"))
            
            elif check is True:
                label.config(text=(players[1]+ " Wins!"))

            elif check == "Tie":
                label.config(text=("Tie"))

first_play = True
def computer_pick():
    global first_play
    global prev_comp_row
    global prev_comp_column
    blocked = False

    if first_play is False:
    # check for possible win
        for row in range(3):
            for column in range(3):
                if test_spots[row][column] == "":
                    test_spots[row][column] = players[1]

                    # when new game is played and won, computer must block that spot
                    if check_winner_computer():
                        buttons[row][column]['text'] = players[1]
                        test_spots[row][column] = players[1]
                        blocked = True
                        prev_comp_row = row
                        prev_comp_column = column
                        return

                    test_spots[row][column] = ""

        # replace every empty square with opponent's character
        for row in range(3):
            for column in range(3):
                if test_spots[row][column] == "":
                    test_spots[row][column] = players[0]

                    # when new game is played and won, computer must block that spot
                    if check_winner_human():
                        buttons[row][column]['text'] = players[1]
                        test_spots[row][column] = players[1]
                        blocked = True
                        prev_comp_row = row
                        prev_comp_column = column
                        return

                    test_spots[row][column] = ""

    # opponent does not have a play to win next play
    if not blocked:
        # place computer's character in middle squares
        if first_play is True:
            # no longer first type
            first_play = False

            if buttons[1][1]['text'] == players[0]:
                play_type = 1
            else:
                play_type = random.randint(0,1)

            # take middle square 50% of the time and opposite square other 50%
            # if the middle sqaure is not already take, then opposite square 100%
            if play_type == 0:
                buttons[1][1]['text'] = players[1]
                test_spots[1][1] = players[1]
                prev_comp_row = 1
                prev_comp_column = 1
                return
            else:
                for row in range(3):
                    for column in range(3):
                        if buttons[row][column]['text'] == players[0]:
                            match row:
                                case 0:
                                    row = 2
                                case 1:
                                    row = 0
                                case 2:
                                    row = 0
                            
                            match column:
                                case 0:
                                    column = 2
                                case 1:
                                    column = 0
                                case 2:
                                    column = 0
                            
                            buttons[row][column]['text'] = players[1]
                            test_spots[row][column] = players[1]
                            prev_comp_row = row
                            prev_comp_column = column
                            return

        else:
            # check to see if middle square is already taken, if not take square
            if buttons[1][1] == "":
                buttons[1][1] = players[1]
                prev_comp_row = 1
                prev_comp_column = 1
                return

            # when previous row is greater than 0, checks each possible space above
            if prev_comp_row > 0:
                if buttons[prev_comp_row - 1][prev_comp_column]['text'] == "":
                    buttons[prev_comp_row - 1][prev_comp_column]['text'] = players[1]
                    test_spots[prev_comp_row - 1][prev_comp_column] = players[1]
                    prev_comp_row -= 1                  

                elif prev_comp_column > 0:
                    if buttons[prev_comp_row - 1][prev_comp_column - 1]['text'] == "":
                        buttons[prev_comp_row - 1][prev_comp_column - 1]['text'] = players[1]
                        test_spots[prev_comp_row - 1][prev_comp_column - 1] = players[1]
                        prev_comp_row -= 1
                        prev_comp_column -= 1

                elif prev_comp_column < 2:
                    if buttons[prev_comp_row - 1][prev_comp_column + 1]['text'] == "":
                        buttons[prev_comp_row - 1][prev_comp_column + 1]['text'] = players[1]
                        test_spots[prev_comp_row - 1][prev_comp_column + 1] = players[1]
                        prev_comp_row -= 1
                        prev_comp_column += 1

            # when previous row is less than 2, checks each possible space below
            elif prev_comp_row < 2:
                if buttons[prev_comp_row + 1][prev_comp_column]['text'] == "":
                    buttons[prev_comp_row + 1][prev_comp_column]['text'] = players[1] 
                    test_spots[prev_comp_row + 1][prev_comp_column] = players[1]
                    prev_comp_row += 1                   

                elif prev_comp_column > 0:
                    if buttons[prev_comp_row + 1][prev_comp_column - 1]['text'] == "":
                        buttons[prev_comp_row + 1][prev_comp_column - 1]['text'] = players[1]
                        test_spots[prev_comp_row + 1][prev_comp_column - 1] = players[1]
                        prev_comp_row += 1
                        prev_comp_column -= 1

                elif prev_comp_column < 2:
                    if buttons[prev_comp_row + 1][prev_comp_column + 1]['text'] == "":
                        buttons[prev_comp_row + 1][prev_comp_column + 1]['text'] = players[1]
                        test_spots[prev_comp_row + 1][prev_comp_column + 1] = players[1]
                        prev_comp_row += 1
                        prev_comp_column += 1

            # when previous column is less than 2, checks possible space to the right
            elif prev_comp_column < 2:
                if buttons[prev_comp_row][prev_comp_column + 1]['text'] == "":
                    buttons[prev_comp_row][prev_comp_column + 1]['text'] = players[1]
                    test_spots[prev_comp_row][prev_comp_column + 1] = players[1]
                    prev_comp_column += 1
            
            # when previous column is greater than 0, checks possible space to the left
            elif prev_comp_column > 0:
                if buttons[prev_comp_row][prev_comp_column - 1]['text'] == "":
                    buttons[prev_comp_row][prev_comp_column - 1]['text'] = players[1]
                    test_spots[prev_comp_row][prev_comp_column - 1] = players[1]
                    prev_comp_column -= 1
            
            return
                    
# check win case


            
    
        




def ok():
    if(number_players.get() == "One"):
        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda row=row, column=column: next_turn_computer(row, column))
                buttons[row][column].grid(row=row, column=column)
    elif(number_players.get() == "Two"):
        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
                buttons[row][column].grid(row=row, column=column)
 
buttons = [[0, 0, 0],
           [0, 0, 0],
            [0, 0, 0]]

test_spots = [["", "", ""],
              ["", "", ""],
               ["", "", ""]]
window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = "X"

prev_comp_row = 0
prev_comp_column = 0

label = Label(text=player + " Turn", font=('consolas', 40))
label.pack(side = "top")

reset_botton = Button(text="restart", font=('consolas', 20), command=new_game)
reset_botton.pack(side = "top")

number_players = StringVar(window)
number_players.set("Pick number of Players")
dropdown_player = OptionMenu(window, number_players, "One", "Two")
dropdown_player.pack()

ok_button = Button(window, text="Ok", command=ok)
ok_button.pack()

frame = Frame(window)
frame.pack()

window.mainloop()
