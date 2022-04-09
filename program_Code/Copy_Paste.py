
        # # def user_Input_Voice():
        # #     """
            
        # #     """
            
        # #     user_Input_Label = Label(main_Body, text="Output", width=20, height=2)
        # #     user_Input_Label.grid(row=2)

        
        # # def language_After_Selection(select_language):
        # #     """output_Label = Label(main_Body, text=selected)
        # #         output_Labele.grid()
            
        # #     """
            
        # #     selected_Language = select_Language.get()
            
             
        # #     if selected_Language == "Nepali":
        # #         """
        # #         selected_Language equal to Nepali Language (Call object of nepali_Object)
                
        # #         """
                
        # #         print("Nepali Langague")
        # #         user_Input_Voice()
                
            
        # #     elif selected_Language == "English":
        # #         """
        # #         selected langage equal to English Language (Call object of english_Object)
                
        # #         """
        # #         # object1 = main.english_Object
        # #         # object1.main()
        # #         print("English Langague")
                
        # #     else:
        # #         print("No langauge Selected.")
                
        # # user_Input_Voice()
        
        
        
        
        
        
        
        
        
        
        #  """
        # Making prediction using english model we create.

        # :param fps: frame per second.
        # :param duaration : Record time duration.
        # :param filename : audio path.
        # :param mapping_Data : Loding the data to compare with our real time audio.
        # """

        # fps = 44100
        # duration = 1
        # filename = "prediction.wav"
        # data = self.crossponding_Word()
        # mapping_Data = data["mappings"]
        
        # print("Prediction Started: ")
        # while True:
            
        #     """
        #     :param myrecording :  Audio to predict real time user voice.
        #     :param prediction :  Prediction of real time audio voice.
        #     :param predicted_index : Hold the max prediction value of our model.
        #     :param predicted_keyword : Text word with which our voice will get compared. 
        #     """
        #     try:
        #         # Real time audio recording.  
        #         print("Say Now: ")
        #         myrecording = sd.rec(int(duration * fps), samplerate=fps, channels=2)
        #         sd.wait()
        #         write(filename, fps, myrecording)
                
        #         # Loading the recorded file using librosa.
        #         signal, sample_rate = librosa.load(filename)
                
        #         # Extracting the MFCC feature of an audio
        #         mfcc = librosa.feature.mfcc(signal, sample_rate, n_mfcc=13, hop_length=512, n_fft=2048)
                
        #         # Making prediction and comparing our audio mfcc with the mfcc of train audio data
        #         prediction = english_Model_Path.predict(tf.expand_dims(mfcc.T, axis=0))
                
        #         # Finding max prediction value and mapping with the index of mapping_Data from json. 
        #         predicted_index = np.argmax(prediction)
        #         predicted_keyword = mapping_Data[predicted_index]
        #         print(predicted_keyword)
                
        #         # To stop the audio record.
        #         stop = input("Enter S or s to stop: ")
        #         if stop == "s" or stop == "S":
        #             break

        #         else:
        #             continue
                    
        #     except Exception as error:
        #         print(error)
        #         continue
        
        
            # user_Input_Voice()
                    # object_Nepali = main.english_Object
                    # object_Nepali.backend_Threading()
                    # try:
                    #     object_Nepali = main.english_Object
                    #     thread_Nepali= threading.Thread(target=object_Nepali.main)
                    #     thread_Nepali.start()
                    #     time.sleep(1)
                        
                    # except Exception as error:
                    #     print("Exception from frontend : thread_Nepali")
                    
                    
                    
                    
                    
                    """
Code to execute the program.
"""

# Importing Inbuilt Libarary.
import time
from threading import Thread
from queue import Queue


# Importing other class and function/method.
import file_Path
from front_End_Code import gui_Object
import mostly_Used_Function
import main 

class Run_Numa():
    """
    Run_Numa class contain the the function to execute the application.
    
    """
    
    def __init__(self):
        """
        
        """
        pass
    
    def wake_Word_Detect(self, object_Backend):
        """
        
        """


        print("Say Wake Word: ")
        wake_Word = "numa"
            
        queue_Thread_Prediction = Queue()
            
        thread_Prediction = Thread(target=object_Backend.prediction, args=(queue_Thread_Prediction,))
        thread_Prediction.start()
            
        wake_Word_Prediction = queue_Thread_Prediction.get()
        print(wake_Word_Prediction)
        return wake_Word_Prediction
        
            
    def run_Numa(self):
        """
        run_Numa function contain the code to execute the application.
        """
        
        wake_Word = "numa"
        
        while True:
            object_Backend = main.english_Object
            wake_Word_Prediction = self.wake_Word_Detect(object_Backend)
            
            print(wake_Word_Prediction)
            count = 1
            if wake_Word_Prediction == wake_Word:
                mostly_Used_Function.play_Audio(file_Path.wake_Word_Sound_Effect)
                        
                if wake_Word_Prediction.count(wake_Word) > 0:
                    """
                    Condition to check the count of wake word is greater then zero to take next command of user.
                    
                    :var count (int) : To keep track of below while loop.
                    """
                    
                    object_Backend.main()
                    
                    count = count + 1
                    
                    # Breaking the loop after the execuation of the program.
                    break
                
        
                
        
        

# gui_Object.numa_gui()

# object_English = main.english_Object
# object_English.main()

object_Numa = Run_Numa()
object_Numa.run_Numa()

