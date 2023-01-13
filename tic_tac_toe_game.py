# import tkinter tools
from tkinter import *
from tkinter import ttk

# instantiate the gui
root = Tk()

# instantiate a top window frame
frm = ttk.Frame(root, padding = 10)

# provide frame with grid geometry manager
frm.grid(sticky='nsew')

# create a label widget for game title
ttk.Label(frm, text='Tic Tac Toe').grid(column = 0, row = 0)

# create a frame for player options
frm_player_options = ttk.Frame(frm, padding=10).grid(column=1, row=1,)

# create a label widget for menu section
menu_selection_label = ttk.Label(frm_player_options, text='Player Options').grid(column=1, row=0)

# variables and values for the player selection radio buttons (below)
player1_selection = None

# create radio buttons for selecting who is x and who is o
player1X_player2O_radio_button = ttk.Radiobutton(frm_player_options, text='Player 1: X\nPlayer 2: O', variable=player1_selection, value='X')
player1O_player2X_radio_button = ttk.Radiobutton(frm_player_options, text='Player 1: O\nPlayer 2: X', variable=player1_selection, value='O')

player1X_player2O_radio_button.grid(column=1, row=1)
player1O_player2X_radio_button.grid(column=1, row=2)

# create a button widget that allows for exiting the gui
#ttk.Button(frm, text='EXIT', command = root.destroy).grid(column = 1, row = 0)

# create another frame for playing board and create grid geometry manager
frm_play = ttk.Frame(frm, padding = 10)
frm_play.grid(column = 0, row = 1, sticky='w')
    # make the grid rows/cols have a minimum size
frm_play.columnconfigure([0,2,4],minsize=100)
frm_play.rowconfigure([0,2,4],minsize=100)

# create labels and separators for the playing board
button_1 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=0,row=4)
button_2 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=2,row=4)
button_3 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=4,row=4)
lower_horizontal_separator = ttk.Separator(frm_play, orient=HORIZONTAL).grid(column=0, columnspan=5, row=3, sticky='ew')
button_4 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=0,row=2)
button_5 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=2,row=2)
button_6 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=4,row=2)
upper_horizontal_separator = ttk.Separator(frm_play, orient=HORIZONTAL).grid(column=0,row=1,columnspan=5,sticky='ew')
button_7 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=0,row=0)
button_8 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=2,row=0)
button_9 = ttk.Button(frm_play, text = 'Tic\nTac\nToe').grid(column=4,row=0)

vertical_left_separator = ttk.Separator(frm_play,orient=VERTICAL).grid(column=1, row=0, rowspan=5,sticky='ns')
vertical_right_separator = ttk.Separator(frm_play,orient=VERTICAL).grid(column=3, row=0, rowspan=5, sticky='ns')

# instantiate the event loop
root.mainloop()