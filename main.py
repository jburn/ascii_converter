from converters import *
from tkinter import *
from tkinter import filedialog

window = Tk()

divider = 10

divid = StringVar(window, "{}".format(divider))

status = StringVar(window, "Choose a file") 

def filebrowse():
    status.set("Choosing a file")
    filepath = filedialog.askopenfilename(initialdir = "/", title="Explore files", filetypes=(("Image files", "*.png*"), ("All files", "*.*")))
    status.set("Current file {}".format(filepath))
    return filepath

def change_divider(new):
    divider = new


window.title('Ascii/Braille image converter')

window.geometry('800x500')

window.config(background = 'white')

divid_label = Entry(window, textvariable=divid)

divid_change = Button(window, text="Submit", command=lambda: change_divider(divid)

status_label = Label(window, textvariable=status, width=50, height=4)

button_explore = Button(window, text="Browse Files", command=filebrowse)

button_ascii = Button(window, text="Convert to ascii", command=lambda: ascii_convert(filebrowse(), divider))

button_braille = Button(window, text="Convert to braille", command=lambda: braille_convert(filebrowse(), divider))

button_explore.grid(column=2, row=1)
status_label.grid(column=1, row=1)
button_ascii.grid(column=2, row=2)

window.mainloop()

#braille_convert()
