#!/usr/bin/python3

# Inbuilt Modules
import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import threading

# Importing other function  
import Open_App
import Close_App
import Terminal_Command
import numa
import Swap_Application

# Recognize the user command
listener = sr.Recognizer() 

# AI voice to speak with user
ai_Engine = pyttsx3.init()
ai_Engine.setProperty("rate", 155) # Controlling the Speed of ai_Voice

# numa.numa_gui()
# Response is given to the user each time some process happen
def Response_Voice(text_Command):
    ai_Engine.say(text_Command)
    ai_Engine.runAndWait()

def Receive_Command():
    try:
        final_Command = None
        with sr.Microphone() as user_Command_Source:   # {with} Terminate the exception with out any error
            # Alert message when numa application is ready 
            print("Listening...")
            # Response_Voice("numa")
            
            # Listen to the user voice from microphone using user_Command_Source
            user_Voice_Command = listener.listen(user_Command_Source)
            
            # speech recognition model will translate the user_Voice_Command which is audio into text
            final_Command = listener.recognize_google(user_Voice_Command)
            
            # Converting the text to lower case
            final_Command = final_Command.lower()
                
    except Exception as error:
        print("Exception in Receive_Command", error)
        
    return final_Command
    

# Main Function that get execuated while user give command 
def numa_System_Run():
    user_Command = Receive_Command()
    try:
        # To know numa is on
        if "are you there" in user_Command:
            try:
                replies = user_Command.replace("are you there", "")
                Response_Voice("Yes Atom, How can I help you" + replies)
                print("Yes Atom, How can I help you")
                
            except Exception as error:
                print("Yes Atom, How can I help you")
            
        # To open the application in system
        elif "open" in user_Command:        
            application_Name = user_Command.replace("open", "")
            Response_Voice("Opeaning " + application_Name)
            Open_App.open_Application(application_Name)
            
        # To Close the application in system
        elif "close" in user_Command:
            application_Name = user_Command.replace("close", "")
            Response_Voice("Closing " + application_Name)
            Close_App.close_Application(application_Name)
        
        # Play the music online or offline 
        elif 'play' in user_Command:
            song = user_Command.replace('play', '')
            Response_Voice('playing ' + song)
            print(song)
            pywhatkit.playonyt(song)
            
        # To get the time 
        elif 'time' in user_Command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            Response_Voice("Current time is " + time)
            
        # To get information from wikipedia python library
        elif 'who is' in user_Command:
            search_Object = user_Command.replace("who is", "")
            object_Information = wikipedia.summary(search_Object, 1)
            print(object_Information)
            Response_Voice(object_Information)
            
        # To update upgrade and autoremove the system
        elif "system" in user_Command:
            system_Command = user_Command.replace("system", "")
            Response_Voice(system_Command+"ing")
            Terminal_Command.terminal_Command(system_Command)
            
        # To swap between an application
        elif "swap" in user_Command:
            swaping_Command = user_Command.replace("swap", "")
            Response_Voice("Swaping")
            Swap_Application.swap_Application()
            
        else:
            Response_Voice("Sorry, can you say it again")
    
    except Exception as error:
        Response_Voice("Command not found")
    
        