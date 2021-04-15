
from tkinter import *
from PIL import Image,ImageTk

import CaptureImage
import Sheets

path = r"/Users/admin/VScode/Mini-Project-III-Python/Mini-Module/Resources/"


def start_button_function():
    
    window.destroy()
    
    CaptureImage.Capture("peta")
    
    return
    
# Main Screen i.e. first Screen when the code is executed 

window = Tk()

# All the properties of the first screen is set here:

window.title('Smart Car Parking System')
window.iconbitmap(path + 'car.ico')
window.configure(background = "black")

heading = Label(window, text = 'Smart Car Parking System', bg = "black", fg = "white",font = "Perpetua 24 bold")
heading.grid(row = 0,column = 0)

frame = LabelFrame(window,padx = 100, pady = 50)
frame.grid(padx = 10, pady = 10)
frame.configure(background = "white")

deathwing = Image.open(path + 'smart.png')
image = deathwing.resize((455,307),Image.ANTIALIAS)
Deathwing = ImageTk.PhotoImage(image)
imagelabel = Label(frame,image = Deathwing,borderwidth = 0)
imagelabel.grid(row = 0,column = 0)

start_img = PhotoImage(file = path + "start.png")
start_button = Button(frame,image = start_img, command = start_button_function, height = 120, width = 190, bg = "white",borderwidth = 0)
start_button.image = start_img
start_button.grid(row = 1,column = 0)

# Exit Button Properties:

exit_img = PhotoImage(file = path + "exit.png")
exit_button = Button(window,image = exit_img,command = window.quit ,height = 50 , width = 50, bg = "white",borderwidth = 0)
exit_button.image = exit_img
exit_button.place(x = 18,y = 490)

window.mainloop()