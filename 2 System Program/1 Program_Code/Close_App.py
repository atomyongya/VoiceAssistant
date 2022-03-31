import os
import sys
import subprocess
import signal
import pyautogui
import time

def close_Application(application_Name):
    print(application_Name)
    chrome_path = "/usr/bin/google-chrome"
    
    # To close chrome
    try:
        if application_Name.strip() == "chrome":
            os.system("pkill chrome")
            
        # To close folder
        elif application_Name.strip() == "folder":
            try:
                os.close(files)
                
            except NameError as name_Error:
                print("Found error", name_Error)
                
            except Exception as error:
                print("There is error other than NameError in Close_App.py File." + error)
            
        
        # Alert message when application is not found open 
        else:
            print("Alert Message") # Use of Vibration 
    
    except NameError as name_Error:
        print("Found error: ", name_Error)
        
    except Exception as error:
        print ("There is error other than NameError in Close_App.py File.")
