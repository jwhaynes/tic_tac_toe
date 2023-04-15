## import tkinter tools and custom classes
from tkinter import *
from tkinter import ttk
from tic_tac_toe_classes import Player, Game

# special board button for tkinter
class tictactoe_button(ttk.Button):
    
    def initialize_button(self, game):
        self.configure(text='\n\n\n', state='!disabled')
        self.configure(command = lambda : self.button_press(game))

    def button_press(self,game):
        
        if game.next_player_turn == 1:
            self.configure(text='\n{symbol}\n\n'.format(symbol=game.p1.symbol), state='disabled')
            game.p1.plays.append(self.id)
            game.play_options.remove(self.id)
            game.next_player_turn = 2
        else:
            self.configure(text='\n{symbol}\n\n'.format(symbol=game.p2.symbol), state='disabled')
            game.p2.plays.append(self.id)
            game.play_options.remove(self.id)
            game.next_player_turn = 1
        
        game.check_for_win()
        if (game.winner != None) and (game.winner == 'CAT'):
            buttons_off(game, buttons)
        elif (game.winner != None):
            buttons_off(game, buttons)



root = Tk() # instantiate the gui

# the following should change name on title bar?
#root.title = "Tic Tac Toe"

## instantiate a top window frame
s_top = ttk.Style()
s_top.configure('top.TFrame',background='blue')

frm = ttk.Frame(root, padding = 10, style='top.TFrame')

## provide frame with grid geometry manager
frm.grid(sticky='nsew')

## create a label widget for game title
title_label = ttk.Label(frm, text='Tic Tac Toe')
title_label.grid(column = 0, row = 0)

## create a frame for player options
s_options = ttk.Style()
s_options.configure('option.TFrame',background='red',relief='sunken')
frm_player_options = ttk.Frame(frm, padding=10, style='option.TFrame')
frm_player_options.grid(column=1, row=1, sticky='e')

## create a label widget for menu section
menu_selection_label = ttk.Label(frm_player_options, text='Player Options')
menu_selection_label.grid(column=1, row=0, pady=5)

# methods, variables and values for the player selection radio buttons (below)
player1_selection = None

def reset_all():
    # function for reset button
    reset_board(buttons)
    start_button.state(['!disabled'])
    player1X_player2O_radio_button.state(['!disabled'])
    player1O_player2X_radio_button.state(['!disabled'])
    turn_indication_label.configure(text='Player turn: ')

def begin_board_game():
    game = Game(player1_selection.get())
    for button in buttons:
        button.initialize_button(game)

    player1X_player2O_radio_button.state(['disabled'])
    player1O_player2X_radio_button.state(['disabled'])
    start_button.state(['disabled'])
    turn_indication_label.configure(text='Player turn: Player {num}'.format(num=game.next_player_turn))
    reset_button.state(['!disabled'])
        


## create radio buttons for selecting who is x and who is o and define associated variable
player1_selection = StringVar()
player1X_player2O_radio_button = ttk.Radiobutton(frm_player_options, text='Player 1: X\nPlayer 2: O', variable=player1_selection, value='X')
player1O_player2X_radio_button = ttk.Radiobutton(frm_player_options, text='Player 1: O\nPlayer 2: X', variable=player1_selection, value='O')

player1X_player2O_radio_button.grid(column=1, row=1)
player1O_player2X_radio_button.grid(column=1, row=2)

## create a start button to begin a game
start_button = ttk.Button(frm_player_options, text='START', command=begin_board_game)
start_button.grid(column=1,row=3,pady=5)

## create a reset button to reset board
reset_button = ttk.Button(frm_player_options, text='RESET BOARD', state = 'disabled', command=reset_all)
reset_button.grid(column=1, row=4, pady=5)

## create a label that displays whose turn it is
turn_indication_label = ttk.Label(frm_player_options, text='Player turn: ')
turn_indication_label.grid(column=1,row=5,pady=5)

# create a button widget that allows for exiting the gui
#ttk.Button(frm, text='EXIT', command = root.destroy).grid(column = 1, row = 0)

## create another frame for playing board and create grid geometry manager
s_play = ttk.Style()
s_play.configure('play.TFrame',background='purple')
frm_play = ttk.Frame(frm, padding = 10, style='play.TFrame')
frm_play.grid(column = 0, row = 1, sticky='w')
    # make the grid rows/cols have a minimum size
frm_play.columnconfigure([0,2,4],minsize=100, weight=1)
frm_play.rowconfigure([0,2,4],minsize=100, weight=1)

## create labels and separators for the playing board
button_names = ['button_' + str(num) for num in range(1,10)] # list of names used for board buttons
buttons = [] # list that will hold button objects
all_vars = vars() # handle for global variables dictionary
rows = (4,2,0) # rows in grid that buttons will be put
cols = (0,2,4) # columns in grid that buttons will be put
combos = [] # list to hold tuples of column, row combinations
for row in rows: # nested loop to create col,row combos
    for col in cols:
        combos.append((col,row))

for name in button_names: # loop to create button, add button to button list, place button in grid, give button id property
    all_vars[name] = tictactoe_button(frm_play, text = 'Tic\nTac\nToe', state = 'disabled')
    buttons.append(all_vars[name])
    num = len(buttons) - 1
    all_vars[name].grid(column=combos[num][0],row=combos[num][1])
    all_vars[name].id = int(name[-1])

def buttons_off(game, buttons):
    for button in buttons:
            button.configure(state = 'disabled')

def reset_board(buttons):
    for button in buttons:
        button.configure(text = 'Tic\nTac\nToe', state = 'disabled')

## create separators for the playing board and place them
lower_horizontal_separator = ttk.Separator(frm_play, orient=HORIZONTAL)
upper_horizontal_separator = ttk.Separator(frm_play, orient=HORIZONTAL)
vertical_left_separator = ttk.Separator(frm_play,orient=VERTICAL)
vertical_right_separator = ttk.Separator(frm_play,orient=VERTICAL)

lower_horizontal_separator.grid(column=0, columnspan=5, row=3, sticky='ew')
upper_horizontal_separator.grid(column=0,row=1,columnspan=5,sticky='ew')
vertical_left_separator.grid(column=1, row=0, rowspan=5,sticky='ns')
vertical_right_separator.grid(column=3, row=0, rowspan=5, sticky='ns')

## instantiate the event loop
root.mainloop()