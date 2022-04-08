"""Open Application Sub System """

# Importing inbuilt Library.
import os 
import sys
import subprocess
import webbrowser

# Importing necessary class and function/method.
from backend_Code import file_Path, mostly_Used_Function

class Open_Application():
    """
    Open_Application class is the subsystem to open application of Linux system.
    """
    
    def __init__(self, application_Name):
        """
        Constructor function.
        
        :param application_Name (str): Name of the application open.
        """
        
        self.application_Name = application_Name
        
    def open_Application(self):
        """
        Method to open application of Linux system.
        """
        
        try:
            """
            To open :
            """
            
            # Chrome 
            if self.application_Name.strip() == "chrome" or self.application_Name.strip() == "google":
                webbrowser.get(file_Path.chrome_Path).open("https://google.com")
                
            # Folder
            elif self.application_Name.strip() == "folder" or self.application_Name.strip() == "file":
                # sudo chmod 775 Desktop -> If any problem occurs do this
                open_Folder = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([open_Folder, file_Path.folder_path])
                
            # Youtube
            elif self.application_Name.strip() == "youtube":
                webbrowser.get(file_Path.chrome_Path).open("https://youtube.com")
                
            # When application name not found give warning output.
            else:
                mostly_Used_Function.produce_Voice(self.application_Name + " is does not exists.")
        
        except Exception as error:
            mostly_Used_Function.produce_Voice(self.application_Name + " is does not exists. Also, contain error.")
