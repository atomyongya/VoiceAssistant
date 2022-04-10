#!/usr/bin/python3

# Importing Inbuilt Models.
import time
import os
import json
import pygame
import librosa
import numpy as np
import sounddevice as sd
import tensorflow as tf
import speech_recognition as sr
from scipy.io.wavfile import write 
from tensorflow.keras.models import load_model
# from threading import Thread, Lock, current_thread
from multiprocessing import Process, Lock
from queue import Queue


# Importing other file.
import file_Path, mostly_Used_Function 


# Importing class.
import open_Application
from front_End_Code import frontend

class Numa_VoiceAssistant():
    """
    Numa_VoiceAssistant class.
    """
    
    def __init__(self, model_Path, list_Of_Word):
        """
        __init__ is a Constructor method.
        
        :param model_Path (String) : Path of Nepali or English Language Keyword detection model. 
        :param list_Of_Word (list) : List to store the multiple user predicted word to form a commond.
        """
        
        self.model = model_Path
        self.list_Of_Word = list_Of_Word
    
    ######################
    def crossponding_Word(self):
        """
        crossponding_Word method : To map with the user voice command with the corresponding text, that we use to train our model.
        
        
        """
        
        json_Path = "/home/atomyongya/Documents/Herald/Final Year Project/VoiceAssistant(Numa)/VoiceAssistant/_system_Model/2_English_KM/2_English_Json_Output_File/English_Data_JSON.json"
        with open(json_Path, "r") as json_Data:
            data = json.load(json_Data)
        
        return data 
        
    ######################
    def prediction(self, queue_Thread_Prediction, lock_Thread_Prediction):        
        """
        Prediction method to predict the word from the user in real time.

        :param fps: frame per second.
        :param duaration : Record time duration.
        :param filename : audio path.
        :param mapping_Data : Loding the data to compare with our real time audio.
        """
        
        with lock_Thread_Prediction:
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
            # print("Current thread: {}".format(current_thread().name))
            
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
                
                queue_Thread_Prediction.put(predicted_keyword)
                # queue_Thread_Prediction.task_done()
                
            except Exception as error:
                print("Error in prediction class.", error)
        

    ######################
    def main(self):
        """
        main method to execute program.
        
        :var wake_Word (String) : Wake word of "Numa" Voice Assistant.
        """
        
        try:
            run_Once = 0
            # print("Current thread: {}".format(current_thread().name))
                    
            print("Say Wake Word: ")
            wake_Word = "numa"
            
            while True:
                """
                Using while lopp because system run continuously in background to detect wake word "numa".
                
                :var predicted_keyword (String): Output/Prediction of our model.
                """
                queue_Thread_Prediction = Queue()
                lock_Thread_Prediction = Lock()
                
                # thread_Prediction = Thread(target=self.prediction, args=(queue_Thread_Prediction,lock_Thread_Prediction))
                # thread_Prediction.start()
                # thread_Prediction.join()
                process_Prediction = Process(target=self.prediction, args=[queue_Thread_Prediction, lock_Thread_Prediction])
                process_Prediction.start()
                process_Prediction.join()
                
                # thread_Prediction.deamon = True
                # print("{}".format(thread_Prediction.is_alive()))
                
                predicted_keyword = queue_Thread_Prediction.get()
                # predicted_keyword = "No"
                print("Wake Word: ", predicted_keyword)
                predicted_keyword = "numa"
                
                if predicted_keyword == wake_Word:
                    
                    print("Inside....")

                    mostly_Used_Function.play_Audio(file_Path.wake_Word_Sound_Effect)
                    
                    if predicted_keyword.count(wake_Word) > 0:
                        """
                        Condition to check the count of wake word is greater then zero to take next command of user.
                        
                        :var count (int) : To keep track of below while loop.
                        """
                        count = 1
                        
                        try: 
                            while True:
                                print("Inside of Inside...")
                                
                                """
                                Loop to get the user main command that will execute some program.
                                
                                :var user_Command (str) : predicted_keyword.
                                """  
                                
                                # Stoting the value value of predicted_keyword in user_Command variable.
                                # thread_Prediction1 = Thread(target=self.prediction, args=(queue_Thread_Prediction, lock_Thread_Prediction))
                                # thread_Prediction1.start()
                                process_Prediction1 = Process(target=self.prediction, args=[queue_Thread_Prediction, lock_Thread_Prediction])
                                
                                predicted_keyword = queue_Thread_Prediction.get()
                                user_Command = predicted_keyword
                                print("Inside: ",user_Command)
                                # thread_Prediction.deamon = True
                                
                                # print("{}".format(thread_Prediction1.is_alive()))

                                # Appending the user predicted_keyword/user_Command in list_Of_Word list.
                                list_Of_Word.append(user_Command)
                                count = count + 1
                                queue_Thread_Prediction.task_done()
                                
                                # user_Command = "open chrome"
                                # Condition to break loop after 4 iteration or 4 second because each record time is 1 second. 
                                if count == 4:
                                    """
                                    Program execuation code.
                                    """
                                    
                                    print(list_Of_Word)
                                    
                                    # To open an application of system.
                                    if "open" in user_Command:
                                        application_Name = user_Command.replace("open", "")
                                        mostly_Used_Function.produce_Voice("Opeaning " + application_Name)
                                        open_Application_Object = open_Application.Open_Application(application_Name)
                                        open_Application_Object.open_Application()
                                    
                                    
                                    # Breaking the loop after the execuation of the program.
                                    break
                                    # queue_Thread_Prediction.task_done()
                                    
                                
                        except Exception as error:
                            print("Error from class main and function main: First exception eror", error)
                        
                        # gui_Object = frontend.gui_Object 
                        # gui_Object.minimize_Application() 
                        # thread_Prediction.daemon = True
                        # thread_Prediction.join()
                        
                        list_Of_Word.clear()
            
                else:
                    continue 
                
        except Exception as error:
            print("Error in class main and Function main: Second exception error", error)
            
"""
Creating object of class "Numa_VoiceAssistant" for english language keyword detection. 

:var english_Object : Object of Numa_VoiceAssistant.
"""

list_Of_Word = []
english_Object = Numa_VoiceAssistant(file_Path.english_Model_Path, list_Of_Word)

nepali_Object = Numa_VoiceAssistant(file_Path.english_Model_Path, list_Of_Word)

# Use if and else if nepali langague if you want to declear nepali object.


