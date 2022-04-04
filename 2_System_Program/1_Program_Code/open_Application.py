# Importing Library
import os 
import sys
import subprocess
import webbrowser

# Importing file_Path python file which contain all the path and directory to run the system.
import file_Path

class Open_Application():
    
    """
    Open_Application class is the subsystem to open application of Linux system.
    """
    
    def __init__(self, application_Name):
        """
        Constructore function.
        
        :param application_Name : Name of the application.
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
            if self.application_Name.strip() == "chrome":
                webbrowser.get(file_Path.chrome_Path).open("https://google.com")
                
            # Folder
            elif self.application_Name.strip() == "folder" or self.application_Name.strip() == "file":
                # sudo chmod 775 Desktop -> If any problem occurs do this
                open_Folder = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([open_Folder, file_Path.folder_path])
                
            # Youtube
            elif self.application_Name.strip() == "youtube":
                webbrowser.get(file_Path.chrome_Path).open("https://youtube.com")
                
            # When application name not found
            else:
                print("No such file exits.")
        
        except Exception as error:
            print("Error")
