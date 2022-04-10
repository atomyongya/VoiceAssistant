""" Frontend of Numa """

# Importing Inbuilt Module/Library.
from tkinter import *
from PIL import ImageTk, Image
# from threading import Thread, Lock, current_thread
from multiprocessing import Process
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
        # self.select_Language = StringVar(value="Nepali")
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
     
    def drop_Down_Menu(self, main_Body):
        """
        drop_Down_menu, contain the list of Language.

        :param main_Body : Frame where OptionMenu widgets will be put.
        
        :var language_Option (list) : List which contain language option.
        :var selected_language : Function that helps to manage the value of widget.
        :var drop_down_menu : OptionMenu widget from which drop down menu will be created.
        """
        
        def user_Input_Voice():
            """
            
            """
            
            user_Input_Label = Label(main_Body, text="Output", width=20, height=2)
            user_Input_Label.grid(row=2)

        
        def language_After_Selection(select_language):
            """output_Label = Label(main_Body, text=selected)
                output_Labele.grid()
            
            """
            
            try:
                selected_Language = select_Language.get()
                
                if selected_Language == "Nepali" or selected_Language == None:
                    """cl
                    selected_Language equal to Nepali Language (Call object of nepali_Object)
                    
                    """
                    
                    time.sleep(0.1)
                    print("Nepali Langague")
                    backend_Object_Nepali = main.nepali_Object
                    # thread_Backend_Nepali = Thread(target=backend_Object_Nepali.main()).start()
                    # thread_Backend_Nepali.join()
                    process_Backend_Nepali = Process(target=backend_Object_Nepali.main)
                    process_Backend_Nepali.start()
                    process_Backend_Nepali.join()
                    
                elif selected_Language == "English":
                    """
                    selected langage equal to English Language (Call object of english_Object)
                    
                    """
                    time.sleep(0.1)
                    print("English Langague")
                    backend_Object_English = main.english_Object
                    # thread_Backend_English = Thread(target=backend_Object_English.main()).start()
                    # thread_Backend_English.join()
                    process_Backend_English = Process(target=backend_Object_English.main)
                    process_Backend_English.start()
                    process_Backend_English.join()
                    
                else:
                    print("No langauge Selected.")
                    
                # return self.selected_Language
                    
            except Exception as error:
                print("Error in class frontend and Function language_After_Selection.", error)
        
        def run_Language_Selection(select_language):
            time.sleep(0.1)
            # run_Language = Thread(target=language_After_Selection, args=(select_Language,) ).start()
            process_Run_Language = Process(target=language_After_Selection, args=[select_Language])
            process_Run_Language.start()
            
        # Variable 
        language_Option = ["Nepali", "English"]
        
        select_Language = StringVar()
        select_Language.set("Nepali")
            
        # Creating DropMenu widgets.
        drop_down_menu = OptionMenu(main_Body, select_Language, *language_Option, command=run_Language_Selection)
        drop_down_menu.grid(row=0, column=0)
        drop_down_menu.config(width=10)
        
        print(select_Language.get())
        
        
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
        main_Body.grid(padx=3, pady=10, sticky="ewns", rowspan=5, columnspan=5)
 
        
        # calling drop_Down_Menu function.
        self.drop_Down_Menu(main_Body)
        
        # Run the loop to display unitl user stop program.
        self.master.mainloop()

"""
Creating an object of clas Numa_GUI.

:var gui_Object : Object of class Numa_GUI. 
"""

gui_Object = Numa_GUI(root)


