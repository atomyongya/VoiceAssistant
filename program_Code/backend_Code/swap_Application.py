""" Swap Application Class """

# importing inbuilt module
import os
import time
import pyautogui

# importing other class and function/method.
from backend_Code import mostly_Used_Function

class Swap_Application():
    """
    Swap_Application Class, to swap between application.
    """
    
    def __init__(self, swap_Command, application_Position):
        """
        Constructore function.
        
        :param swap_Command (str) : Contian only "swap" command.
        :param application (int) : Contain the position of the application.
        """
        
        self.swap_Command = swap_Command
        self.application_Position = application_Position
        
    def swap_Application(self):
        """
        Swaping the application with the position given by the user.
        """
        
        # only swap
        if self.swap_Command.strip() == "swap":
            pyautogui.keyDown("alt")
            time.sleep(1)
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
              
        # swap with option            
        elif self.swap_Command.strip() == "swap option":
            
            # Opeaning activities to display application opened.
            pyautogui.keyDown("win")
            pyautogui.keyUp("win")
            time.sleep(1)
            
            # Looping/moving to the given position of the application given by user. 
            for i in range(self.application_Position + 1):
                pyautogui.press("tab")
            

            # Select application.
            pyautogui.keyDown("\n")
            pyautogui.keyUp("\n")
            
            
# swap_Object = Swap_Application("swap option", 3)
# swap_Object.swap_Application()