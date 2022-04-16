""" Frontend of Numa """

# Importing Inbuilt Module/Library.
import time
import pyautogui
import random

from tkinter import *
from PIL import ImageTk, Image
from threading import Thread, Lock, current_thread
from queue import Queue

# Importing other class and function/method
import main
import file_Path
from front_End_Code import audio_Animation

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

# Color used as a backend for GUI of application.
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
        self.x_Start = 5
        self.y_Start = 220
        self.x_End = 40
        self.y_End = 230
        self.color_List = ["orange", "red"]
                        
    def move_Application(self, event):
        """
        move_Application method, provide power to move application around the computer scrren. 
        
        :param event : Event during application move in screen.
        """
           
        self.master.geometry(f"+{event.x_root}+{event.y_root}")    
    
    def minimize_Application(self):
        """
        minimize_Application method, to minimize the application.
        """
        
        self.master.withdraw()
        
    def display_After_Minimize_Close(self):
        """
        display_After_Minimize_Close method, to reopen application.
        """

        self.master.deiconify()
        
    def fake_Title_Bar(self):
        """
        fake_Title_Bar method, to create beautiful title bar.
        
        :var title_Bar : Frame widgets act as the title bar for our system GUI.
        :var load_Icon : Opeaning/Loading image from icon_Path folder.
        :var icon_Label : Label widget to display image.
        :var title_Name : Label widgets that contain the title name of our system.
        :var minimize_Button : Button widget to minimize the application.
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
        close_Button = Button(title_Bar, text="X", font=20, bg=background_Color2, fg="white", command=self.master.quit, relief=SUNKEN, borderwidth=0, highlightthickness=0)
        close_Button.grid(row=0, column=1, sticky="es")
     
    def change_Language(self):
        """
        change_Language method is called when there is change in language from drop_Down_Menu method.
        
        :var is_Default (Boolean) : It is helps us to switch between Nepali and English langauge.
        :var select_Language (str) : Selected Language.  
        """
        
        global is_Default
        
        # For Default value and Nepali Language
        if is_Default:
            select_Language = "Nepali"
            print(select_Language)
            is_Default = False
            
        # For English Language
        else:
            select_Language = "English"
            print(select_Language)
            is_Default = True
            
        return select_Language
    
 
                
    def default_Animation(self, canvas_Audio_Animation):
        """
        
        """
        
        for i in range(7):
            if i == 0:
                audio_Animation_Object = audio_Animation.Audio_Animation(canvas_Audio_Animation, self.x_Start, self.y_Start, self.x_End, self.y_End, self.color_List)
                audio_Animation_Object.audio_Input_Animation()
        
            else:
                audio_Animation_Object = audio_Animation.Audio_Animation(canvas_Audio_Animation, self.x_Start, self.y_Start, self.x_End, self.y_End, self.color_List)
                audio_Animation_Object.audio_Input_Animation()
                
            self.x_Start = self.x_Start + 40
            self.x_End = self.x_End + 40
            
    def animation_If_User_Speak(self, canvas_Audio_Animation):
        """
        Random rectangle object apper when user gives command.
        """
        
        x_Start = 5
        y_Start = 200
        x_End = 40
        y_End = 210
        
        list_Rows = [4, 5, 6, 7, 8, 9, 10]
        output_Row = random.choice(list_Rows)
        print(output_Row)
        list_Columns = [4, 5, 6, 7]
        output_Column = random.choice(list_Columns)
        print(output_Column)
        
        for i in range(output_Row):
            
            for j in range(output_Column):
                animation_On_Speak = audio_Animation.Audio_Animation(canvas_Audio_Animation, x_Start, y_Start, x_End, y_End, self.color_List)
                animation_On_Speak.audio_Input_Animation()
                x_Start = x_Start + 40  
                x_End = x_End + 40
            time.sleep(0.001)
            x_Start = 5
            y_Start = y_Start - 20
            x_End = 40
            y_End = y_End - 20
            
    def drop_Down_Menu(self, main_Body):
        """
        drop_Down_menu, contain the list of Language.

        :param main_Body : Frame where OptionMenu widgets will be put.
        
        :var options (list) : List which contain language option.
        :var language_Option : Selected language in dropdown menu.
        :var drop_down_menu : OptionMenu widget from which drop down menu will be created.
        """
<<<<<<< HEAD
        
=======

>>>>>>> demo
        # Options for language selection.
        options = ["Nepali", "English"]
        language_Option = StringVar()
        language_Option.set("Nepali")
        
        # Creating Drop Down Meu.
        drop_down_menu = OptionMenu(main_Body, language_Option, *options, command=lambda x=None: self.change_Language())
        drop_down_menu.grid(row=0, column=0, padx=5, pady= 2, sticky="w")
        drop_down_menu.config(background=background_Color3, foreground="white", borderwidth=0, highlightbackground=background_Color3)
            
        # Creating label widget where the user command will be displayed.
        label_Language_Info = Label(main_Body, text="", width=40, bg=background_Color1, fg="white")
        label_Language_Info.grid(padx=2, pady=60)
        
        # Creating Object of Audio_Animation class and calling method audio_Input_Animation.
        
<<<<<<< HEAD
        canvas_Audio_Animation = Canvas(main_Body, width=300, height=240, background=background_Color1, borderwidth=0, highlightthickness=0)
        canvas_Audio_Animation.grid(pady=0) 
        self.default_Animation(canvas_Audio_Animation)
=======
        # Creating label widget where the user command will be displayed.
        label_Language_Info = Label(main_Body, text="", width=40, bg=background_Color1, fg="white", font=(20), borderwidth=1, highlightthickness=0, highlightcolor=background_Color1)
        label_Language_Info.grid(padx=2, pady=80, ipady=5)
>>>>>>> demo
        
        # Condition to run language with the selected langauge in drop_down_menu widget.
        default_language = "Nepali"
        if is_Default:
            backend_Nepali_Object = main.english_Object
            thread_Backend_Nepali = Thread(target=backend_Nepali_Object.main, args=(label_Language_Info, canvas_Audio_Animation))
            thread_Backend_Nepali.start()
            print("Nepali Stopped")
            
        elif is_Default == False:
            print("English")
            backend_English_Object = main.english_Object
            thread_Backend_English = Thread(target=backend_English_Object.main, args=(label_Language_Info, canvas_Audio_Animation))
            # thread_Backend_English.daemon = True
            thread_Backend_English.start()
            print("English Stopped")
            
        else:
            print("Default Nepali")
            backend_Nepali_Object = main.english_Object
            thread_Backend_Nepali = Thread(target=backend_Nepali_Object.main, args=(label_Language_Info, canvas_Audio_Animation))
            # thread_Backend_Nepali.daemon = True
            thread_Backend_Nepali.start()
            print("Nepali Stopped")
            
    
            
    def numa_gui(self):
        """
        numa_gui method that hold sub widgets.
        
        :var main_Body : Frame that hold the main sub widgets of application. 
        """
        
        # Removing the default title bar.
        self.master.overrideredirect(True) 
        
        # Configuring column gird to take space of 1.
        self.master.grid_columnconfigure(0, weight=1)
        
        # Calling method fake_Title_Bar.
        self.fake_Title_Bar()
        
        # Creating main body of an application.
        main_Body = Frame(self.master, bg=background_Color1, width=480, height=550, relief="raised", borderwidth=0)
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


