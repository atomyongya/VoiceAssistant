"""
This file hold mostly used class and function of the system.
"""

# Importing Important Library
import os
import pyttsx3
import pygame

# Importing other function and library 
import file_Path

"""
(1) produce_Voice Function, to produce voice.

:var ai_Engine : Insitilizing the pyttsx3 module.
"""

ai_Engine = pyttsx3.init()
ai_Engine.setProperty("rate", 155) # Controlling the Speed of ai_Voice

def produce_Voice(replies_Sentence):
    ai_Engine.say(replies_Sentence)
    ai_Engine.runAndWait()

###################################   
"""
(2) play_Audio Function, to play audio.
"""

pygame.init()

def play_Audio(audio_Path):
    pygame.mixer.Sound(audio_Path).play()
    
###################################
"""
(3) award Function, Which will produce sound and play audio currently recorded.

:var award_Penelty : Input to give award or not.
"""
def award():
    award_Penelty = input("Enter 'enter' keyword for penelty else award: ")
        
    if award_Penelty == "a" or award_Penelty == "A":
        produce_Voice("Hello Atom, How can I help you?")
        play_Audio(file_Path.save_Audio_Path)
        
    else:
        print("Bad word. Give Penelty.")
        
###################################
"""
(4) make_Directory function, to create a folder.

:var number_Folder (int) : Number of folder user want to create.
:var folder_Name : Name of folder user want to create.
"""

def make_Directory():
    number_Folder = int(input("Enter the number of folder to create: "))
    
    for i in range(number_Folder):
        folder_Name = input(f"Enter the name of the {i} folder: ")
        os.mkdir(file_Path.save_Awarded_Audio + "/" + folder_Name)

###################################
"""
(3) Save the awarded audio file.
"""

def save_Awarded_Audio():
    """
    :var list_Directory (list) : List of the folder name.
    :var user_Selection (String) : Folder name where the file will be saved.
    """
    
    # List of directory
    list_Directory = [saved_File for saved_File in os.listdir(file_Path.save_Awarded_Audio)]
    print(list_Directory)
    
    user_Selection = input("Enter the name of the folder where you want to save file: ")
    
    # Looping through list_Directory List to match folder name.
    for i in range(len(list_Directory)):
        
        # Condition to match with the name of the folder present inside list_Directory list.
        if user_Selection == list_Directory[i]:
            
            while True:
                """
                Moving, Saving and Renaming the audio file unitl user do not stop the loop.
                
                :var list_File (list) :  File inside the user selected folder.
                :var length_Selected_Folder (int) : Length of the list_File variable.
                :var renaming_File (str) : Renaming the name of the prediction.wav file.
                :var continue_File (str) : To continue or break while loop.
                """
                
                try:
                    # move the awarded audio in there respective folder.
                    if os.path.exists(user_Audio/prediction.wav):
                        os.system("mv user_Audio/prediction.wav " + "user_Audio/awarded_Audio/" + user_Selection + "/")
                    
                    else:
                        print("No File to move.")
                    
                    list_File = [file_name for file_name in os.listdir(file_Path.save_Awarded_Audio + user_Selection + "/")]
                    length_Selected_Folder = len(list_File)

                    try:
                        if length_Selected_Folder == 1:
                            length_Selected_Folder = 1
                            renaming_File = os.rename(f"user_Audio/awarded_Audio/{user_Selection}/prediction.wav", f"user_Audio/awarded_Audio/{user_Selection}/{length_Selected_Folder}.wav")
                            
                        else:
                            renaming_File = os.rename(f"user_Audio/awarded_Audio/{user_Selection}/prediction.wav", f"user_Audio/awarded_Audio/{user_Selection}/{length_Selected_Folder}.wav")
                    
                    except Exception as error:
                        print("No file to rename.")
                    
                    print(f"Old Name : prediction.wav \nNew Name : {renaming_File}")
                    
                except Exception as error:
                    print("File not found.")
                
                # Condition to continue or break while loop.
                continue_File = input("Continue: ")
                if continue_File == "n":
                        break
                    
                else:
                    continue
        
        else:
            continue
        
    
###################################
"""
Function call if necessary.
"""

# make_Directory()

# save_Awarded_Audio()