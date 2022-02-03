import os
import subprocess
import signal
import Open_App

def close_Application(application_Name):
    print(application_Name)
    chrome_path = "/usr/bin/google-chrome"
    
    # To close browser
    if application_Name.strip() == "chrome":
        pass
        
    # To close folder
    elif application_Name.strip() == "folder":
        os.kill(pid, sig)
    
    # To Close all application
    elif application_Name.strip() == "all application":
        print("All applications closed")
    
    # Alert message when application is not found open 
    else:
        print("Alert Message") # Use of Vibration 
        exit()
