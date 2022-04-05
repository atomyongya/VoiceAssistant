"""
Close Only One Application from multiple application.
"""

# Import Inbuilt module.
import time
import pyautogui

# Import necessary class and function/method
import mostly_Used_Function

class Close_Only_1_Application():
    """
    Close Only One Application from multiple application.
    """
    
    def __init__(self, application_Position):
        """
        Constructore Fucntion.
        
        :param application_Position (int) : Position of application in activities of Linux system.
        """
        
        self.application_Position = application_Position
    
    
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

object_1 = Close_Only_1_Application(3)
object_1.close_Only_1_Application()