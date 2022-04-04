#!/usr/bin/python3

# Importing Inbuilt Models.
import os
import json
import librosa
import numpy as np
import sounddevice as sd
import tensorflow as tf
import speech_recognition as sr
import playsound
import IPython.display as ipd
import pygame

from scipy.io.wavfile import write 
from tensorflow.keras.models import load_model

# Importing other class.
# import award_Penelty
import file_Path
import mostly_Used_Function 

"""
:var nepali_Model_Path (String) : Path of Nepali Langague Keyword detection model. 
:var english_Model_Path (String) : Path of English Language keyword detection model.
"""

# Model Path
nepali_Model_Path = ""
english_Model_Path = load_model("../../1_System_Model/2_English_KM/3_English_Model_File/english_Model.h5")

class Numa_VoiceAssistant():
    """
    Numa_VoiceAssistant class.
    """
    
    def __init__(self, model_Path):
        """
        __init__ is a Constructor method.
        
        :param model_Path (String) : Path of Nepali or English Language Keyword detection model. 
        """
        
        self.model = model_Path
    
    ######################
    def crossponding_Word(self):
        """
        crossponding_Word method : To map with the user voice command with the corresponding text, that we use to train our model.
        
        
        """
        
        json_Path = "../../1_System_Model/2_English_KM/2_English_Json_Output_File/English_Data_JSON.json"
        with open(json_Path, "r") as json_Data:
            data = json.load(json_Data)
        
        return data 
        
    ######################
    def prediction(self):        
        """
        Prediction method to predict the word from the user in real time.

        :param fps: frame per second.
        :param duaration : Record time duration.
        :param filename : audio path.
        :param mapping_Data : Loding the data to compare with our real time audio.
        """

        data = self.crossponding_Word()
        mapping_Data = data["mappings"]
        
        fps = 44100
        duration = 1
        filename = "user_Audio/prediction.wav"

        """
        :var myrecording :  Audio to predict real time user voice.
        :var prediction :  Prediction of real time audio voice.
        :var predicted_index : Hold the max prediction value of our model.
        :var predicted_keyword : Text word with which our voice will get compared. 
        """
        
        try:
            # Real time audio recording.  
            myrecording = sd.rec(int(duration * fps), samplerate=fps, channels=2)
            sd.wait()
            write(filename, fps, myrecording)
            
            # Loading the recorded file using librosa.
            signal, sample_rate = librosa.load(filename)

            # Extracting the MFCC feature of an audio
            mfcc = librosa.feature.mfcc(signal, sample_rate, n_mfcc=13, hop_length=512, n_fft=2048)

            # Making prediction and comparing our audio mfcc with the mfcc of train audio data
            prediction = self.model.predict(tf.expand_dims(mfcc.T, axis=0)) 
            
            

            # Finding max prediction value and mapping with the index of mapping_Data from json. 
            predicted_index = np.argmax(prediction)

            predicted_keyword = mapping_Data[predicted_index]
            # print(predicted_keyword)
            
        except Exception as error:
            print(error)
            
        return predicted_keyword
    
    ######################
    def main(self):
        """
        main method to execute program.
        
        :var wake_Word (String) : Wake word of "Numa" Voice Assistant.
        """
        
        wake_Word = "numa"
        
        print("Listening")
        while True:
            """
            Using while lopp because system run continuously in background to detect wake word "numa".
            
            :var predicted_keyword (String): Output/Prediction of our model.
            """
            
            predicted_keyword = self.prediction()
            print(predicted_keyword)
            
            mostly_Used_Function.award()
            print("end")
            
            # if predicted_keyword.count(wake_Word) > 0:
            #     """
            #     Condition to check the count of wake word is greater then zero to take next command of user.
                
                
            #     """
                
            #     try:       
            #         predicted_keyword = self.prediction()
            #         user_Command = predicted_keyword
            #         print(user_Command)
                    
            #         self.response_Voice("Hello Atom, How can I help you?")
                    
            #     except Exception as error:
            #         print(error)
                    
                    
                
    

"""
Creating object of class "Numa_VoiceAssistant" for english language keyword detection. 

:var english_Object : Object of Numa_VoiceAssistant.
"""

english_Object = Numa_VoiceAssistant(english_Model_Path)
english_Object.main()



# Use if and else if nepali langague if you want to declear nepali object.

