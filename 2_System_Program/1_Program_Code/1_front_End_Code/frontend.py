""" Frontend of Numa """

# Importing Inbuilt Module/Library.
from tkinter import *
from PIL import ImageTk, Image

# Importing other class and function/method


"""
Creating the widgets/window of our system.

:var root : Main widgets of application which contain all other widgets.
:var app_Width (int) : Width of application.
:var app_Height (int) : Height of application.
:var screen_Width (float) : Width of computer screen.
:var screen_Height (float) : Height of computer screen.
:var x_axis (float) : Center of computer screen horizantlly.
:var y_axis (float) : Center of computer screen vertically.
"""

background_Color1 = "#1f273e"
background_Color2 = "#636af9"

# Declearing Root Widgets.
root = Tk()
root.title("Numa")
root.config(bg=background_Color1, highlightbackground=background_Color2, borderwidth=0, highlightthickness=2, relief=RAISED)



# Insitilizing the width and height of application.
app_Width = 500
app_Height = 600

# Getting width and height info of computer screen.
screen_Width = root.winfo_screenwidth()
screen_Height = root.winfo_screenheight()

# To find the center of the computer screen.
x_axis = (screen_Width/2) - (app_Width/2)
y_axis = (screen_Height/2) - (app_Height/2)

# Declearing the with and height of the application and position of application when open.
root.geometry(f"{app_Width}x{app_Height}+{int(x_axis)}+{int(y_axis)}")

class Numa_GUI():
    """
    Graphical User Interface of "Numa" Voice Assistant.
    """
    
    def __init__(self, master):
        """
        Constructor Function.
        
        :param master : Main Widgets/Window of system which hold other sub widgets.
        """
        
        self.master = master    
                        
    def move_Application(self, event):
        """
        move_Application method, provide power to move application around the computer scrren. 
        """
           
        self.master.geometry(f"+{event.x_root}+{event.y_root}")
        
    def fake_Title_Bar(self):
        """
        fake_Title_Bar method, to create beautiful title bar.
        
        :var title_Bar : Frame widgets act as the title bar for our system GUI.
        :var title_Name : Label widgets that contain the title name of our system.
        :var close_Button : Button widgets to close the application.
        """
        
        
        
        # Creating a frame for title bar.
        title_Bar = Frame(self.master, width=500, bg=background_Color2, relief="raised")
        title_Bar.grid(row=0, column=0, sticky="ew")
        title_Bar.grid_rowconfigure(0, weight=1)
        title_Bar.grid_columnconfigure(0, weight=1)
        
        # Binding title_Bar frame which allow our application to move when user drag.
        title_Bar.bind("<B1-Motion>", self.move_Application)
        
         # Icon of title bar.
        icon_Path = "icon.png"
        load_Icon = ImageTk.PhotoImage(Image.open(icon_Path))
        icon_Label = Label(title_Bar, image=load_Icon, width=20, height=20)
        icon_Label.grid(row=0, column=0, padx=3, pady=3, sticky=W)
        icon_Label.bind("<B1-Motion>", self.move_Application)
        
        # Adding the lable inside title_Bar frame.
        title_Name = Label(title_Bar, text="Numa", bg=background_Color2, foreground="white", font=20)
        title_Name.grid(row=0, column=0, padx=30, pady=3, sticky=W)
        title_Name.bind("<B1-Motion>", self.move_Application)
        
        # Creating close button for title bar.
        close_Button = Button(title_Bar, text="X", font=20, bg=background_Color2, fg="white", command=self.master.quit, relief=SUNKEN, borderwidth=0, highlightthickness=0)
        close_Button.grid(row=0, sticky="es")
        
       
        
          
        
    def numa_gui(self):
        """
        numa_gui method that hold sub widgets.
        """
        self.master.overrideredirect(True)
        self.master.grid_columnconfigure(0, weight=1)
        self.fake_Title_Bar()
        # Creating main body of an application.
        main_Body = LabelFrame(self.master, bg=background_Color1, width=480, height=550, relief="raised", borderwidth=0)
        main_Body.grid(pady=10)

        
gui_Object = Numa_GUI(root)
gui_Object.numa_gui()

# Run the loop to display unitl user stop program.
root.mainloop()