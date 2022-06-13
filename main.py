from converters import *
from tkinter import *
from tkinter import filedialog

# Image resolution divider, 10 is default
a = {"divider": 10}

window = Tk()

divid = StringVar(window, "")

divid_display = StringVar(window, f"Set image resize divider (Currently: {a['divider']})")

status = StringVar(window, "Choose conversion type") 

# Function to browse filesystem for an image file
def filebrowse():
    status.set("Choosing a file")
    filepath = filedialog.askopenfilename(initialdir = "/", title="Explore files", 
        filetypes=(
        ("Image files", "*.png"), ("Image files", "*.jpg")
        ))
    if filepath == "":
        status.set("No file chosen currently")
    else:
        status.set(f"Current file\n{filepath}")
    return filepath

# Function that changes the image resolution divider
def change_divider():
    a["divider"] = int(divid_entry.get())
    divid_display.set(f"Set image resize divider (Currently: {a['divider']})")

window.title('Ascii/Braille image converter')
window.geometry('500x200')
window.iconphoto(False, PhotoImage(file="./winicon.png"))
window.config(background = 'gray10')

divid_entry = Entry(window, textvariable=divid, bg="gray35", fg='lightgray')
divid_change = Button(window, text="Submit", command=change_divider, bg="gray35", fg='lightgray')
divid_info = Label(window,textvariable=divid_display, width=32, height=1, bg="gray10", fg='lightgray')

status_label = Label(window, textvariable=status, width=30, height=2, bg='gray10', fg='lightgray')


button_ascii = Button(window, text="Convert to ascii", command=lambda: ascii_convert(filebrowse(), a["divider"]), bg="gray35", fg='lightgray')
button_braille = Button(window, text="Convert to braille", command=lambda: braille_convert(filebrowse(), a["divider"]), bg="gray35", fg='lightgray')

status_label.grid(column=1, row=1, padx=10, pady=10)
button_braille.grid(column=1, row=2, padx=10, pady=5)
button_ascii.grid(column=1, row=3, padx=10, pady=5)

divid_info.grid(column=2, row=1, padx=10, pady=10)
divid_entry.grid(column=2, row=2, padx=10, pady=10)
divid_change.grid(column=2, row=3, padx=10, pady=10)

window.mainloop()
