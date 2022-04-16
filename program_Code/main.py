#!/usr/bin/python3

# Importing Inbuilt Models.
import time
import os
import json
import pygame
import librosa
import numpy as np
import noisereduce as nr
import sounddevice as sd
import tensorflow as tf
import speech_recognition as sr

from queue import Queue
from scipy.io import wavfile
from scipy.io.wavfile import write 
from tensorflow.keras.models import load_model
from threading import Thread, Lock, current_thread

# Importing other file.
import file_Path, mostly_Used_Function 

# Importing class.
import open_Application
from front_End_Code import frontend


class Numa_VoiceAssistant(object):
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
        
        :var json_Path (str) : Path of JSON file.
        :var data (dic) : Dictonary that hold the value of JOSON file loaded.
        """
        
        json_Path = file_Path.english_Json_Path
        with open(json_Path, "r") as json_Data:
            data = json.load(json_Data)
        
        return data 
        
    ######################
    def prediction(self, queue_Thread_Prediction, lock_Thread_Prediction):        
        """
        Prediction method to predict the word from the user in real time.

        :param queue_Thread_Prediction : It helps to get the output from thread.
        :param lock_Thread_Prediction : It helps therad from getting race condition.
        
        :var fps: frame per second.
        :var duaration : Record time duration.
        :var filename : audio path.
        :var mapping_Data : Loding the data to compare with our real time audio.
        :var data (dict) : Dictonary which hold our data infomation.
        :var mapping_Data : Mapping Data to map with user voice.
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
                
                # Reducing Noise
                rate, clean_Audio_Data = wavfile.read(filename)
                nr.reduce_noise(np.reshape(clean_Audio_Data, (2, -1)), rate)
                
                write("user_Audio/clean_Audio.wav", fps, clean_Audio_Data)
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
                
            except Exception as error:
                print("Error in prediction class.", error)
    
    ######################
    def main(self, label_Language_Info):
        """
        main method to execute program.
        
        :param label_Language_Info (widget) : Frontend Label widget where user voice command will be displayed as text.
        
        :var run_Once
        :var wake_Word (String) : Wake word of "Numa" Voice Assistant.
        
        """
        
        try:
            # print("Current thread: {}".format(current_thread().name))
            
            print("Say Wake Word: ")
            wake_Word = "numa"
            count_Outside = 0
            
            while True:
                """
                Using while lopp because system run continuously in background to detect wake word "numa".
                
                :var predicted_keyword (String): Output/Prediction of our model.
                """
                
                # Creating instance of inbuilt Queue and Lock Module.
                queue_Thread_Prediction = Queue()
                lock_Thread_Prediction = Lock()
                
                # Creating thread to predict the wakeword.
                thread_Prediction = Thread(target=self.prediction, args=(queue_Thread_Prediction,lock_Thread_Prediction))
                thread_Prediction.start()
                thread_Prediction.join()
                thread_Prediction.deamon = True
                # print("{}".format(thread_Prediction.is_alive()))
                
                # predicted wake word.
                predicted_keyword = queue_Thread_Prediction.get()
                print(predicted_keyword)
                
                # if count_Outside < 2:
                #     predicted_keyword = "No"
                # else:
                #     predicted_keyword = "numa"
                #     count_Outside = 0
                
                # count_Outside = count_Outside + 1
                
                # mostly_Used_Function.save_Awarded_Audio()
                
                if predicted_keyword == wake_Word:
                    print("Inside....")
                    
                    # Displaying GUI of application if "numa" is activated.
                    gui_object = frontend.gui_Object
                    gui_object.display_After_Minimize_Close()
                    
                    # Sending the signal as audio to inform user that numa is ready to take command.
                    mostly_Used_Function.play_Audio(file_Path.wake_Word_Sound_Effect)
                    
                    if predicted_keyword.count(wake_Word) > 0:
                        """
                        Condition to check the count of wake word is greater then zero to take next command of user.
                        
                        :var count (int) : To keep track of below while loop.
                        """
                        count = 1
                        
                        try: 
                            while True:
                                """
                                Loop to get the user main command that will execute some program.
                                
                                :var user_Command (str) : predicted_keyword.
                                """  
                                
                                # thread_Animation = Thread(target=gui_object.animation_If_User_Speak, args=(canvas,))
                                # thread_Animation.setDaemon(True)
                                # thread_Animation.start()
                                
                                # Creating thread to predict the user command voice.
                                thread_Prediction1 = Thread(target=self.prediction, args=(queue_Thread_Prediction, lock_Thread_Prediction))
                                thread_Prediction1.setDaemon(True)
                                # print("{}".format(thread_Prediction.is_alive()))
                                thread_Prediction1.start()
                                thread_Prediction1.join()
                                
                                # Stoting the value value of predicted_keyword in user_Command variable.
                                predicted_keyword = queue_Thread_Prediction.get()
                                user_Command = predicted_keyword
                                print("Inside: ",user_Command)
                                
                                # Appending the user predicted_keyword/user_Command in list_Of_Word list.
                                self.list_Of_Word.append(user_Command)
                                
                                # Displaying output in GUI of Application.
                                label_Language_Info.config(text=list_Of_Word, font=(20))
                                
                                count = count + 1
                                queue_Thread_Prediction.task_done()
                                
                                # user_Command = "open chrome"
                                # Condition to break loop after 4 iteration or 4 second because each record time is 1 second. 
                                if count == 4:
                                    """
                                    Program execuation code.
                                    """
                                    
                                    print(self.list_Of_Word)
                                    
                                    # To open an application of system.
                                    if "open" in user_Command:
                                        application_Name = user_Command.replace("open", "")
                                        mostly_Used_Function.produce_Voice("Opeaning " + application_Name)
                                        open_Application_Object = open_Application.Open_Application(application_Name)
                                        open_Application_Object.open_Application()
                                    
                                    
                                    # Breaking the loop after the execuation of the program.
                                    break
                                    
                        except Exception as error:
                            print("Error from class main and function main: First exception eror", error)
                        
                        self.list_Of_Word.clear()
            
                else:
                    continue 
                
        except Exception as error:
            print("Error in class main and Function main: Second exception error", error)
            
"""
Creating object of class "Numa_VoiceAssistant" for english language keyword detection. 

:var list_Of_Word (list) : List to hold user command.
"""

list_Of_Word = []

english_Object = Numa_VoiceAssistant(file_Path.english_Model_Path, list_Of_Word)

nepali_Object = Numa_VoiceAssistant(file_Path.english_Model_Path, list_Of_Word)

# Use if and else if nepali langague if you want to declear nepali object.


