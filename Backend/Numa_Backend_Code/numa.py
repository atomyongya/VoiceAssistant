from tkinter import *
from tkinter.ttk import *
# from PIL import ImageTk, Image

def numa_gui():
    # Declearing window of the application
    window = Tk()
    window.configure(background='Purple')
    window.geometry('500x500')
    window.title("Numa")

    # Creating a drop down menu to select language
    language = ["English", "Nepali"]
    combo = Combobox(window, value=language, width=10)
    combo.place(relx=0.02, rely=0.02)
    combo.current(0)

    # creating text field to know what they are taking
    entryBox = Entry(window)
    entryBox.place(relx=0.5, rely=0.3, width=400, height=40, anchor=CENTER)

    # Creating canvas for microphone 
    canvas = Canvas(window, width=80, height=140)
    canvas.configure(background='Purple')
    # img = Image.open("./image/microphone2.png")
    # resized = img.resize((80, 140), Image.ANTIALIAS)
    # img2 = ImageTk.PhotoImage(resized)
    # canvas.create_image(0, 0, anchor=NW, image=img2)
    canvas.place(relx=0.5, rely=0.55,  anchor=CENTER)

    # Shoving it onto the Screen
    window.mainloop()