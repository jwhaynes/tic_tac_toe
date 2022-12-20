# import tkinter tools
from tkinter import *
from tkinter import ttk

# instantiate the gui
root = Tk()

# instantiate a top window frame
frm = ttk.Frame(root, padding = 10)

# provide frame with grid geometry manager
frm.grid()

# create a label widget
ttk.Label(frm, text='GUI LABEL').grid(column = 0, row = 0)

# create a button widget that allows for exiting the gui
ttk.Button(frm, text='EXIT', command = root.destroy).grid(column = 1, row = 0)

# create another frame for playing board and create gride geometry manager
frm_play = ttk.Frame(frm, padding = 10)
frm_play.grid()

# create labels for each part of playing board
label_1 = ttk.Label(frm_play, text = '1').grid(column=0,row=2)
label_2 = ttk.Label(frm_play, text = '2').grid(column=1,row=2)
label_3 = ttk.Label(frm_play, text = '3').grid(column=2,row=2)
label_4 = ttk.Label(frm_play, text = '4').grid(column=0,row=1)
label_5 = ttk.Label(frm_play, text = '5').grid(column=1,row=1)
label_6 = ttk.Label(frm_play, text = '6').grid(column=2,row=1)
label_7 = ttk.Label(frm_play, text = '7').grid(column=0,row=0)
label_8 = ttk.Label(frm_play, text = '8').grid(column=1,row=0)
label_9 = ttk.Label(frm_play, text = '9').grid(column=2,row=0)

# instantiate the event loop
root.mainloop()