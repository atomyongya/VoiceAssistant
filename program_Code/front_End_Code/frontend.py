""" Frontend of Numa """

# Importing Inbuilt Module/Library.
from tkinter import *
from PIL import ImageTk, Image
from threading import Thread, Lock, current_thread
from queue import Queue

import time
import pyautogui

# Importing other class and function/method
import file_Path
import main

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
background_Color3 = "#655edd"

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

is_Default = True

# Declearing the with and height of the application and position of application when open.
root.geometry(f"{app_Width}x{app_Height}+{int(x_axis)}+{int(y_axis)}")

class Numa_GUI(object):
    """
    Graphical User Interface of "Numa" Voice Assistant.
    """
    
    def __init__(self, master):
        """
        Constructor Function.
        
        :param master : Main Widgets/Window of system which hold other sub widgets.
        """
        
        self.master = master    
        # self.selected_Language = None
                        
    def move_Application(self, event):
        """
        move_Application method, provide power to move application around the computer scrren. 
        
        :param event : Event during application move in screen.
        """
           
        self.master.geometry(f"+{event.x_root}+{event.y_root}")    
    
    def minimize_Application(self):
        """
        
        """
        self.master.withdraw()
        
    def display_After_Minimize(self):
        """
        
        """

        self.master.deiconify()
        
    def fake_Title_Bar(self):
        """
        fake_Title_Bar method, to create beautiful title bar.
        
        :var title_Bar : Frame widgets act as the title bar for our system GUI.
        :var icon_Path (str) : Path of image icon.
        :var load_Icon : Opeaning/Loading image from icon_Path folder.
        :var icon_Label : Label widget to display image.
        :var title_Name : Label widgets that contain the title name of our system.
        :var close_Button : Button widgets to close the application.
        """
        
        # Creating a frame for title bar.
        title_Bar = Frame(self.master, bg=background_Color2, relief="raised")
        title_Bar.grid(row=0, column=0, sticky="ew")
        title_Bar.grid_rowconfigure(0, weight=1)
        title_Bar.grid_columnconfigure(0, weight=1)
        
        # Binding title_Bar frame which allow our application to move when user drag.
        title_Bar.bind("<B1-Motion>", self.move_Application)
        
         # Icon of title bar.
        load_Icon = ImageTk.PhotoImage(Image.open(file_Path.icon_Path))
        icon_Label = Label(title_Bar, image=load_Icon, width=20, height=20)
        icon_Label.grid(row=0, column=0, padx=3, pady=3, sticky=W)
        icon_Label.bind("<B1-Motion>", self.move_Application)
        
        # Adding the lable inside title_Bar frame.
        title_Name = Label(title_Bar, text="Numa", bg=background_Color2, foreground="white", font=20)
        title_Name.grid(row=0, column=0, padx=30, pady=3, sticky=W)
        title_Name.bind("<B1-Motion>", self.move_Application)
        
        # Adding minimize button.
        minimize_Button = Button(title_Bar, text="-", font=20, bg=background_Color2, fg="white", command=self.minimize_Application, relief=SUNKEN, borderwidth=0, highlightthickness=0)
        minimize_Button.grid(row=0, sticky="es")
        
        # Creating close button for title bar.
        close_Button = Button(title_Bar, text="X", font=20, bg=background_Color2, fg="white", command=self.minimize_Application, relief=SUNKEN, borderwidth=0, highlightthickness=0)
        close_Button.grid(row=0, column=1, sticky="es")
     
    def change_Language(self, label_Language_Info):
        
        global is_Default
        
        if is_Default:
            select_Language = "English"
            label_Language_Info.config(text=select_Language)
            print(select_Language)
            is_Default = False
            
        else:
            select_Language = "Nepali"
            label_Language_Info.config(text=select_Language)
            print(select_Language)
            is_Default = True
            
        return select_Language
    
    
    # def get_Output_Word(self, predicted_Word):
    #     label_Language_Info.config()
    #     return word
        
    def drop_Down_Menu(self, main_Body):
        """
        drop_Down_menu, contain the list of Language.

        :param main_Body : Frame where OptionMenu widgets will be put.
        
        :var language_Option (list) : List which contain language option.
        :var selected_language : Function that helps to manage the value of widget.
        :var drop_down_menu : OptionMenu widget from which drop down menu will be created.
        """
        
        
        entry_Input_Command = Entry(main_Body, fg="black")
        entry_Input_Command.grid(padx=1, pady=20)
        
        options = ["Nepali", "English"]
        language_Option = StringVar()
        language_Option.set("Nepali")
        
        drop_down_menu = OptionMenu(main_Body, language_Option, *options, command=lambda x=None: self.change_Language(label_Language_Info))
        drop_down_menu.grid(row=0, column=0, padx=5, pady= 2, sticky="w")
        drop_down_menu.config(background=background_Color3, foreground="white", borderwidth=0, highlightbackground=background_Color3)
        
        # Animation or image
        
        backend_Object = main.english_Object
        
        label_Language_Info = Label(main_Body, text="", width=40, bg="white", fg="black", borderwidth=1, highlightthickness=1, highlightcolor="white")
        label_Language_Info.grid(padx=2, pady=40)
        
       
        
        default_language = "Nepali"
        if is_Default:
            backend_Nepali_Object = main.english_Object
            thread_Backend_Nepali = Thread(target=backend_Nepali_Object.main, args=(label_Language_Info,))
            thread_Backend_Nepali.start()
            print("Nepali Stopped")
            
        elif is_Default == False:
            print("English")
            
            backend_English_Object = main.english_Object
            thread_Backend_English = Thread(target=backend_English_Object.main, args=(label_Language_Info,))
            thread_Backend_English.daemon = True
            thread_Backend_English.start()
            print("English Stopped")
            
            
        else:
            print("Default Nepali")
            backend_Nepali_Object = main.english_Object
            thread_Backend_Nepali = Thread(target=backend_Nepali_Object.main, args=(label_Language_Info))
            thread_Backend_Nepali.daemon = True
            thread_Backend_Nepali.start()
            print("Nepali Stopped")
            
        
    def numa_gui(self):
        """
        numa_gui method that hold sub widgets.
        
        :var main_Body : Frame that hold the main sub widgets of application. 
        """
        
        self.master.overrideredirect(True) # Removing the default title bar.
        self.master.grid_columnconfigure(0, weight=1)
        
        self.fake_Title_Bar()
        
        # Creating main body of an application.
        main_Body = Frame(self.master, bg="red", width=480, height=550, relief="raised", borderwidth=0)
        main_Body.grid(padx=3, pady=3, sticky="nsew")
        main_Body.grid_columnconfigure(0, weight=1)
        main_Body.grid_rowconfigure(0, weight=1)
        
        
        # calling drop_Down_Menu function.
        self.drop_Down_Menu(main_Body)
        
        # Run the loop to display unitl user stop program.
        self.master.mainloop()

"""
Creating an object of clas Numa_GUI.

:var gui_Object : Object of class Numa_GUI. 
"""

gui_Object = Numa_GUI(root)


