# import tkinter tools
from tkinter import *
from tkinter import ttk

# instantiate the gui
root = Tk()

# instantiate a top window frame
frm = ttk.Frame(root, padding = 10)

# provide frame with grid geometry manager
frm.grid(sticky='nsew')

# create a label widget
ttk.Label(frm, text='GUI LABEL').grid(column = 0, row = 0)

# create a button widget that allows for exiting the gui
ttk.Button(frm, text='EXIT', command = root.destroy).grid(column = 1, row = 0)

# create another frame for playing board and create grid geometry manager
frm_play = ttk.Frame(frm, padding = 10)
frm_play.grid(sticky='nsew')
    # make the grid rows/cols have a minimum size
frm_play.columnconfigure([0,1,2,3],minsize=25)
frm_play.rowconfigure([0,2,3],minsize=25)

# create labels and separators for the playing board
label_1 = ttk.Label(frm_play, text = '1').grid(column=0,row=4)
label_2 = ttk.Label(frm_play, text = '2').grid(column=2,row=4)
label_3 = ttk.Label(frm_play, text = '3').grid(column=4,row=4)
lower_horizontal_separator = ttk.Separator(frm_play, orient=HORIZONTAL).grid(column=0, columnspan=5, row=3, sticky='ew')
label_4 = ttk.Label(frm_play, text = '4').grid(column=0,row=2)
label_5 = ttk.Label(frm_play, text = '5').grid(column=2,row=2)
label_6 = ttk.Label(frm_play, text = '6').grid(column=4,row=2)
upper_horizontal_separator = ttk.Separator(frm_play, orient=HORIZONTAL).grid(column=0,row=1,columnspan=5,sticky='ew')
label_7 = ttk.Label(frm_play, text = '7').grid(column=0,row=0)
label_8 = ttk.Label(frm_play, text = '8').grid(column=2,row=0)
label_9 = ttk.Label(frm_play, text = '9').grid(column=4,row=0)

vertical_left_separator = ttk.Separator(frm_play,orient=VERTICAL).grid(column=1, row=0, rowspan=5,sticky='ns')
vertical_right_separator = ttk.Separator(frm_play,orient=VERTICAL).grid(column=3, row=0, rowspan=5, sticky='ns')

# instantiate the event loop
root.mainloop()