from converters import *
from tkinter import *
from tkinter import filedialog


a = {
    "divider": 1}

window = Tk()

divid = StringVar(window, "{}".format(a["divider"]))

status = StringVar(window, "Choose conversion type") 

def filebrowse():
    status.set("Choosing a file")
    filepath = filedialog.askopenfilename(initialdir = "/", title="Explore files", filetypes=(("Image files", "*.png*"), ("All files", "*.*")))
    status.set("Current file\n{}".format(filepath))
    print(filepath)
    return filepath

def change_divider():
    a["divider"] = int(divid_entry.get())
    print(a["divider"])


window.title('Ascii/Braille image converter')

window.geometry('500x200')

window.config(background = 'gray10')

divid_entry = Entry(window, textvariable=divid, bg="gray35", fg='lightgray')

divid_change = Button(window, text="Submit", command=change_divider, bg="gray35", fg='lightgray')

status_label = Label(window, textvariable=status, width=30, height=2, bg='gray10', fg='lightgray')

divid_info = Label(window,text="Set image resize divider (1 for original size)", width=32, height=1, bg="gray10", fg='lightgray')

button_ascii = Button(window, text="Convert to ascii", command=lambda: ascii_convert(filebrowse(), a["divider"]), bg="gray35", fg='lightgray')

button_braille = Button(window, text="Convert to braille", command=lambda: braille_convert(filebrowse(), a["divider"]), bg="gray35", fg='lightgray')

status_label.grid(column=1, row=1, padx=10, pady=10)
button_braille.grid(column=1, row=2, padx=10, pady=5)
button_ascii.grid(column=1, row=3, padx=10, pady=5)

divid_info.grid(column=2, row=1, padx=10, pady=10)
divid_entry.grid(column=2, row=2, padx=10, pady=10)
divid_change.grid(column=2, row=3, padx=10, pady=10)

window.mainloop()
