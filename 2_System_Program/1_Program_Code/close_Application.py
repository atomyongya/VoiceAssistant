""" Close Application Sub System """ 

# Importing in built Library
import os
import time
import pyautogui

# Importing necessary class and function/method
import file_Path
import mostly_Used_Function
import close_One_Application

class Close_Application():
    """
    Close_Application class is a subsystem to close application of Linux system.
    """
    
    def __init__(self, application_Name):
        """
        Constructor function/method.
        
        :param application_Name (str) : Name of application to close.
        """
        
        self.application_Name = application_Name
        
    def close_Only_1_Application(self):
        """
        Closing the application in position given by the user.
        """
            
        # Move to spefic application.
        pyautogui.keyDown("alt")
        time.sleep(1)
        for i in range(self.application_Position + 1):
            pyautogui.press("tab")
        
        pyautogui.keyUp("alt")

        # Select application.
        pyautogui.keyDown("\n")
        pyautogui.keyUp("\n")
        
        # To close the application.
        pyautogui.keyDown("alt")
        pyautogui.press("F4")
        pyautogui.keyDown("alt")
        
    def close_Application(self):
        """
        Method to close application of Linux system.
        """
        
        try:
            """
            To close;
            """
            
            # chrome
            if self.application_Name.strip() == "chrome" or self.application_Name.strip() == "google":
                os.system("pkill chrome")
            
            # folder/files
            elif self.application_Name.strip() == "folder" or self.application_Name.strip() == "file":
                os.close(files)
                
            elif self.application_Name.strip() == "code":
                os.system("pkill code")
            
            # close with option where you don't know name of application.
            elif self.application_Name.strip() == "option":
                mostly_Used_Function.display_Multiple_Application()
                
            # When application name not found give warning output.
            else:
                mostly_Used_Function.produce_Voice(self.application_Name + " is does not exists.")
            
        except Exception as error:
            mostly_Used_Function.produce_Voice(self.application_Name + " is does not exists.")
                
            
    