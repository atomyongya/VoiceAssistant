""" Frontend of Numa """

# Importing Inbuilt Module/Library.
from tkinter import *
from PIL import ImageTk, Image

class Numa_GUI():
    """
    Graphical User Interface of "Numa" Voice Assistant.
    """
    
    def __init__(self, root):
        """
        Constructor Function.
        
        :var root : Main Widgets/Window of system which hold other sub widgets.
        """

        self.root = root
        
    def numa_gui(self):
        """
        numa_gui method that hold sub widgets.
        """
        self.root = Tk()
        self.root.title("Numa")
        self.root.geometry("800x400")
        my_Label = Label(self.root, text="Hello World").grid(row=5, column=1)
        
        # Run the loop to display unitl user stop program.
        self.root.mainloop()

gui_Object = Numa_GUI("root")
gui_Object.numa_gui()