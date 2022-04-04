"""
This file hold mostly used class and function of the system.
"""

# Importing Important Library
import pyttsx3
import pygame
import playsound as playsound

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

def play_Audio():
    pygame.mixer.Sound(file_Path.save_Audio_Path).play()
    
###################################
"""
(3) award Function, Which will produce sound and play audio currently recorded.

:var award_Penelty : Input to give award or not.
"""
def award():
    award_Penelty = input("Enter 'enter' keyword for penelty else award: ")
        
    if award_Penelty == "a" or award_Penelty == "A":
        produce_Voice("Hello Atom, How can I help you?")
        play_Audio()
        
    else:
        print("Bad word. Give Penelty.")
        self.main()

###################################
"""
(3) Save the awarded audio file.
"""
    
    
###################################